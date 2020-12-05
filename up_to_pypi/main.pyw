from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
import qtmodern.styles
import qtmodern.windows

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
opf_folder_location = ""
abs_path = os.path.dirname(__file__)
reader = ProcessOutputReader()
theme_count = 0
# resize_window = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{abs_path}/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.show_hide = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{abs_path}/images/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_hide.setIcon(icon1)
        self.show_hide.setObjectName("show_hide")
        self.gridLayout.addWidget(self.show_hide, 3, 1, 1, 1)
        self.commands = QtWidgets.QLabel(self.centralwidget)
        self.commands.setObjectName("commands")
        self.gridLayout.addWidget(self.commands, 13, 0, 1, 1)
        self.commands_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.commands_box.setObjectName("commands_box")
        self.gridLayout.addWidget(self.commands_box, 14, 0, 1, 2)
        self.output_box = output_console(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 16, 0, 1, 2)
        self.settings = QtWidgets.QLabel(self.centralwidget)
        self.settings.setFont(QtGui.QFont("", 10))
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 4, 0, 1, 2)
        self.pypi_password = QtWidgets.QLineEdit(self.centralwidget)
        self.pypi_password.setText("")
        self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pypi_password.setObjectName("pypi_password")
        self.gridLayout.addWidget(self.pypi_password, 3, 0, 1, 1)
        self.details = QtWidgets.QLabel(self.centralwidget)
        self.details.setObjectName("details")
        self.gridLayout.addWidget(self.details, 1, 0, 1, 2)
        self.pypi_username = QtWidgets.QLineEdit(self.centralwidget)
        self.pypi_username.setObjectName("pypi_username")
        self.gridLayout.addWidget(self.pypi_username, 2, 0, 1, 2)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 15, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setObjectName("c1")
        self.gridLayout_2.addWidget(self.c1, 0, 0, 1, 1)
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setObjectName("c3")
        self.gridLayout_2.addWidget(self.c3, 1, 0, 1, 1)
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setObjectName("c2")
        self.gridLayout_2.addWidget(self.c2, 0, 1, 1, 1)
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setObjectName("c5")
        self.gridLayout_2.addWidget(self.c5, 2, 0, 1, 1)
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setObjectName("c6")
        self.gridLayout_2.addWidget(self.c6, 2, 1, 1, 1)
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setObjectName("c4")
        self.gridLayout_2.addWidget(self.c4, 1, 1, 1, 1)
        self.opf = QtWidgets.QPushButton(self.centralwidget)
        self.opf.setObjectName("opf")
        self.gridLayout_2.addWidget(self.opf, 3, 0, 1, 1)
        self.abort = QtWidgets.QPushButton(self.centralwidget)
        self.abort.setObjectName("abort")
        self.gridLayout_2.addWidget(self.abort, 3, 1, 1, 1)
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setIcon(icon)
        self.upload.setObjectName("upload")
        self.gridLayout.addWidget(self.upload, 12, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 248, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuThemes = QtWidgets.QMenu(self.menuSettings)
        self.menuThemes.setObjectName("menuThemes")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(True)
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
        self.actionSave_User.setObjectName("actionSave_User")
        self.actionClear_Text_Fields = QtWidgets.QAction(MainWindow)
        self.actionClear_Text_Fields.setObjectName("actionClear_Text_Fields")
        self.actionReset_To_Default = QtWidgets.QAction(MainWindow)
        self.actionReset_To_Default.setObjectName("actionReset_To_Default")
        self.actionSave_PyPi_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_PyPi_Settings.setCheckable(True)
        self.actionSave_PyPi_Settings.setObjectName("actionSave_PyPi_Settings")
        self.menuOpen.addAction(self.actionOpen_Project_Folder)
        self.menuThemes.addSeparator()
        self.menuThemes.addAction(self.actionDark)
        self.menuThemes.addAction(self.actionLight)
        self.menuSettings.addAction(self.menuThemes.menuAction())
        self.menuSettings.addAction(self.actionSave_User)
        self.menuSettings.addAction(self.actionSave_PyPi_Settings)
        self.menuSettings.addAction(self.actionReset_To_Default)
        self.menuHelp.addAction(self.actionAbout_Up_To_PyPi)
        self.menuOptions.addAction(self.actionClear_Text_Fields)
        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.show_hide.clicked.connect(self.show_hide_password)
        self.opf.clicked.connect(self.opf_popup)
        self.abort.clicked.connect(self.abort_qprocess)
        self.upload.clicked.connect(self.getting_command)

        self.c1.stateChanged.connect(self.commands_box_view)
        self.c2.stateChanged.connect(self.commands_box_view)
        self.c3.stateChanged.connect(self.commands_box_view)
        self.c4.stateChanged.connect(self.commands_box_view)
        self.c5.stateChanged.connect(self.commands_box_view)
        self.c6.stateChanged.connect(self.commands_box_view)
        self.pypi_username.textEdited.connect(self.commands_box_view)
        self.pypi_password.textEdited.connect(self.commands_box_view)

        MainWindow.resizeEvent = self.resize_text
        MainWindow.closeEvent = self.save_settings

        self.actionOpen_Project_Folder.triggered.connect(lambda: self.opf_popup())
        self.actionLight.triggered.connect(lambda: self.light_theme())
        self.actionDark.triggered.connect(lambda: self.dark_theme())
        self.actionReset_To_Default.triggered.connect(lambda: self.Settings_Reset_To_Default())
        self.actionAbout_Up_To_PyPi.triggered.connect(lambda: self.about_uptopypi())

        self.actionClear_Text_Fields.triggered.connect(lambda: self.pypi_username.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.pypi_password.clear())

        # Moving Window To Center
        qr = MainWindow.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Up To PyPi"))
        self.commands.setText(_translate("MainWindow", "Commands Going To Execute :-"))
        self.commands_box.setText(_translate("MainWindow", "python setup.py sdist bdist_wheel\ntwine upload dist/* -u   -p  "))
        self.output_box.setText(_translate("MainWindow", "NULL"))   
        self.settings.setText(_translate("MainWindow", "Settings :-"))
        self.pypi_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.details.setText(_translate("MainWindow", "PyPI Details :-"))
        self.pypi_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.output.setText(_translate("MainWindow", "Output Terminal :-"))
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
        self.c4.setToolTip(_translate("MainWindow", "Upgrade setuptools to latest version"))
        self.c4.setText(_translate("MainWindow", "Upgrade Setuptools"))
        self.opf.setText(_translate("MainWindow", "Open Project Folder"))
        self.abort.setText(_translate("MainWindow", "Abort"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
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
        self.actionClear_Text_Fields.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionReset_To_Default.setText(_translate("MainWindow", "Reset To Default"))
        self.actionSave_PyPi_Settings.setText(_translate("MainWindow", "Save PyPi Settings"))

    def resize_text(self, event):
        # global resize_window

        # if resize_window == True:
        #     MainWindow.resize(340, 530)
        #     resize_window = False

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
        self.output.setFont(font_size_change2)

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

    def show_hide_password(self):
        global count_password_switch
        icon = QtGui.QIcon()
        if count_password_switch%2==0:
            icon.addPixmap(QtGui.QPixmap(f"{abs_path}/images/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.show_hide.setIcon(icon)
            count_password_switch += 1
            self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            icon.addPixmap(QtGui.QPixmap(f"{abs_path}/images/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        reader.kill()
        _translate = QtCore.QCoreApplication.translate
        self.output_box.append(_translate("MainWindow", "=============\nProcess Aborted\n============="))
        cursor = self.output_box.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.output_box.setTextCursor(cursor)

    def commands_box_view(self):
        with open (f"{abs_path}/commands.txt", "w", encoding="utf-8") as f:
            if self.c4.isChecked():
                f.write("pip install --upgrade setuptools wheel\n")
            if self.c5.isChecked():
                f.write("pip install twine\n")
            if self.c6.isChecked():
                f.write("pip install --upgrade twine\n")
            if self.c3.isChecked():
                f.write("python setup.py sdist bdist_wheel\n")
            if self.c1.isChecked():
                f.write(f"twine upload dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
            if self.c2.isChecked():
                f.write(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")

        if self.c4.isChecked() == False and self.c5.isChecked() == False and self.c6.isChecked() == False and self.c3.isChecked() == False and self.c1.isChecked() == False and self.c2.isChecked() == False:
            _translate = QtCore.QCoreApplication.translate
            self.commands_box.setText(_translate("MainWindow", "NULL"))

        else:
            with open (f"{abs_path}/commands.txt", encoding="utf-8") as f:
                readings = f.read()
                _translate = QtCore.QCoreApplication.translate
                self.commands_box.setText(_translate("MainWindow", readings))

    def getting_command(self):
        with open (f"{abs_path}/commands.bat", "w", encoding="utf-8") as f:
            f.write(f'cd /d "{opf_folder_location}"\n')
            if self.c4.isChecked():
                f.write("pip install --upgrade setuptools wheel\n")
            if self.c5.isChecked():
                f.write("pip install twine\n")
            if self.c6.isChecked():
                f.write("pip install --upgrade twine\n")
            if self.c3.isChecked():
                f.write("python setup.py sdist bdist_wheel\n")
            if self.c1.isChecked():
                f.write(f"twine upload dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
            if self.c2.isChecked():
                f.write(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
            f.write("echo off\n"
                "echo =======\n"
                "echo FINISHED\n"
                "echo =======\n")

        os.chdir(abs_path)
        self.output_box = output_console(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 16, 0, 1, 2)
        reader.produce_output.connect(self.output_box.append_output)
        reader.start('commands.bat')

    def light_theme(self):
        qtmodern.styles.light(app)
        self.actionDark.setChecked(False)
        self.actionLight.setChecked(True)

    def dark_theme(self):
        qtmodern.styles.dark(app)
        self.actionLight.setChecked(False)
        self.actionDark.setChecked(True)

    def Settings_Reset_To_Default(self):
        qtmodern.styles.dark(app)
        self.actionLight.setChecked(False)
        self.actionDark.setChecked(True)
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
        self.commands_box_view()
        _translate = QtCore.QCoreApplication.translate
        self.output_box.setText(_translate("MainWindow", "NULL")) 

    def about_uptopypi(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Up To PyPi")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Up To PyPi v1.0.9")
        msg.setInformativeText("Developed By 360modder")
        # msg.setDetailedText("Build With Python & PyQt5")
        msg = qtmodern.windows.ModernWindow(msg)
        msg.resize(100, 100)

        qr = msg.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        msg.move(qr.topLeft())

        msg.show()

    def open_settings(self):
        with open (f"{abs_path}/assets/settings.txt", encoding="utf-8") as f:
            read = f.read()
            read = read.split("@**@")

            if read[0] == 'False':
                self.light_theme()
            else:
                self.dark_theme()

            if read[1] == 'True':
                self.actionSave_User.setChecked(True)
                self.pypi_username.setText(read[3])
                self.pypi_password.setText(read[4])
            else:
                self.actionSave_User.setChecked(False)

            if read[2] == 'True':
                self.actionSave_PyPi_Settings.setChecked(True)
                if read[5] == 'True':
                    self.c1.setChecked(True)
                if read[6] == 'True':
                    self.c2.setChecked(True)
                if read[7] == 'True':
                    self.c3.setChecked(True)
                if read[8] == 'True':
                    self.c4.setChecked(True)
                if read[9] == 'True':
                    self.c5.setChecked(True)
                if read[10] == 'True':
                    self.c6.setChecked(True)
            else:
                self.actionSave_PyPi_Settings.setChecked(False)


    def save_settings(self, event):
        with open (f"{abs_path}/assets/settings.txt", "w", encoding="utf-8") as f:
            f.write(f"{self.actionDark.isChecked()}@**@")
            f.write(f"{self.actionSave_User.isChecked()}@**@")
            f.write(f"{self.actionSave_PyPi_Settings.isChecked()}@**@")
            f.write(f"{self.pypi_username.text()}@**@")
            f.write(f"{self.pypi_password.text()}@**@")
            f.write(f"{self.c1.isChecked()}@**@")
            f.write(f"{self.c2.isChecked()}@**@")
            f.write(f"{self.c3.isChecked()}@**@")
            f.write(f"{self.c4.isChecked()}@**@")
            f.write(f"{self.c5.isChecked()}@**@")
            f.write(f"{self.c6.isChecked()}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(MainWindow)
    # mw.resize(340, 530)
    ui.open_settings()
    mw.show()
    sys.exit(app.exec_())
