"""This module automatically imports all requirements for custom nodes.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources
without path modifications which caused issues in the past."""

import inspect
import sys
import os


if os.environ['RYVEN_MODE'] == 'gui':

    from ryvencore_qt import NodeInputBP, NodeOutputBP, dtypes
    from nodes.NodeBase import NodeBase as Node

else:

    # import sources directly from backend if not running in gui mode
    from ryvencore_qt.src.ryvencore import Node as _Node, NodeInputBP, NodeOutputBP, dtypes

    class Node(_Node):
        """
        Wraps the nodes s.t. their usages of ryvencore-qt or Ryven features don't brake them.
        """

        def __init__(self, params):
            self.special_actions = dict()
            super().__init__(params)


from tools import load_from_file
# from inspect import stack


def import_widgets(origin_file: str, rel_file_path='widgets.py'):
    """
    Import all exported widgets from 'widgets.py' with respect to the origin_file location.
    Returns an object with all exported widgets as attributes for direct access.
    """

    caller_location = os.path.dirname(origin_file)

    # alternative solution without __file__ argument; does not work with debugging, so it's not the best idea
    #   caller_location = os.path.dirname(stack()[1].filename)  # getting caller file path from stack frame

    abs_path = os.path.join(caller_location, rel_file_path)

    if os.environ['RYVEN_MODE'] == 'gui':

        # import the widgets module
        load_from_file(abs_path)

        # in GUI mode, import the widgets container from NWENV containing all the exported widget classes
        import NWENV
        widgets_container = NWENV.WidgetsRegistry.exported_widgets[-1]

    else:
        # in non-gui mode, return an object that just returns None for all accessed attributes
        # so widgets.MyWidget in the nodes file just returns None then
        class PlaceholderWidgetsContainer:
            def __getattr__(self, item):
                return None
        widgets_container = PlaceholderWidgetsContainer()

    return widgets_container

# ------------------------------------------------------


class NodesRegistry:
    """
    Stores the nodes exported via export_nodes on import of a nodes package.
    After running the imported nodes.py module (which causes export_nodes() to run),
    Ryven can find the exported nodes in exported_nodes.
    """
    exported_nodes: [[Node]] = []
    exported_node_sources: [[str]] = []


def export_nodes(*args):
    """
    Exports/exposes the specified nodes to Ryven for use in flows.
    """

    nodes = list(args)
    NodesRegistry.exported_nodes.append(nodes)

    # get sources
    node_sources = [inspect.getsource(n) for n in nodes]
    NodesRegistry.exported_node_sources.append(node_sources)


# ------------------------------------------------------