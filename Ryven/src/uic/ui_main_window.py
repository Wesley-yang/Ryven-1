# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1368, 908)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionImport_Nodes = QAction(MainWindow)
        self.actionImport_Nodes.setObjectName(u"actionImport_Nodes")
        self.actionSave_Project = QAction(MainWindow)
        self.actionSave_Project.setObjectName(u"actionSave_Project")
        self.actionDesignDark_Std = QAction(MainWindow)
        self.actionDesignDark_Std.setObjectName(u"actionDesignDark_Std")
        self.actionDesignDark_Tron = QAction(MainWindow)
        self.actionDesignDark_Tron.setObjectName(u"actionDesignDark_Tron")
        self.actionEnableInfoMessages = QAction(MainWindow)
        self.actionEnableInfoMessages.setObjectName(u"actionEnableInfoMessages")
        self.actionDisableInfoMessages = QAction(MainWindow)
        self.actionDisableInfoMessages.setObjectName(u"actionDisableInfoMessages")
        self.actionSave_Pic_Viewport = QAction(MainWindow)
        self.actionSave_Pic_Viewport.setObjectName(u"actionSave_Pic_Viewport")
        self.actionSave_Pic_Whole_Scene_scaled = QAction(MainWindow)
        self.actionSave_Pic_Whole_Scene_scaled.setObjectName(u"actionSave_Pic_Whole_Scene_scaled")
        self.actionRe_Import_Nodes = QAction(MainWindow)
        self.actionRe_Import_Nodes.setObjectName(u"actionRe_Import_Nodes")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_vertical_splitter = QSplitter(self.centralWidget)
        self.main_vertical_splitter.setObjectName(u"main_vertical_splitter")
        self.main_vertical_splitter.setOrientation(Qt.Vertical)
        self.main_horizontal_splitter = QSplitter(self.main_vertical_splitter)
        self.main_horizontal_splitter.setObjectName(u"main_horizontal_splitter")
        self.main_horizontal_splitter.setOrientation(Qt.Horizontal)
        self.left_vertical_splitter = QSplitter(self.main_horizontal_splitter)
        self.left_vertical_splitter.setObjectName(u"left_vertical_splitter")
        self.left_vertical_splitter.setOrientation(Qt.Vertical)
        self.scripts_groupBox = QGroupBox(self.left_vertical_splitter)
        self.scripts_groupBox.setObjectName(u"scripts_groupBox")
        self.verticalLayout = QVBoxLayout(self.scripts_groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.left_vertical_splitter.addWidget(self.scripts_groupBox)
        self.main_horizontal_splitter.addWidget(self.left_vertical_splitter)
        self.scripts_tab_widget = QTabWidget(self.main_horizontal_splitter)
        self.scripts_tab_widget.setObjectName(u"scripts_tab_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scripts_tab_widget.sizePolicy().hasHeightForWidth())
        self.scripts_tab_widget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.scripts_tab_widget.addTab(self.tab, "")
        self.main_horizontal_splitter.addWidget(self.scripts_tab_widget)
        self.main_vertical_splitter.addWidget(self.main_horizontal_splitter)
        self.bottom_splitter = QSplitter(self.main_vertical_splitter)
        self.bottom_splitter.setObjectName(u"bottom_splitter")
        self.bottom_splitter.setOrientation(Qt.Horizontal)
        self.main_vertical_splitter.addWidget(self.bottom_splitter)

        self.gridLayout.addWidget(self.main_vertical_splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1368, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuFlow_Design_Style = QMenu(self.menuView)
        self.menuFlow_Design_Style.setObjectName(u"menuFlow_Design_Style")
        self.menuSave_Picture = QMenu(self.menuView)
        self.menuSave_Picture.setObjectName(u"menuSave_Picture")
        self.menuDebugging = QMenu(self.menuBar)
        self.menuDebugging.setObjectName(u"menuDebugging")
        self.menuInfo_Messages = QMenu(self.menuDebugging)
        self.menuInfo_Messages.setObjectName(u"menuInfo_Messages")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuDebugging.menuAction())
        self.menuFile.addAction(self.actionImport_Nodes)
        self.menuFile.addAction(self.actionRe_Import_Nodes)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuFlow_Design_Style.menuAction())
        self.menuView.addAction(self.menuSave_Picture.menuAction())
        self.menuSave_Picture.addAction(self.actionSave_Pic_Viewport)
        self.menuSave_Picture.addAction(self.actionSave_Pic_Whole_Scene_scaled)
        self.menuDebugging.addAction(self.menuInfo_Messages.menuAction())
        self.menuInfo_Messages.addAction(self.actionEnableInfoMessages)
        self.menuInfo_Messages.addAction(self.actionDisableInfoMessages)

        self.retranslateUi(MainWindow)

        self.scripts_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport_Nodes.setText(QCoreApplication.translate("MainWindow", u"Import Nodes", None))
        self.actionSave_Project.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionDesignDark_Std.setText(QCoreApplication.translate("MainWindow", u"Dark Std", None))
        self.actionDesignDark_Tron.setText(QCoreApplication.translate("MainWindow", u"Dark Tron", None))
        self.actionEnableInfoMessages.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.actionDisableInfoMessages.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.actionSave_Pic_Viewport.setText(QCoreApplication.translate("MainWindow", u"Save Pic - Viewport", None))
#if QT_CONFIG(tooltip)
        self.actionSave_Pic_Viewport.setToolTip(QCoreApplication.translate("MainWindow", u"Save a picture of the current scene's viewport.\n"
"This will save exactly what you see in the same resolution.", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_Pic_Whole_Scene_scaled.setText(QCoreApplication.translate("MainWindow", u"Save Pic - Whole Scene (scaled)", None))
#if QT_CONFIG(tooltip)
        self.actionSave_Pic_Whole_Scene_scaled.setToolTip(QCoreApplication.translate("MainWindow", u"Saves a picture of the whole current scene. \n"
"The more you zoomed in, the sharper the picture.\n"
"This will take a few seconds.", None))
#endif // QT_CONFIG(tooltip)
        self.actionRe_Import_Nodes.setText(QCoreApplication.translate("MainWindow", u"Re-Import Nodes", None))
        self.scripts_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.scripts_tab_widget.setTabText(self.scripts_tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFlow_Design_Style.setTitle(QCoreApplication.translate("MainWindow", u"Flow Theme", None))
        self.menuSave_Picture.setTitle(QCoreApplication.translate("MainWindow", u"Save Picture", None))
        self.menuDebugging.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuInfo_Messages.setTitle(QCoreApplication.translate("MainWindow", u"Info Messages", None))
    # retranslateUi

