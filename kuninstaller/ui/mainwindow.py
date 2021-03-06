# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(563, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(81, 71))
        self.label_2.setMaximumSize(QtCore.QSize(81, 71))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 4, 0, 1, 3)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.treeWidget.setIconSize(QtCore.QSize(20, 20))
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_2.addWidget(self.treeWidget, 3, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(251, 32))
        self.lineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 29))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionKuninstaller_settings = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("settings-configure")
        self.actionKuninstaller_settings.setIcon(icon)
        self.actionKuninstaller_settings.setObjectName("actionKuninstaller_settings")
        self.actionAbout_Kuninstaller = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAbout_Kuninstaller.setIcon(icon)
        self.actionAbout_Kuninstaller.setObjectName("actionAbout_Kuninstaller")
        self.actionAbout_KDE = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("kde")
        self.actionAbout_KDE.setIcon(icon)
        self.actionAbout_KDE.setObjectName("actionAbout_KDE")
        self.actionUninstall = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("package-remove")
        self.actionUninstall.setIcon(icon)
        self.actionUninstall.setObjectName("actionUninstall")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help-about")
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionKuninstaller_settings)
        self.menuHelp.addAction(self.actionAbout_Kuninstaller)
        self.menuHelp.addAction(self.actionAbout_KDE)
        self.menuProgram.addAction(self.actionUninstall)
        self.menuProgram.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kuninstaller"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">Uninstall program</span></p><p>To uninstall a program, select it from the list and then right-click and select Uninstall or About.</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Current program"))
        self.label_4.setText(_translate("MainWindow", "Total size: x MB"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Description"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search programs ..."))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuSettings.setTitle(_translate("MainWindow", "Sett&ings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuProgram.setTitle(_translate("MainWindow", "P&rogram"))
        self.actionQuit.setText(_translate("MainWindow", "&Refresh"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionKuninstaller_settings.setText(_translate("MainWindow", "&Kuninstaller settings ..."))
        self.actionAbout_Kuninstaller.setText(_translate("MainWindow", "&About Kuninstaller"))
        self.actionAbout_KDE.setText(_translate("MainWindow", "About &KDE"))
        self.actionUninstall.setText(_translate("MainWindow", "&Uninstall"))
        self.actionAbout.setText(_translate("MainWindow", "&About this package"))

