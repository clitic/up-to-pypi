import os
import sys
import json
import glob
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from .components.wheel_ui import Ui_WheelWindow
from . import utils


class WheelWindow(QMainWindow):
    def __init__(self):
        super(WheelWindow, self).__init__()
        self.ui = Ui_WheelWindow()
        self.ui.setupUi(self)
        self.make_connections(self)
        self.load_settings()

    def resource_path(self, path):
        return utils.platform_path(os.path.join(self.cwd, path))

    def make_connections(self, WheelWindow):
        # some variables
        self.opf_folder_location = ""
        self.cwd = utils.cwd_of_script(__file__)
        # resizing wheel window
        WheelWindow.resize(600, 600)
        # moving wheel window to center
        qr = QtCore.QRect(0, 0, 600, 600)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        WheelWindow.move(qr.topLeft())
        # setting up icon for main window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("images/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WheelWindow.setWindowIcon(icon)
        # mapping buttons
        self.ui.create_wheel.clicked.connect(self.build_wheel)
        self.ui.open_setup.clicked.connect(self.opf_popup)
        self.ui.abort.clicked.connect(self.abort_qthread)
        # mapping menu items
        self.ui.actionCreate_Wheel.triggered.connect(lambda: self.build_wheel())
        self.ui.actionOpen_Project_Folder.triggered.connect(lambda: self.opf_popup())
        self.ui.actionAdvance_Wheel_Creator.triggered.connect(lambda: self.about_awc())
        self.ui.actionReset_To_Default.triggered.connect(lambda: self.reset_settings())
        self.ui.actionAbort.triggered.connect(lambda: self.abort_qthread())
        # mapping wheel window events
        WheelWindow.resizeEvent = self.resize_text
        WheelWindow.closeEvent = self.save_settings
        self.ui.c1.stateChanged.connect(self.preview_commands)
        self.ui.c2.stateChanged.connect(self.preview_commands)
        self.ui.c3.stateChanged.connect(self.preview_commands)
        self.ui.c5.stateChanged.connect(self.preview_commands)
        self.ui.c6.stateChanged.connect(self.preview_commands)
        self.ui.c7.stateChanged.connect(self.preview_commands)
        self.ui.c8.stateChanged.connect(self.preview_commands)
        self.ui.c10.stateChanged.connect(self.preview_commands)
        self.ui.c11.stateChanged.connect(self.preview_commands)
        self.ui.c12.stateChanged.connect(self.preview_commands)
        self.ui.c13.stateChanged.connect(self.preview_commands)
        self.ui.c15.stateChanged.connect(self.preview_commands)
        self.ui.c16.stateChanged.connect(self.preview_commands)
        self.ui.c17.stateChanged.connect(self.preview_commands)
        self.ui.c18.stateChanged.connect(self.preview_commands)
        self.ui.c19.stateChanged.connect(self.preview_commands)
        self.ui.c20.stateChanged.connect(self.preview_commands)
        self.ui.cu1.stateChanged.connect(self.preview_commands)
        self.ui.cu2.stateChanged.connect(self.preview_commands)
        self.ui.cu3.stateChanged.connect(self.preview_commands)
        self.ui.cu1val.textEdited.connect(self.preview_commands)
        self.ui.cu2val.textEdited.connect(self.preview_commands)
        self.ui.cu3val.textEdited.connect(self.preview_commands)
        # pre gui overrides
        self.preview_commands()

    def command_merge(self, apis, buildno, platform):
        command = [
            "python" if utils.is_windows else "python3",
            'setup.py',
            'sdist',
            'bdist_wheel',
        ]

        if apis != "":
            command.append(apis)
        if buildno != "":
            command.append(buildno)
        if platform != "":
            command.append(platform)
        return " ".join(command)

    def all_commands(self):
        commands = [
            f'cd{" /d " if utils.is_windows else " "}"{self.opf_folder_location}"'
        ]

        buildno = f"--build-number {self.ui.cu3val.text()}" if self.ui.cu3.isChecked() else ""

        if self.ui.cu2.isChecked():
            apis = f"--py-limited-api {self.ui.cu2val.text()} --python-tag {self.ui.cu2val.text()}"
        else:
            apis = self._extracted_from_all_commands_9()
        if self.ui.cu1.isChecked():
            commands.append(self.command_merge(apis, buildno, f"--plat-name {self.ui.cu1val.text()}"))
        if self.ui.c5.isChecked():
            commands.append(self.command_merge(apis, buildno, "--universal"))
        if self.ui.c1.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux2014_x86_64"))
        if self.ui.c6.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux2014_aarch64"))
        if self.ui.c11.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux2010_i686"))
        if self.ui.c15.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux2010_x86_64"))
        if self.ui.c18.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux1_i686"))
        if self.ui.c20.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name manylinux1_x86_64"))
        if self.ui.c2.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name win_amd64"))
        if self.ui.c7.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name win32"))
        if self.ui.c12.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name macosx_10_13_intel"))
        if self.ui.c16.isChecked():
            commands.append(self.command_merge(apis, buildno, "--plat-name macosx_10_9_x86_64"))

        return commands

    # TODO Rename this here and in `all_commands`
    def _extracted_from_all_commands_9(self):
        all_api = []
        if self.ui.c3.isChecked():
            all_api.append("cp39")
        if self.ui.c8.isChecked():
            all_api.append("cp38")
        if self.ui.c13.isChecked():
            all_api.append("cp37")
        if self.ui.c17.isChecked():
            all_api.append("cp36")
        if self.ui.c19.isChecked():
            all_api.append("cp27")
        all_api = ".".join(all_api)
        return (
            ""
            if len(all_api) == 0
            else f"--py-limited-api {all_api} --python-tag {all_api}"
        )
        
    def post_commands(self):
        self.setStatusTip("Running Post Commands")

        try:
            for folder in os.listdir(self.opf_folder_location):
                if self.ui.c10.isChecked() and (
                    "build" in folder or "egg-info" in folder
                ):
                    shutil.rmtree(utils.platform_path(os.path.join(self.opf_folder_location, folder)))

            for whl in glob.glob(utils.platform_path(os.path.join(self.opf_folder_location, "dist/*.whl"))):
                if self.ui.c14.isChecked():
                    break
                if self.ui.c4.isChecked():
                    tag = "-abi3"
                if self.ui.c9.isChecked():
                    tag = "-cp33m"
                if not os.path.exists(utils.platform_path(os.path.join(whl, whl.replace("-none", tag)))):
                    os.rename(whl, whl.replace("-none", tag))

        except Exception as e:
            print(e.__str__())

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

    def build_wheel(self):
        # pre confirmation
        command = " && ".join(self.all_commands())
        msg = QMessageBox()
        question_response = msg.question(self, "Confirmation Prompt", f"Do you really want to execute the below command ?\n\n{command}", QMessageBox.Yes | QMessageBox.No)

        if question_response == QMessageBox.Yes:
            # clean dist
            try:
                if self.ui.c21.isChecked() and os.path.exists(utils.platform_path(os.path.join(self.opf_folder_location, "dist"))):
                    shutil.rmtree(utils.platform_path(os.path.join(self.opf_folder_location, "dist")))
            except Exception as e:
                print(e.__str__())
                
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
            self.worker_thread.finished.connect(self.post_commands)
            self.subprocess_worker.progress.connect(self.subprocess_output)
            # starting thread
            self.worker_thread.start()
            # post gui overrides
            self.ui.commands.setText("Output Terminal (In Progress) :-")
            self.ui.create_wheel.setDisabled(True)
            self.ui.abort.setEnabled(True)
            self.worker_thread.finished.connect(lambda: self.ui.create_wheel.setEnabled(True))
            self.worker_thread.finished.connect(lambda: self.ui.abort.setDisabled(True))
            self.worker_thread.finished.connect(lambda: self.ui.commands.setText("Output Terminal (Finished) :-"))
            self.worker_thread.finished.connect(lambda: self.ui.commands_box.append(f"Finished Executing {command}"))
            self.worker_thread.finished.connect(lambda: self.setStatusTip(f"Finished Executing {command}"))

    def about_awc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Advance Wheel Creator")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Advance Wheel Creator v0.1.0")
        msg.setInformativeText("Developed By clitic")
        msg.exec_()

    @utils.traceback_catch
    def opf_popup(self):
        self.opf_folder_location = utils.platform_path(QtWidgets.QFileDialog.getExistingDirectory())
        self.setStatusTip(f"Project Folder Path {self.opf_folder_location}")
        self.preview_commands()
        if self.opf_folder_location != "":
            self.ui.create_wheel.setEnabled(True)

    def resize_text(self, event):
        default_size = 11
        width = self.frameGeometry().width()

        if width // 100> default_size:
            font_size_change = QtGui.QFont("Roboto", width // 100)
            font_size_change2 = QtGui.QFont("Roboto", width // 100)
        else:
            font_size_change = QtGui.QFont("Roboto", default_size)
            font_size_change2 = QtGui.QFont()

        # text browser
        self.ui.commands_box.setFont(font_size_change)
        # text fields
        self.ui.cu1val.setFont(font_size_change)
        self.ui.cu2val.setFont(font_size_change)
        self.ui.cu3val.setFont(font_size_change)
        # labels
        self.ui.l1.setFont(font_size_change2)
        self.ui.l2.setFont(font_size_change2)
        self.ui.l3.setFont(font_size_change2)
        self.ui.l4.setFont(font_size_change2)
        self.ui.l5.setFont(font_size_change2)
        self.ui.commands.setFont(font_size_change2)
        # image buttons
        self.ui.open_setup.setFont(font_size_change2)
        self.ui.abort.setFont(font_size_change2)
        self.ui.create_wheel.setFont(font_size_change2)
        # checkboxes
        self.ui.c1.setFont(font_size_change)
        self.ui.c2.setFont(font_size_change)
        self.ui.c3.setFont(font_size_change)
        self.ui.c4.setFont(font_size_change)
        self.ui.c5.setFont(font_size_change)
        self.ui.c6.setFont(font_size_change)
        self.ui.c7.setFont(font_size_change)
        self.ui.c8.setFont(font_size_change)
        self.ui.c9.setFont(font_size_change)
        self.ui.c10.setFont(font_size_change)
        self.ui.c11.setFont(font_size_change)
        self.ui.c12.setFont(font_size_change)
        self.ui.c13.setFont(font_size_change)
        self.ui.c14.setFont(font_size_change)
        self.ui.c15.setFont(font_size_change)
        self.ui.c16.setFont(font_size_change)
        self.ui.c17.setFont(font_size_change)
        self.ui.c18.setFont(font_size_change)
        self.ui.c19.setFont(font_size_change)
        self.ui.c20.setFont(font_size_change)
        self.ui.c21.setFont(font_size_change)
        self.ui.cu1.setFont(font_size_change)
        self.ui.cu2.setFont(font_size_change)
        self.ui.cu3.setFont(font_size_change)
        
    def save_settings(self, event):
        settings = {
            "c1": self.ui.c1.isChecked(),
            "c2": self.ui.c2.isChecked(),
            "c3": self.ui.c3.isChecked(),
            "c4": self.ui.c4.isChecked(),
            "c5": self.ui.c5.isChecked(),
            "c6": self.ui.c6.isChecked(),
            "c7": self.ui.c7.isChecked(),
            "c8": self.ui.c8.isChecked(),
            "c9": self.ui.c9.isChecked(),
            "c10": self.ui.c10.isChecked(),
            "c11": self.ui.c11.isChecked(),
            "c12": self.ui.c12.isChecked(),
            "c13": self.ui.c13.isChecked(),
            "c14": self.ui.c14.isChecked(),
            "c15": self.ui.c15.isChecked(),
            "c16": self.ui.c16.isChecked(),
            "c17": self.ui.c17.isChecked(),
            "c18": self.ui.c18.isChecked(),
            "c19": self.ui.c19.isChecked(),
            "c20": self.ui.c20.isChecked(),
            "c21": self.ui.c21.isChecked(),
            "cu1": self.ui.cu1.isChecked(),
            "cu2": self.ui.cu2.isChecked(),
            "cu3": self.ui.cu3.isChecked(),
            "cu1val": self.ui.cu1val.text(),
            "cu2val": self.ui.cu2val.text(),
            "cu3val": self.ui.cu3val.text(),
        }

        with open(self.resource_path("settings/settings-wheel-user.json"), "w") as f:
            json.dump(settings, f, indent=4, sort_keys=True)

    def load_settings(self):
        def checkbox_ticker(checkbox, jsonkey, settings):
            if settings[jsonkey]:
                checkbox.setChecked(True)
            else:
                checkbox.setChecked(False)

        with open(self.resource_path("settings/settings-wheel-user.json")) as f:
            settings = json.load(f)

        checkboxes = {
            "c1": self.ui.c1,
            "c2": self.ui.c2,
            "c3": self.ui.c3,
            "c4": self.ui.c4,
            "c5": self.ui.c5,
            "c6": self.ui.c6,
            "c7": self.ui.c7,
            "c8": self.ui.c8,
            "c9": self.ui.c9,
            "c10": self.ui.c10,
            "c11": self.ui.c11,
            "c12": self.ui.c12,
            "c13": self.ui.c13,
            "c14": self.ui.c14,
            "c15": self.ui.c15,
            "c16": self.ui.c16,
            "c17": self.ui.c17,
            "c18": self.ui.c18,
            "c19": self.ui.c19,
            "c20": self.ui.c20,
            "c21": self.ui.c21,
            "cu1": self.ui.cu1,
            "cu2": self.ui.cu2,
            "cu3": self.ui.cu3,
        }

        for jsonkey, box in checkboxes.items():
            checkbox_ticker(box, jsonkey, settings)

        self.ui.cu1val.setText(settings["cu1val"])
        self.ui.cu2val.setText(settings["cu2val"])
        self.ui.cu3val.setText(settings["cu3val"])

    def reset_settings(self):
        with open(self.resource_path("settings/settings-wheel-default.json")) as settings:
            with open(self.resource_path("settings/settings-wheel-user.json"), "w") as f:
                f.write(settings.read())

        self.load_settings()
        self.preview_commands()
        self.setStatusTip("Settings Resetted To Default")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = WheelWindow()
    window.show()

    sys.exit(app.exec_())
