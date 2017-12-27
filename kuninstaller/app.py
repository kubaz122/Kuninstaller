#! /usr/bin/env python3
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, uic
from hurry.filesize import size
from kuninstaller.ui import mainwindow, aboutpackagedialog, removepkgdialog, settings
import os, configparser, locale, apt, subprocess, time

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionQuit.triggered.connect(self.loadProgramsList)
        self.loadProgramsList()
        self.ui.lineEdit.textChanged.connect(self.searchInList)
        self.ui.treeWidget.itemClicked[QtWidgets.QTreeWidgetItem, int].connect(self.printAppInfo)
        self.ui.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.treeWidget.customContextMenuRequested.connect(self.openMenu)
        self.ui.widget.setVisible(False)
        self.ui.actionKuninstaller_settings.triggered.connect(self.editSettings)
        self.ui.actionAbout_Kuninstaller.triggered.connect(self.aboutKuninstaller)
        self.ui.actionAbout_KDE.triggered.connect(self.aboutKDE)

        self.loadSettings()

    def aboutKDE(self):
        os.popen("x-www-browser https://www.kde.org/community/whatiskde/")
    def aboutKuninstaller(self):
        aboutdialog = QtWidgets.QDialog(self)
        uic.loadUi("./designer/about.ui", aboutdialog)
        aboutdialog.show()
    
    def editSettings(self):
        self.settingseditor = SettingsEditor(self.iconsize, self.sorting, self.autoremove)
        self.settingseditor.applysignal.connect(self.applySettings)
        retval = self.settingseditor.exec_()
        if retval == 1:
            self.saveSettings()
        
    def saveSettings(self):        
        config = configparser.ConfigParser()
        config.read(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf")
        
        config["Kuninstaller"]["icon_size"] = str(self.iconsize) 
        config["Kuninstaller"]["sorting"] = str(self.sorting)
        config["Kuninstaller"]["autoremove"] = str(self.autoremove)
    
        with open(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf", 'w') as configfile:
            config.write(configfile)
            
    def applySettings(self, iconsize,sorting,autoremove):
        self.iconsize = iconsize
        self.sorting = sorting
        self.autoremove = autoremove
        
        self.ui.treeWidget.setIconSize(QtCore.QSize(self.iconsize, self.iconsize))
        self.ui.treeWidget.setSortingEnabled(self.sorting)
        
    def loadSettings(self):
        if not os.path.isfile(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf"):
            os.makedirs(os.path.expanduser("~") + "/.config/Kuninstaller")
            open(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf", "a").close()
            with open(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf", "w") as fconf:
                fconf.write("""[Kuninstaller]
icon_size = 20
sorting = False
autoremove = True""")
            self.loadSettings()
        config = configparser.ConfigParser()
        config.read(os.path.expanduser("~") + "/.config/Kuninstaller/settings.conf")
        
        self.iconsize = config["Kuninstaller"].getint("icon_size")
        self.sorting = config["Kuninstaller"].getboolean("sorting")
        self.autoremove = config["Kuninstaller"].getboolean("autoremove")

        self.ui.treeWidget.setIconSize(QtCore.QSize(self.iconsize, self.iconsize))
        self.ui.treeWidget.setSortingEnabled(self.sorting)
                
        
    def uninstallPkg(self):
        item = self.ui.treeWidget.currentItem()
        try:
            package = item.pkgname
        except:
            pkgname = subprocess.getoutput("dpkg -S '" + item.appconf + "'")
            pkgname = pkgname.replace(": " + item.appconf, "")
            cache = apt.Cache()
            package = pkgname
        desktopconf = item.appconf
        
        buttonReply = QtWidgets.QMessageBox.question(self, package, "Uninstall " + item.text(0) + "?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            cache = apt.Cache()
            try:
                pkg = cache[package]
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('The package can not be recognized.')
                error_dialog.exec_()
                return None
            self.installprogress = RemovePkg(package, desktopconf)
            self.installprogress.exec_()
        else:
            return False
            
        self.loadProgramsList()
        
    def aboutCurrentPkg(self):
        item = self.ui.treeWidget.currentItem()
        try:
            package = item.pkgname
        except:
            pkgname = subprocess.getoutput("dpkg -S '" + item.appconf + "'")
            pkgname = pkgname.replace(": " + item.appconf, "")
            cache = apt.Cache()
            package = pkgname
            
        desktopconf = item.appconf
        self.dialog = aboutPackageDialog(package, desktopconf)
        self.dialog.exec_()
    def openMenu(self, position):
        indexes = self.ui.treeWidget.selectedIndexes()
        if len(indexes) > 0:           
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
        _translate = QtCore.QCoreApplication.translate
        menu = QtWidgets.QMenu()
        menu.addAction(QtGui.QIcon.fromTheme("package-remove"), _translate('MainWindow',"Uninstall"), self.uninstallPkg)
        menu.addAction(QtGui.QIcon.fromTheme("help-about"), _translate('MainWindow', "About this package"), self.aboutCurrentPkg)
        menu.exec_(self.ui.treeWidget.viewport().mapToGlobal(position))
    def printAppInfo(self, item, col):
        
        self.ui.widget.setVisible(True)
        
        icon = item.icon(0)
        self.ui.label_2.setPixmap(icon.pixmap(icon.actualSize(QtCore.QSize(81, 71))))
        self.ui.label_3.setText(item.text(0))
        pkgname = subprocess.getoutput("dpkg -S '" + item.appconf + "'")
        pkgname = pkgname.replace(": " + item.appconf, "")
        cache = apt.Cache()
        item.pkgname = pkgname
        try:
            pkg = cache[pkgname]
        except:
            item.removeChild(item)
            return SystemError("The package can not be recognized.")
        self.ui.label_4.setText("Total size: " + str(size(pkg.versions[0].size)))
    def searchInList(self):
        searchstr = self.ui.lineEdit.text()
        items = self.ui.treeWidget.findItems(searchstr,QtCore.Qt.MatchContains , 0)
        root = self.ui.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            if not item in items:
                item.setHidden(True)
            else:
                item.setHidden(False)
    def loadProgramsList(self):
        self.ui.treeWidget.clear()
        lang = locale
        lang = lang[:2]
        for root, dirs, files in os.walk("/usr/share/applications/", topdown=False):
            for name in (x for x in files if x.endswith(".desktop")):
                appconf = os.path.join(root, name)
                config = configparser.ConfigParser()
                config.read(appconf)
                if not config["Desktop Entry"].getboolean('NoDisplay'):
                    item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
                    if "Name[" + lang + "]" in config["Desktop Entry"]:
                        item.setText(0, config["Desktop Entry"]["Name[" + lang + "]"])
                    else:
                        item.setText(0, config["Desktop Entry"]["Name"])
                    if "Comment" in config["Desktop Entry"]:
                        item.setText(1, config["Desktop Entry"]["Comment"])
                    if "Icon" in config["Desktop Entry"] and os.path.isfile(config["Desktop Entry"]["Icon"]):
                        item.setIcon(0, QtGui.QIcon(QtGui.QPixmap(config["Desktop Entry"]["Icon"])))
                    elif "Icon" in config["Desktop Entry"]:
                        item.setIcon(0, QtGui.QIcon.fromTheme(config["Desktop Entry"]["Icon"]))
                    item.appconf = appconf
        self.ui.treeWidget.resizeColumnToContents(0)

class aboutPackageDialog(QtWidgets.QDialog):
    def __init__(self, package, desktopconf):
        QtWidgets.QDialog.__init__(self)
        self.ui = aboutpackagedialog.Ui_Dialog()
        self.ui.setupUi(self)
        
        config = configparser.ConfigParser()
        config.read(desktopconf)
        lang = locale
        lang = lang[0]
        lang = lang[:2]
        if "Name[" + lang + "]" in config["Desktop Entry"]:
            self.ui.label.setText(config["Desktop Entry"]["Name[" + lang + "]"])
        else:
            self.ui.label.setText(config["Desktop Entry"]["Name"])
        if "Icon" in config["Desktop Entry"] and os.path.isfile(config["Desktop Entry"]["Icon"]):
            self.ui.label_2.setPixmap(QtGui.QPixmap(config["Desktop Entry"]["Icon"]))
        elif "Icon" in config["Desktop Entry"]:
            icon = QtGui.QIcon.fromTheme(config["Desktop Entry"]["Icon"])
            self.ui.label_2.setPixmap(icon.pixmap(icon.actualSize(QtCore.QSize(81, 71))))
        
        self.ui.textBrowser.setVisible(False)
        self.ui.label_3.setText("Package: " + package)
        
        cache = apt.Cache()
        try:
            pkg = cache[package]
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('The package can not be recognized.')
            error_dialog.exec_()
            self.close()
            return None
        
        self.ui.label_4.setText("Size: " + str(size(pkg.versions[0].size)))
        self.ui.textBrowser.setText(pkg.versions[0].raw_description)
        
        
class RemovePkg(QtWidgets.QDialog):
    def __init__(self, package, desktopconf):
        QtWidgets.QDialog.__init__(self)
        self.ui = removepkgdialog.Ui_Dialog()
        self.ui.setupUi(self)

        config = configparser.ConfigParser()
        config.read(desktopconf)
        lang = locale
        lang = lang[0]
        lang = lang[:2]
        if "Icon" in config["Desktop Entry"] and os.path.isfile(config["Desktop Entry"]["Icon"]):
            self.ui.label_2.setPixmap(QtGui.QPixmap(config["Desktop Entry"]["Icon"]))
        elif "Icon" in config["Desktop Entry"]:
            icon = QtGui.QIcon.fromTheme(config["Desktop Entry"]["Icon"])
            self.ui.label_2.setPixmap(icon.pixmap(icon.actualSize(QtCore.QSize(81, 71))))
        if "Name[" + lang + "]" in config["Desktop Entry"]:
            self.ui.label.setText(config["Desktop Entry"]["Name[" + lang + "]"])
        else:
            self.ui.label.setText(config["Desktop Entry"]["Name"])
        
        if MainWindow().autoremove:
            command = "pkexec sudo apt-get autoremove -y " + package
        else:
            command = "pkexec sudo apt-get remove -y " + package
        process = QtCore.QProcess(self)
        process.finished.connect(self.onFinished)
        process.start(command)

    def onFinished(self):
        self.close()
        
class SettingsEditor(QtWidgets.QDialog):
    applysignal = QtCore.pyqtSignal(int, bool, bool)
    def __init__(self, iconsize, sorting, autoremove):
        QtWidgets.QDialog.__init__(self)
        self.ui = settings.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.changeSettings()
        btn = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Apply)
        btn.clicked.connect(self.applySettingsConnect)
        btn = self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        btn.clicked.connect(self.okSettingsConnect)
        
        self.ui.checkBox.setChecked(sorting)
        self.ui.checkBox_2.setChecked(autoremove)
        self.ui.spinBox.setValue(iconsize)
        
        self.ui.checkBox.stateChanged.connect(self.changeSettings)
        self.ui.spinBox.valueChanged.connect(self.changeSettings)
        self.ui.checkBox_2.stateChanged.connect(self.changeSettings)
    
    def okSettingsConnect(self):
        self.applysignal.emit(self.iconsize, self.sorting, self.autoremove)
        self.accept()
    def changeSettings(self):
        self.iconsize = self.ui.spinBox.value()
        self.sorting = self.ui.checkBox.checkState()
        self.autoremove = self.ui.checkBox_2.checkState()
    def applySettingsConnect(self):
        self.applysignal.emit(self.iconsize, self.sorting, self.autoremove)
        


        
app = QtWidgets.QApplication(sys.argv)


locale = QtCore.QLocale.system().name()
qtTranslator = QtCore.QTranslator()

if qtTranslator.load("i18n/Kuninstaller_" + locale):
    app.installTranslator(qtTranslator)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
