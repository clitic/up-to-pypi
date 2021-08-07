import os
import sys
import json
import webbrowser
import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from components.main_ui import Ui_MainWindow
from wheel_window import WheelWindow
from crmod_window import CRModWindow
import utils


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.make_connections(self)
        self.load_settings()

    def resource_path(self, path):
        return utils.platform_path(os.path.join(self.cwd, path))

    def make_connections(self, MainWindow):
        # some variables
        self.count_password_switch = 0
        self.opf_folder_location = ""
        self.cwd = utils.cwd_of_script(__file__)
        # resizing main window
        MainWindow.resize(600, 500)
        # moving main window to center
        qr = QtCore.QRect(0, 0, 600, 500)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        # setting up icon for main window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("images/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # setting up icon for password echo button
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("images/hide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.show_hide.setIcon(icon1)
        # mapping buttons
        self.ui.show_hide.clicked.connect(self.show_hide_password)
        self.ui.opf.clicked.connect(self.opf_popup)
        self.ui.abort.clicked.connect(self.abort_qthread)
        self.ui.upload.clicked.connect(self.upload_module)
        # mapping menu items
        self.ui.actionOpen_Project_Folder.triggered.connect(lambda: self.opf_popup())
        self.ui.actionNew_Module.triggered.connect(lambda: CRModWindowObj.show())
        self.ui.actionUpload.triggered.connect(lambda: self.upload_module())
        self.ui.actionAbort.triggered.connect(lambda: self.abort_qthread())  
        self.ui.actionClear_Text_Fields.triggered.connect(lambda: self.ui.pypi_username.clear())
        self.ui.actionClear_Text_Fields.triggered.connect(lambda: self.ui.pypi_password.clear())
        self.ui.actionAdvance_Wheel_Creator.triggered.connect(lambda: WheelWindowObj.show())
        self.ui.actionLight.triggered.connect(lambda: self.light_theme())
        self.ui.actionDark.triggered.connect(lambda: self.dark_theme())
        self.ui.actionReset_To_Default.triggered.connect(lambda: self.reset_settings())
        self.ui.actionReport_A_Bug.triggered.connect(lambda: webbrowser.open("https://github.com/360modder/up-to-pypi/issues", new=2))
        self.ui.actionAbout_Up_To_PyPi.triggered.connect(lambda: self.about_uptopypi())
        self.ui.actionAbout_Qt.triggered.connect(lambda _: QApplication.aboutQt())
        # mapping main window events
        MainWindow.resizeEvent = self.resize_text
        MainWindow.closeEvent = self.save_settings
        self.ui.c1.stateChanged.connect(self.preview_commands)
        self.ui.c2.stateChanged.connect(self.preview_commands)
        self.ui.c3.stateChanged.connect(self.preview_commands)
        self.ui.c4.stateChanged.connect(self.preview_commands)
        self.ui.pypi_username.textEdited.connect(self.preview_commands)
        self.ui.pypi_password.textEdited.connect(self.preview_commands)
        # pre gui overrides
        self.preview_commands()

    def all_commands(self, hidepass=True):
        commands = []
        username = self.ui.pypi_username.text()
        password = len(self.ui.pypi_password.text()) * "*" if hidepass else self.ui.pypi_password.text()
        python_command = "python" if utils.is_windows else "python3"
        pip_command = "pip" if utils.is_windows else "pip3"

        commands.append(f'cd{" /d " if utils.is_windows else " "}"{self.opf_folder_location}"')
        if self.ui.c4.isChecked():
            commands.append(f"{pip_command} install setuptools wheel twine --upgrade")
        if self.ui.c3.isChecked():
            commands.append(f"{python_command} setup.py sdist bdist_wheel")
        if self.ui.c1.isChecked():
            commands.append(f"twine upload dist/* -u {username} -p {password}")
        if self.ui.c2.isChecked():
            commands.append(f"twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u {username} -p {password}")
        return commands

    def preview_commands(self):
        self.ui.commands_box.setText("\n".join(self.all_commands()) if self.all_commands() != [] else "")
        self.ui.commands.setText("Commands Going To Execute :-")

    def subprocess_output(self, subprocess_output):
        cursor = self.ui.commands_box.textCursor()
        self.ui.commands_box.append(subprocess_output)
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.movePosition(QtGui.QTextCursor.Up if cursor.atBlockStart() else QtGui.QTextCursor.StartOfLine)
        self.ui.commands_box.setTextCursor(cursor)

    def abort_qthread(self):
        self.subprocess_worker.stop()
        self.ui.abort.setDisabled(True)

    def upload_module(self):
        # pre confirmation
        command = " && ".join(self.all_commands(hidepass=False))
        msg = QMessageBox()
        question_response = msg.question(self, "Confirmation Prompt", f"Do you really want to execute the below command ?\n\n{command}", QMessageBox.Yes | QMessageBox.No)

        if question_response == QMessageBox.Yes:
            # pre gui overrides
            self.ui.commands_box.clear()
            self.setStatusTip(f"Running Command {command}")
            # intializing worker thread
            self.worker_thread = QThread()
            self.subprocess_worker = utils.SubprocessWorker(command)
            self.subprocess_worker.moveToThread(self.worker_thread)
            # connecting slots and signals
            self.worker_thread.started.connect(self.subprocess_worker.run)
            self.subprocess_worker.finished.connect(self.worker_thread.quit)
            self.subprocess_worker.finished.connect(self.subprocess_worker.deleteLater)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)
            self.subprocess_worker.progress.connect(self.subprocess_output)
            # starting thread
            self.worker_thread.start()
            # post gui overrides
            self.ui.commands.setText("Output Terminal (In Progress) :-")
            self.ui.upload.setDisabled(True)
            self.ui.abort.setEnabled(True)
            self.worker_thread.finished.connect(lambda: self.ui.upload.setEnabled(True))
            self.worker_thread.finished.connect(lambda: self.ui.abort.setDisabled(True))
            self.worker_thread.finished.connect(lambda: self.ui.commands.setText("Output Terminal (Finished) :-"))
            self.worker_thread.finished.connect(lambda: self.ui.commands_box.append(f"Finished Executing {command}"))
            self.worker_thread.finished.connect(lambda: self.setStatusTip(f"Finished Executing {command}"))
        
    @utils.traceback_catch
    def opf_popup(self):
        self.opf_folder_location = utils.platform_path(QtWidgets.QFileDialog.getExistingDirectory())
        self.setStatusTip(f"Project Folder Path {self.opf_folder_location}")
        self.preview_commands()
        if self.opf_folder_location != "":
            self.ui.upload.setEnabled(True)

    def about_uptopypi(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Up To PyPi")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Up To PyPi v2.1.4")
        msg.setInformativeText("Developed By 360modder")
        msg.setDetailedText("Build With Python & PyQt5")
        msg.exec_()

    def show_hide_password(self):
        icon = QtGui.QIcon()

        if self.count_password_switch % 2 == 0:
            icon.addPixmap(QtGui.QPixmap(self.resource_path("images/show.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pypi_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            icon.addPixmap(QtGui.QPixmap(self.resource_path("images/hide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.pypi_password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.ui.show_hide.setIcon(icon)
        self.count_password_switch += 1

    def resize_text(self, event):
        default_size = 11
        width = self.frameGeometry().width()

        if width // 100 > default_size:
            font_size_change = QtGui.QFont("Roboto", width // 100)
            font_size_change2 = QtGui.QFont("Roboto", width // 100)
        else:
            font_size_change = QtGui.QFont("Roboto", default_size)
            font_size_change2 = QtGui.QFont()

        # text browser
        self.ui.commands_box.setFont(font_size_change)
        # text fields
        self.ui.pypi_username.setFont(font_size_change)
        self.ui.pypi_password.setFont(font_size_change)
        # labels
        self.ui.settings.setFont(font_size_change2)
        self.ui.details.setFont(font_size_change2)
        self.ui.commands.setFont(font_size_change2)
        # image buttons
        self.ui.show_hide.setFont(font_size_change2)
        self.ui.opf.setFont(font_size_change2)
        self.ui.abort.setFont(font_size_change2)
        self.ui.upload.setFont(font_size_change2)
        # checkboxes
        self.ui.c1.setFont(font_size_change)
        self.ui.c2.setFont(font_size_change)
        self.ui.c3.setFont(font_size_change)
        self.ui.c4.setFont(font_size_change)

    def light_theme(self):
        qtmodern.styles.light(app)
        self.ui.actionDark.setChecked(False)
        self.ui.actionLight.setChecked(True)
        self.save_settings(self)
        self.resize_text("")

    def dark_theme(self):
        qtmodern.styles.dark(app)
        self.ui.actionLight.setChecked(False)
        self.ui.actionDark.setChecked(True)
        self.save_settings(self)
        self.resize_text("")

    def save_settings(self, event):
        settings = {
            "actionLight": self.ui.actionLight.isChecked(),
            "pypi_username": self.ui.pypi_username.text(),
            "pypi_password": self.ui.pypi_password.text(),
            "c1": self.ui.c1.isChecked(),
            "c2": self.ui.c2.isChecked(),
            "c3": self.ui.c3.isChecked(),
            "c4": self.ui.c4.isChecked(),
        }

        with open(self.resource_path("settings/settings-user.json"), "w") as f:
            json.dump(settings, f, indent=4, sort_keys=True)

    def load_settings(self):
        def checkbox_ticker(checkbox, jsonkey, settings):
            if settings[jsonkey]:
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)

        with open(self.resource_path("settings/settings-user.json")) as f:
            settings = json.load(f)

        checkboxes = {
            "actionLight": self.ui.actionLight,
            "c1": self.ui.c1,
            "c2": self.ui.c2,
            "c3": self.ui.c3,
            "c4": self.ui.c4,
        }

        for jsonkey, box in checkboxes.items():
            checkbox_ticker(box, jsonkey, settings)

        self.ui.pypi_username.setText(settings["pypi_username"])
        self.ui.pypi_password.setText(settings["pypi_password"])
        self.light_theme() if settings["actionLight"] else self.dark_theme()

    def reset_settings(self):
        with open(self.resource_path("settings/settings-default.json")) as settings:
            with open(self.resource_path("settings/settings-user.json"), "w") as f:
                f.write(settings.read())

        self.load_settings()
        self.preview_commands()
        self.setStatusTip("Settings Resetted To Default")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qtmodern.styles.light(app)
    
    window = MainWindow()
    WheelWindowObj = WheelWindow()
    CRModWindowObj = CRModWindow()
    # window = qtmodern.windows.ModernWindow(window)
    # WheelWindowObj = qtmodern.windows.ModernWindow(WheelWindowObj())

    window.show()
    sys.exit(app.exec_())
