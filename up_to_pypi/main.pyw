from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import qtmodern.styles
import qtmodern.windows
import webbrowser

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QProcess, QTextCodec
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextBrowser, QMessageBox

class ProcessOutputReader(QProcess):
    produce_output = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setProcessChannelMode(QProcess.MergedChannels)
        codec = QTextCodec.codecForLocale()
        self._decoder_stdout = codec.makeDecoder()
        self.readyReadStandardOutput.connect(self._ready_read_standard_output)

    @pyqtSlot()
    def _ready_read_standard_output(self):
        raw_bytes = self.readAllStandardOutput()
        text = self._decoder_stdout.toUnicode(raw_bytes)
        self.produce_output.emit(text)

class output_console(QTextBrowser):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFont(QtGui.QFont('Roboto', 11))
        self.setReadOnly(True)
        self._cursor_output = self.textCursor()

    @pyqtSlot(str)
    def append_output(self, text):
        self._cursor_output.insertText(text)
        self.scroll_to_last_line()

    def scroll_to_last_line(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.movePosition(QTextCursor.Up if cursor.atBlockStart() else
                            QTextCursor.StartOfLine)
        self.setTextCursor(cursor)

# Globals
count_password_switch = 0
loaded = False
opf_folder_location = ""
abs_path = os.path.dirname(__file__)
reader = ProcessOutputReader()
theme_count = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setStatusTip("")
        self.c2.setObjectName("c2")
        self.gridLayout_2.addWidget(self.c2, 0, 1, 1, 1)
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setChecked(False)
        self.c4.setObjectName("c4")
        self.gridLayout_2.addWidget(self.c4, 1, 1, 1, 1)
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setChecked(False)
        self.c1.setObjectName("c1")
        self.gridLayout_2.addWidget(self.c1, 0, 0, 1, 1)
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setStatusTip("")
        self.c3.setWhatsThis("")
        self.c3.setChecked(False)
        self.c3.setTristate(False)
        self.c3.setObjectName("c3")
        self.gridLayout_2.addWidget(self.c3, 1, 0, 1, 1)
        self.opf = QtWidgets.QPushButton(self.centralwidget)
        self.opf.setObjectName("opf")
        self.gridLayout_2.addWidget(self.opf, 3, 0, 1, 1)
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setObjectName("c5")
        self.gridLayout_2.addWidget(self.c5, 2, 0, 1, 1)
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setStatusTip("")
        self.c6.setChecked(False)
        self.c6.setObjectName("c6")
        self.gridLayout_2.addWidget(self.c6, 2, 1, 1, 1)
        self.abort = QtWidgets.QPushButton(self.centralwidget)
        self.abort.setObjectName("abort")
        self.gridLayout_2.addWidget(self.abort, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        self.pypi_password = QtWidgets.QLineEdit(self.centralwidget)
        self.pypi_password.setText("")
        self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pypi_password.setObjectName("pypi_password")
        self.gridLayout.addWidget(self.pypi_password, 3, 0, 1, 1)
        self.commands_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.commands_box.setObjectName("commands_box")
        self.gridLayout.addWidget(self.commands_box, 14, 0, 1, 2)
        self.pypi_username = QtWidgets.QLineEdit(self.centralwidget)
        self.pypi_username.setObjectName("pypi_username")
        self.gridLayout.addWidget(self.pypi_username, 2, 0, 1, 2)
        self.commands = QtWidgets.QLabel(self.centralwidget)
        self.commands.setObjectName("commands")
        self.gridLayout.addWidget(self.commands, 13, 0, 1, 1)
        self.details = QtWidgets.QLabel(self.centralwidget)
        self.details.setObjectName("details")
        self.gridLayout.addWidget(self.details, 1, 0, 1, 2)
        self.show_hide = QtWidgets.QPushButton(self.centralwidget)
        self.show_hide.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_hide.setIcon(icon1)
        self.show_hide.setFlat(False)
        self.show_hide.setObjectName("show_hide")
        self.gridLayout.addWidget(self.show_hide, 3, 1, 1, 1)
        self.output_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 16, 0, 1, 2)
        self.settings = QtWidgets.QLabel(self.centralwidget)
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 4, 0, 1, 2)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 15, 0, 1, 1)
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setIcon(icon)
        self.upload.setObjectName("upload")
        self.gridLayout.addWidget(self.upload, 12, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 292, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuThemes = QtWidgets.QMenu(self.menuSettings)
        self.menuThemes.setObjectName("menuThemes")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(True)
        self.actionDark.setChecked(False)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setCheckable(True)
        self.actionLight.setObjectName("actionLight")
        self.actionAbout_Up_To_PyPi = QtWidgets.QAction(MainWindow)
        self.actionAbout_Up_To_PyPi.setObjectName("actionAbout_Up_To_PyPi")
        self.actionOpen_Project_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project_Folder.setObjectName("actionOpen_Project_Folder")
        self.actionSave_User = QtWidgets.QAction(MainWindow)
        self.actionSave_User.setCheckable(True)
        self.actionSave_User.setChecked(False)
        self.actionSave_User.setObjectName("actionSave_User")
        self.actionClear_Text_Fields = QtWidgets.QAction(MainWindow)
        self.actionClear_Text_Fields.setObjectName("actionClear_Text_Fields")
        self.actionReset_To_Default = QtWidgets.QAction(MainWindow)
        self.actionReset_To_Default.setObjectName("actionReset_To_Default")
        self.actionSave_PyPi_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_PyPi_Settings.setCheckable(True)
        self.actionSave_PyPi_Settings.setObjectName("actionSave_PyPi_Settings")
        self.actionAdvance_Wheel_Creator = QtWidgets.QAction(MainWindow)
        self.actionAdvance_Wheel_Creator.setObjectName("actionAdvance_Wheel_Creator")
        self.actionReport_A_Bug = QtWidgets.QAction(MainWindow)
        self.actionReport_A_Bug.setObjectName("actionReport_A_Bug")
        self.actionRequest_New_Features = QtWidgets.QAction(MainWindow)
        self.actionRequest_New_Features.setObjectName("actionRequest_New_Features")
        self.actionNeed_Help = QtWidgets.QAction(MainWindow)
        self.actionNeed_Help.setObjectName("actionNeed_Help")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionAbort = QtWidgets.QAction(MainWindow)
        self.actionAbort.setObjectName("actionAbort")
        self.actionSave_A_bat_File = QtWidgets.QAction(MainWindow)
        self.actionSave_A_bat_File.setObjectName("actionSave_A_bat_File")
        self.actionModule_Creator = QtWidgets.QAction(MainWindow)
        self.actionModule_Creator.setObjectName("actionModule_Creator")
        self.menuFile.addAction(self.actionOpen_Project_Folder)
        self.menuFile.addAction(self.actionSave_A_bat_File)
        self.menuThemes.addSeparator()
        self.menuThemes.addAction(self.actionDark)
        self.menuThemes.addAction(self.actionLight)
        self.menuSettings.addAction(self.menuThemes.menuAction())
        self.menuSettings.addAction(self.actionSave_User)
        self.menuSettings.addAction(self.actionSave_PyPi_Settings)
        self.menuSettings.addAction(self.actionReset_To_Default)
        self.menuHelp.addAction(self.actionReport_A_Bug)
        self.menuHelp.addAction(self.actionRequest_New_Features)
        self.menuHelp.addAction(self.actionNeed_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Up_To_PyPi)
        self.menuOptions.addAction(self.actionUpload)
        self.menuOptions.addAction(self.actionAbort)
        self.menuOptions.addAction(self.actionClear_Text_Fields)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionAdvance_Wheel_Creator)
        self.menuOptions.addAction(self.actionModule_Creator)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.show_hide.clicked.connect(self.show_hide_password)
        self.opf.clicked.connect(self.opf_popup)
        self.abort.clicked.connect(self.abort_qprocess)
        self.actionAbort.triggered.connect(lambda: self.abort_qprocess())        
        self.upload.clicked.connect(self.upload_module)
        self.actionUpload.triggered.connect(lambda: self.upload_module())

        self.c1.stateChanged.connect(self.preview_commands)
        self.c2.stateChanged.connect(self.preview_commands)
        self.c3.stateChanged.connect(self.preview_commands)
        self.c4.stateChanged.connect(self.preview_commands)
        self.c5.stateChanged.connect(self.preview_commands)
        self.c6.stateChanged.connect(self.preview_commands)
        self.pypi_username.textEdited.connect(self.preview_commands)
        self.pypi_password.textEdited.connect(self.preview_commands)

        MainWindow.resizeEvent = self.resize_text
        MainWindow.closeEvent = self.save_settings

        self.actionOpen_Project_Folder.triggered.connect(lambda: self.opf_popup())
        self.actionSave_A_bat_File.triggered.connect(lambda: self.save_bat())
        self.actionReport_A_Bug.triggered.connect(lambda: self.github_issues())
        self.actionReport_A_Bug.triggered.connect(lambda: self.github_issues())
        self.actionRequest_New_Features.triggered.connect(lambda: self.gform())
        self.actionNeed_Help.triggered.connect(lambda: self.gform())

        self.actionLight.triggered.connect(lambda: self.light_theme())
        self.actionDark.triggered.connect(lambda: self.dark_theme())
        self.actionReset_To_Default.triggered.connect(lambda: self.Settings_Reset_To_Default())
        self.actionAbout_Up_To_PyPi.triggered.connect(lambda: self.about_uptopypi())

        self.actionClear_Text_Fields.triggered.connect(lambda: self.pypi_username.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.pypi_password.clear())
        self.actionAdvance_Wheel_Creator.triggered.connect(lambda: self.open_awc())
        self.actionModule_Creator.triggered.connect(lambda: self.open_crmod())

        # Moving Window To Center
        qr = QtCore.QRect(0, 0, 640, 470)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Up To PyPi"))
        self.commands.setText(_translate("MainWindow", "Commands Going To Execute :-"))
        self.commands_box.setText(_translate("MainWindow", "python setup.py sdist bdist_wheel\ntwine upload dist/* -u   -p  "))
        self.settings.setText(_translate("MainWindow", "Settings :-"))
        self.pypi_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.details.setText(_translate("MainWindow", "PyPI Details :-"))
        self.pypi_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.c1.setToolTip(_translate("MainWindow", "Upload realese at pypi.org"))
        self.c1.setText(_translate("MainWindow", "Upload At PyPi"))
        self.c3.setToolTip(_translate("MainWindow", "Creates a whl and tar.gz file of program using setup.py file."))
        self.c3.setText(_translate("MainWindow", "Create Wheel"))
        self.c2.setToolTip(_translate("MainWindow", "Upload realese at test.pypi.org"))
        self.c2.setText(_translate("MainWindow", "Upload At Test PyPi"))
        self.c5.setToolTip(_translate("MainWindow", "Install main uploading package i.e. twine."))
        self.c5.setText(_translate("MainWindow", "Install Twine"))
        self.c6.setToolTip(_translate("MainWindow", "Upgrades twine to latest version."))
        self.c6.setText(_translate("MainWindow", "Upgrade Twine"))
        self.c4.setToolTip(_translate("MainWindow", "Upgrade setuptools and wheel to latest version"))
        self.c4.setText(_translate("MainWindow", "Upgrade Setuptools + Wheel"))
        self.opf.setText(_translate("MainWindow", "Open Project Folder"))
        self.abort.setText(_translate("MainWindow", "Abort"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionAbout_Up_To_PyPi.setText(_translate("MainWindow", "About Up To PyPi"))
        self.actionOpen_Project_Folder.setText(_translate("MainWindow", "Open Project Folder"))
        self.actionSave_User.setText(_translate("MainWindow", "Save User"))
        self.actionClear_Text_Fields.setText(_translate("MainWindow", "Clear Text Fields"))
        self.actionClear_Text_Fields.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionReset_To_Default.setText(_translate("MainWindow", "Reset To Default"))
        self.actionSave_PyPi_Settings.setText(_translate("MainWindow", "Save PyPi Settings"))
        self.actionAdvance_Wheel_Creator.setText(_translate("MainWindow", "Advance Wheel Creator"))
        self.actionReport_A_Bug.setText(_translate("MainWindow", "Report A Bug"))
        self.actionRequest_New_Features.setText(_translate("MainWindow", "Request New Features"))
        self.actionNeed_Help.setText(_translate("MainWindow", "Need Help ?"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionAbort.setText(_translate("MainWindow", "Abort"))
        self.actionSave_A_bat_File.setText(_translate("MainWindow", "Save A .bat File"))
        self.actionSave_A_bat_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.output.setText(_translate("WheelWindow", "Output Terminal :-"))
        self.output_box.setText(_translate("WheelWindow", "NULL"))
        self.actionModule_Creator.setText(_translate("MainWindow", "Module Creator"))

        self.output.deleteLater()
        self.output_box.deleteLater()

    def resize_text(self, event):
        default_size = 11
        width = MainWindow.frameGeometry().width()

        if width // 100> default_size:
            font_size_change = QtGui.QFont('Roboto', width // 100)
            font_size_change2 = QtGui.QFont('Roboto', width // 100)
        else:
            font_size_change = QtGui.QFont('Roboto', default_size)
            font_size_change2 = QtGui.QFont()


        self.settings.setFont(font_size_change2)
        self.details.setFont(font_size_change2)
        self.commands.setFont(font_size_change2)

        self.pypi_username.setFont(font_size_change)
        self.pypi_password.setFont(font_size_change)

        self.show_hide.setFont(font_size_change2)
        self.opf.setFont(font_size_change2)
        self.abort.setFont(font_size_change2)
        self.upload.setFont(font_size_change2)

        self.c1.setFont(font_size_change)
        self.c2.setFont(font_size_change)
        self.c3.setFont(font_size_change)
        self.c4.setFont(font_size_change)
        self.c5.setFont(font_size_change)
        self.c6.setFont(font_size_change)

        self.commands_box.setFont(font_size_change)

        if loaded:
        	self.output.setFont(font_size_change2)

    def show_hide_password(self):
        global count_password_switch
        icon = QtGui.QIcon()
        if count_password_switch%2==0:
            icon.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.show_hide.setIcon(icon)
            count_password_switch += 1
            self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            icon.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.show_hide.setIcon(icon)
            count_password_switch -= 1
            self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def opf_popup(self):
        global opf_folder_location
        opf_folder = QtWidgets.QFileDialog.getExistingDirectory()
        try:
          opf_folder_location = opf_folder
        except:
            pass

    def abort_qprocess(self):
    	try:
    		reader.kill()
    		_translate = QtCore.QCoreApplication.translate
    		self.output_box.append(_translate("MainWindow", "=============\nProcess Aborted\n============="))
    		cursor = self.output_box.textCursor()
    		cursor.movePosition(QTextCursor.End)
    		self.output_box.setTextCursor(cursor)
    	except:
    		pass

    def all_commands(self):
    	all_cmd = []
    	if self.c4.isChecked(): all_cmd.append("pip install --upgrade setuptools wheel")
    	if self.c5.isChecked(): all_cmd.append("pip install twine")
    	if self.c6.isChecked(): all_cmd.append("pip install --upgrade twine")
    	if self.c3.isChecked(): all_cmd.append("python setup.py sdist bdist_wheel")
    	if self.c1.isChecked(): all_cmd.append(f"twine upload dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}")
    	if self.c2.isChecked(): all_cmd.append(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}")
    	return all_cmd

    def preview_commands(self):
        with open (f"{abs_path}\\assets\\commands.txt", "w", encoding="utf-8") as f:
        	for commands in self.all_commands():
        		f.write(f"{commands}\n")

        if self.c4.isChecked() == False and self.c5.isChecked() == False and self.c6.isChecked() == False and self.c3.isChecked() == False and self.c1.isChecked() == False and self.c2.isChecked() == False:
            _translate = QtCore.QCoreApplication.translate
            self.commands_box.setText(_translate("MainWindow", "NULL"))

        else:
            with open (f"{abs_path}\\assets\\commands.txt", encoding="utf-8") as f:
                readings = f.read()
                _translate = QtCore.QCoreApplication.translate
                self.commands_box.setText(_translate("MainWindow", readings))

    def create_bat(self, location):
    	with open (location, "w", encoding="utf-8") as f:
    		module_dir = opf_folder_location.replace("/", "\\")
    		f.write(f'cd /d "{module_dir}"\n')
    		for commands in self.all_commands():
    			f.write(f"{commands}\n")
    			f.write("echo off\n"
		        "echo =======\n"
		        "echo FINISHED\n"
		        "echo =======\n")

    def upload_module(self):
    	global loaded

    	if loaded:
    		pass
    	else:
    		self.output = QtWidgets.QLabel(self.centralwidget)
    		self.output.setObjectName("output")
    		self.gridLayout.addWidget(self.output, 15, 0, 1, 1)
    		self.output_box = output_console(self.centralwidget)
    		self.output_box.setObjectName("output_box")
    		self.gridLayout.addWidget(self.output_box, 16, 0, 1, 2)
    		_translate = QtCore.QCoreApplication.translate
    		self.output.setText(_translate("MainWindow", "Output Terminal :-"))
    		self.output_box.setText(_translate("MainWindow", "NULL"))
    		loaded = True

    	self.create_bat(f"{abs_path}\\assets\\commands.bat")
    	os.chdir(f"{abs_path}\\assets")
    	self.output_box = output_console(self.centralwidget)
    	self.output_box.setObjectName("output_box")
    	self.gridLayout.addWidget(self.output_box, 16, 0, 1, 2)
    	reader.produce_output.connect(self.output_box.append_output)
    	reader.start('commands.bat')

    def save_bat(self):
        opf_folder = QtWidgets.QFileDialog.getSaveFileName(filter="Batch Files (*.bat)")
        location_to_save = opf_folder[0].replace("/", "\\\\")
        filename = opf_folder[0].split("/")[-1]
        try:
        	self.create_bat(location_to_save)
        	_translate = QtCore.QCoreApplication.translate
        	MainWindow.setStatusTip(_translate("MainWindow", f"{filename} Saved At {opf_folder[0]}"))

        except FileNotFoundError:
        	pass

    def github_issues(self):
    	webbrowser.open("https://github.com/360modder/up-to-pypi/issues", new=2)

    def gform(self):
    	webbrowser.open("https://docs.google.com/forms/u/1/d/e/"
    		"1FAIpQLSfgZYjhWP1grsRyiDJ35K0kPhcQbwh7n5HK-qPgoGdDKlGn-A/viewform?usp=sf_link", new=2)

    def light_theme(self):
        qtmodern.styles.light(app)
        self.actionDark.setChecked(False)
        self.actionLight.setChecked(True)
        self.save_settings(self)
        self.resize_text("")

    def dark_theme(self):
        qtmodern.styles.dark(app)
        self.actionLight.setChecked(False)
        self.actionDark.setChecked(True)
        self.save_settings(self)
        self.resize_text("")

    def Settings_Reset_To_Default(self):
        qtmodern.styles.light(app)
        self.actionLight.setChecked(True)
        self.actionDark.setChecked(False)
        self.actionSave_User.setChecked(True)
        self.actionSave_PyPi_Settings.setChecked(True)
        self.pypi_username.clear()
        self.pypi_password.clear()
        self.c1.setChecked(True)
        self.c3.setChecked(True)
        self.c2.setChecked(False)
        self.c4.setChecked(False)
        self.c5.setChecked(False)
        self.c6.setChecked(False)
        self.resize_text("")
        self.preview_commands()
        _translate = QtCore.QCoreApplication.translate
        if loaded:
        	self.output_box.setText(_translate("MainWindow", "NULL")) 
        MainWindow.setStatusTip(_translate("MainWindow", "Settings Resetted To Default"))


    def about_uptopypi(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Up To PyPi")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Up To PyPi v2.0.1")
        msg.setInformativeText("Developed By 360modder")
        msg.setDetailedText("Build With Python & PyQt5")
        msg.exec_()

    def load_settings(self):

        def check_boxes(value, cb_no):
            if value == "True":
                cb_no.setChecked(True)
            else:
                pass

        with open (f"{abs_path}\\assets\\settings.txt", encoding="utf-8") as f:
            read = f.read()
            read = read.split("\n")

            if read[0] == 'True':
                self.light_theme()
            else:
                self.dark_theme()

            if read[1] == 'True':
                self.actionSave_User.setChecked(True)
                self.pypi_username.setText(read[3])
                self.pypi_password.setText(read[4])
            else:
                pass

            if read[2] == 'True':
                self.actionSave_PyPi_Settings.setChecked(True)
                check_boxes(read[5], self.c1)
                check_boxes(read[6], self.c2)
                check_boxes(read[7], self.c3)
                check_boxes(read[8], self.c4)
                check_boxes(read[9], self.c5)
                check_boxes(read[10], self.c6)
            else:
                pass


    def save_settings(self, event):
        with open (f"{abs_path}\\assets\\settings.txt", "w", encoding="utf-8") as f:
            f.write(f"{self.actionLight.isChecked()}\n")
            f.write(f"{self.actionSave_User.isChecked()}\n")
            f.write(f"{self.actionSave_PyPi_Settings.isChecked()}\n")
            f.write(f"{self.pypi_username.text()}\n")
            f.write(f"{self.pypi_password.text()}\n")
            f.write(f"{self.c1.isChecked()}\n")
            f.write(f"{self.c2.isChecked()}\n")
            f.write(f"{self.c3.isChecked()}\n")
            f.write(f"{self.c4.isChecked()}\n")
            f.write(f"{self.c5.isChecked()}\n")
            f.write(f"{self.c6.isChecked()}")

    def open_awc(self):
        os.startfile(f"{abs_path}\\wheel_window.pyw")
        self.save_settings(self)

    def open_crmod(self):
        os.startfile(f"{abs_path}\\crmod_window.pyw")
        self.save_settings(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qtmodern.styles.light(app)
    ui.load_settings()
    MainWindow.show()
    sys.exit(app.exec_())
