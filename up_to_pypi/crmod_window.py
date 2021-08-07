import os
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from components.crmod_ui import Ui_CRModWindow
import utils


class CRModWindow(QMainWindow):
    def __init__(self):
        super(CRModWindow, self).__init__()
        self.ui = Ui_CRModWindow()
        self.ui.setupUi(self)
        self.make_connections(self)

    def resource_path(self, path):
        return utils.platform_path(os.path.join(self.cwd, path))

    def make_connections(self, CRModWindow):
        # some variables
        self.cl_folder = ""
        self.cwd = utils.cwd_of_script(__file__)
        # setting fixed crmod window size
        CRModWindow.setFixedSize(300, 200)
        # setting up icon for crmod window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("images/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CRModWindow.setWindowIcon(icon)
        # mapping all buttons
        self.ui.choose_location.clicked.connect(self.cl_popup)
        self.ui.build_files.clicked.connect(self.run_build_files)

    @utils.traceback_catch
    def cl_popup(self):
        self.cl_folder = utils.platform_path(QtWidgets.QFileDialog.getExistingDirectory())
        if self.cl_folder != "":
            self.ui.build_files.setEnabled(True)

    @utils.traceback_catch
    def run_build_files(self):
        os.chdir(self.cl_folder)
        module_structure = f"{self.ui.module_name.text()}/{self.ui.module_name.text()}"
        os.makedirs(module_structure)

        with open (utils.platform_path(os.path.join(module_structure, "__init__.py")), "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/init_template.txt")) as f2:
                f.write(f2.read())
                
        with open (utils.platform_path(os.path.join(module_structure, "__main__.py")), "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/main_template.txt")) as f2:
                f.write(f2.read())

        with open (f"{self.ui.module_name.text()}/setup.py", "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/setup_template.txt")) as f2:
                f.write(f2.read()
                        .replace("{self.ui.module_name.text()}", self.ui.module_name.text())
                        .replace("{self.ui.module_version.text()}", self.ui.module_version.text())
                        .replace("{self.ui.description.text()}", self.ui.description.text())
                        .replace("{self.ui.repo_url.text()}", self.ui.repo_url.text())
                        .replace("{self.ui.author.text()}", self.ui.author.text())
                        .replace("{self.ui.author_email.text()}", self.ui.author_email.text())
                )

        with open (f"{self.ui.module_name.text()}/README.md", "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/readme_template.txt")) as f2:
                f.write(f2.read()
                        .replace("{self.ui.module_name.text()}", self.ui.module_name.text())
                        .replace("{self.ui.description.text()}", self.ui.description.text())
                        .replace("{self.ui.author.text()}", self.ui.author.text())
                        .replace("{self.ui.module_name.text()}", self.ui.module_name.text())
                )

        with open (f"{self.ui.module_name.text()}/LICENSE", "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/license_template.txt")) as f2:
                f.write(f2.read()
                        .replace("{self.ui.author.text()}", self.ui.author.text())
                )

        with open (f"{self.ui.module_name.text()}/.gitignore", "w", encoding="utf-8") as f:
            with open(self.resource_path("templates/gitignore_template.txt")) as f2:
                f.write(f2.read())

        os.chdir(self.cwd)

        msg = QMessageBox()
        msg.setWindowTitle("About Module Creator")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Files Created Successfully")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = CRModWindow()
    window.show()

    sys.exit(app.exec_())
