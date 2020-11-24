from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from pyqt5_material import apply_stylesheet

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QProcess, QTextCodec
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextBrowser

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

class MyConsole(QTextBrowser):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.show_hide = QtWidgets.QPushButton(self.centralwidget)
        self.show_hide.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_hide.setIcon(icon1)
        self.show_hide.setObjectName("show_hide")
        self.gridLayout.addWidget(self.show_hide, 3, 1, 1, 1)
        self.commands = QtWidgets.QLabel(self.centralwidget)
        self.commands.setObjectName("commands")
        self.gridLayout.addWidget(self.commands, 12, 0, 1, 1)
        self.commands_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.commands_box.setObjectName("commands_box")
        self.gridLayout.addWidget(self.commands_box, 13, 0, 1, 2)
        self.output_box = MyConsole(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 15, 0, 1, 2)
        self.settings = QtWidgets.QLabel(self.centralwidget)
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
        self.gridLayout.addWidget(self.output, 14, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setChecked(True)
        self.c1.setObjectName("c1")
        self.gridLayout_2.addWidget(self.c1, 0, 0, 1, 1)
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setStatusTip("")
        self.c3.setWhatsThis("")
        self.c3.setChecked(True)
        self.c3.setObjectName("c3")
        self.gridLayout_2.addWidget(self.c3, 1, 0, 1, 1)
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setStatusTip("")
        self.c2.setObjectName("c2")
        self.gridLayout_2.addWidget(self.c2, 0, 1, 1, 1)
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setObjectName("c5")
        self.gridLayout_2.addWidget(self.c5, 2, 0, 1, 1)
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setStatusTip("")
        self.c6.setObjectName("c6")
        self.gridLayout_2.addWidget(self.c6, 2, 1, 1, 1)
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setObjectName("c4")
        self.gridLayout_2.addWidget(self.c4, 1, 1, 1, 1)
        self.opf = QtWidgets.QPushButton(self.centralwidget)
        self.opf.setObjectName("opf")
        self.gridLayout_2.addWidget(self.opf, 3, 0, 1, 1)
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setIcon(icon)
        self.upload.setObjectName("upload")
        self.gridLayout_2.addWidget(self.upload, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 248, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.show_hide.clicked.connect(self.show_hide_password)
        self.opf.clicked.connect(self.opf_popup)
        self.upload.clicked.connect(self.getting_command)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Up To PyPi"))
        self.commands.setText(_translate("MainWindow", "Commands Going To Execute :-"))
        self.commands_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>"))
        self.output_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">View In Terminal</p></body></html>"))       
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
        self.upload.setText(_translate("MainWindow", "Upload"))

    def show_hide_password(self):
        global count_password_switch
        if count_password_switch%2==0:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.show_hide.setIcon(icon)
            count_password_switch += 1
            self.pypi_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/hide.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

    def getting_command(self):
        with open ("commands.sh", "w", encoding="utf-8") as f:
            with open ("commands.txt", "w", encoding="utf-8") as f2:
                f.write(f"cd {opf_folder_location}\n")
                if self.c4.isChecked():
                    f.write("pip install --upgrade setuptools wheel\n")
                    f2.write("pip install --upgrade setuptools wheel\n")
                if self.c5.isChecked():
                    f.write("pip install twine\n")
                    f2.write("pip install twine\n")
                if self.c6.isChecked():
                    f.write("pip install --upgrade twine\n")
                    f2.write("pip install --upgrade twine\n")
                if self.c3.isChecked():
                    f.write("python setup.py sdist bdist_wheel\n")
                    f2.write("python setup.py sdist bdist_wheel\n")
                if self.c1.isChecked():
                    f.write(f"twine upload dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
                    f2.write(f"twine upload dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
                if self.c2.isChecked():
                    f.write(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n")
                    f2.write(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {self.pypi_username.text()} -p {self.pypi_password.text()}\n") 
                f.write('echo "========"\n'
                    'echo "FINISHED"\n'
                    'echo "========"\n')
    
        with open ("commands.txt", encoding="utf-8") as f:
            readings = f.read()
            _translate = QtCore.QCoreApplication.translate
            self.commands_box.setText(_translate("MainWindow", readings))

        reader.produce_output.connect(self.output_box.append_output)
        os.chdir(abs_path)
        os.system('sh commands.sh')
        os.remove('commands.sh')
        os.remove('commands.txt')

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    apply_stylesheet(app, theme=f'{abs_path}/assets/darker_blue.xml') 
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()