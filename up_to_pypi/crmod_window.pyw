from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import qtmodern.styles
import qtmodern.windows

# Globals
abs_path = os.path.dirname(__file__)
cl_folder_location = ""

class Ui_CRModWindow(object):
    def setupUi(self, CRModWindow):
        CRModWindow.setObjectName("CRModWindow")
        CRModWindow.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CRModWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CRModWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l2.sizePolicy().hasHeightForWidth())
        self.l2.setSizePolicy(sizePolicy)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 6, 0, 1, 2)
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setObjectName("c5")
        self.gridLayout.addWidget(self.c5, 12, 0, 1, 1)
        self.module_version = QtWidgets.QLineEdit(self.centralwidget)
        self.module_version.setObjectName("module_version")
        self.gridLayout.addWidget(self.module_version, 2, 1, 1, 1)
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setObjectName("c6")
        self.gridLayout.addWidget(self.c6, 12, 1, 1, 1)
        self.author = QtWidgets.QLineEdit(self.centralwidget)
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 5, 0, 1, 1)
        self.module_name = QtWidgets.QLineEdit(self.centralwidget)
        self.module_name.setObjectName("module_name")
        self.gridLayout.addWidget(self.module_name, 2, 0, 1, 1)
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setChecked(True)
        self.c2.setObjectName("c2")
        self.gridLayout.addWidget(self.c2, 8, 1, 1, 1)
        self.author_email = QtWidgets.QLineEdit(self.centralwidget)
        self.author_email.setObjectName("author_email")
        self.gridLayout.addWidget(self.author_email, 5, 1, 1, 1)
        self.description = QtWidgets.QLineEdit(self.centralwidget)
        self.description.setObjectName("description")
        self.gridLayout.addWidget(self.description, 4, 0, 1, 1)
        self.build_files = QtWidgets.QPushButton(self.centralwidget)
        self.build_files.setObjectName("build_files")
        self.gridLayout.addWidget(self.build_files, 15, 0, 1, 2)
        self.repo_url = QtWidgets.QLineEdit(self.centralwidget)
        self.repo_url.setObjectName("repo_url")
        self.gridLayout.addWidget(self.repo_url, 4, 1, 1, 1)
        self.choose_location = QtWidgets.QPushButton(self.centralwidget)
        self.choose_location.setObjectName("choose_location")
        self.gridLayout.addWidget(self.choose_location, 13, 0, 1, 2)
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setChecked(True)
        self.c3.setObjectName("c3")
        self.gridLayout.addWidget(self.c3, 9, 0, 1, 1)
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l3.sizePolicy().hasHeightForWidth())
        self.l3.setSizePolicy(sizePolicy)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 11, 0, 1, 2)
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setChecked(True)
        self.c4.setObjectName("c4")
        self.gridLayout.addWidget(self.c4, 9, 1, 1, 1)
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setChecked(True)
        self.c1.setObjectName("c1")
        self.gridLayout.addWidget(self.c1, 8, 0, 1, 1)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l1.sizePolicy().hasHeightForWidth())
        self.l1.setSizePolicy(sizePolicy)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 1, 0, 1, 2)
        CRModWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CRModWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        CRModWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CRModWindow)
        self.statusbar.setObjectName("statusbar")
        CRModWindow.setStatusBar(self.statusbar)
        self.actionChoose_Location = QtWidgets.QAction(CRModWindow)
        self.actionChoose_Location.setObjectName("actionChoose_Location")
        self.actionBuild_Files = QtWidgets.QAction(CRModWindow)
        self.actionBuild_Files.setObjectName("actionBuild_Files")
        self.actionClear_Text_Fields = QtWidgets.QAction(CRModWindow)
        self.actionClear_Text_Fields.setObjectName("actionClear_Text_Fields")
        self.actionAbout_Module_Creator = QtWidgets.QAction(CRModWindow)
        self.actionAbout_Module_Creator.setObjectName("actionAbout_Module_Creator")
        self.menuOptions.addAction(self.actionChoose_Location)
        self.menuOptions.addAction(self.actionBuild_Files)
        self.menuOptions.addAction(self.actionClear_Text_Fields)
        self.menuHelp.addAction(self.actionAbout_Module_Creator)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(CRModWindow)
        QtCore.QMetaObject.connectSlotsByName(CRModWindow)

        CRModWindow.resizeEvent = self.resize_text

        self.build_files.clicked.connect(self.run_build_files)
        self.choose_location.clicked.connect(self.cl_popup)

        self.actionBuild_Files.triggered.connect(lambda: self.run_build_files())
        self.actionChoose_Location.triggered.connect(lambda: self.cl_popup())
        self.actionAbout_Module_Creator.triggered.connect(lambda: self.about_crmod())

        self.actionClear_Text_Fields.triggered.connect(lambda: self.module_name.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.module_version.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.description.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.author.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.author_email.clear())
        self.actionClear_Text_Fields.triggered.connect(lambda: self.repo_url.clear())

    def retranslateUi(self, CRModWindow):
        _translate = QtCore.QCoreApplication.translate
        CRModWindow.setWindowTitle(_translate("CRModWindow", "Module Creater"))
        self.l2.setText(_translate("CRModWindow", "Files To Create (Recommended) :-"))
        self.c5.setText(_translate("CRModWindow", ".gitignore"))
        self.module_version.setPlaceholderText(_translate("CRModWindow", "Module Version"))
        self.c6.setText(_translate("CRModWindow", "MANIFEST.in"))
        self.author.setPlaceholderText(_translate("CRModWindow", "Author Name"))
        self.module_name.setPlaceholderText(_translate("CRModWindow", "Module Name"))
        self.c2.setText(_translate("CRModWindow", "__init__.py + __main__.py"))
        self.author_email.setPlaceholderText(_translate("CRModWindow", "Author Email"))
        self.description.setPlaceholderText(_translate("CRModWindow", "Small Description"))
        self.build_files.setText(_translate("CRModWindow", "Build Files"))
        self.repo_url.setPlaceholderText(_translate("CRModWindow", "URL"))
        self.choose_location.setText(_translate("CRModWindow", "Choose Location"))
        self.c3.setText(_translate("CRModWindow", "README.md"))
        self.l3.setText(_translate("CRModWindow", "Files To Create (Optional) :-"))
        self.c4.setText(_translate("CRModWindow", "LICENSE"))
        self.c1.setText(_translate("CRModWindow", "setup.py"))
        self.l1.setText(_translate("CRModWindow", "Please Fill Some Details :-"))
        self.menuOptions.setTitle(_translate("CRModWindow", "Options"))
        self.menuHelp.setTitle(_translate("CRModWindow", "Help"))
        self.actionChoose_Location.setText(_translate("CRModWindow", "Choose Location"))
        self.actionBuild_Files.setText(_translate("CRModWindow", "Build Files"))
        self.actionClear_Text_Fields.setText(_translate("CRModWindow", "Clear Text Fields"))
        self.actionAbout_Module_Creator.setText(_translate("CRModWindow", "About Module Creator"))

    def resize_text(self, event):
        default_size = 11
        width = CRModWindow.frameGeometry().width()

        if width // 100> default_size:
            font_size_change = QtGui.QFont('Roboto', width // 100)
            font_size_change2 = QtGui.QFont('Roboto', width // 100)
        else:
            font_size_change = QtGui.QFont('Roboto', default_size)
            font_size_change2 = QtGui.QFont()

        self.l1.setFont(font_size_change2)
        self.l2.setFont(font_size_change2)
        self.l3.setFont(font_size_change2)

        self.c1.setFont(font_size_change)
        self.c2.setFont(font_size_change)
        self.c3.setFont(font_size_change)
        self.c4.setFont(font_size_change)
        self.c5.setFont(font_size_change)
        self.c6.setFont(font_size_change)
        self.module_name.setFont(font_size_change)
        self.module_version.setFont(font_size_change)
        self.description.setFont(font_size_change)
        self.author.setFont(font_size_change)
        self.author_email.setFont(font_size_change)
        self.repo_url.setFont(font_size_change)

        self.choose_location.setFont(font_size_change2)
        self.build_files.setFont(font_size_change2)

    def cl_popup(self):
        global opf_folder_location
        cl_folder = QtWidgets.QFileDialog.getExistingDirectory()
        try:
          cl_folder_location = cl_folder.replace("/", "\\")
          os.chdir(cl_folder_location)
        except:
            pass

    def run_build_files(self):
        SetupC = f"""import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="{self.module_name.text()}",
    version="{self.module_version.text()}",
    description="{self.description.text()}",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=[],
    url="{self.repo_url.text()}",
    author="{self.author.text()}",
    author_email="{self.author_email.text()}",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["{self.module_name.text()}"],
    include_package_data=True,
    install_requires=[],
)
        """

        ReadmeC = f"""# {self.module_name.text()}

{self.description.text()}

## Installation

```pip install {self.module_name.text()}```

## License

© 2020 {self.author.text()}

This repository is licensed under the MIT license. See LICENSE for details.
        """

        LicenseC = f"""MIT License

Copyright (c) 2020 {self.author.text()}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
        """

        ManifestC = """"""

        GitIgnoreC = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
bin/
include/



# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

##my files
check.py
*.pdf
deletes/
sorted/
splits/
merged/
pyvenv.cfg
.DS_Store
"""

        try:
            os.makedirs(f"{self.module_name.text()}\\{self.module_name.text()}")
        except:
            pass
        
        if self.c1.isChecked():
            with open (f"{self.module_name.text()}\\setup.py", "w", encoding="utf-8") as f:
                f.write(SetupC)

        if self.c2.isChecked():
            with open (f"{self.module_name.text()}\\{self.module_name.text()}\\__init__.py", "w", encoding="utf-8") as f:
                f.write("from .__main__ import *\n")

            with open (f"{self.module_name.text()}\\{self.module_name.text()}\\__main__.py", "w", encoding="utf-8") as f:
                f.write("def main():\n\tprint('Hello World!')\n\n"
                    "if __name__ == '__main__':\n\tmain()\n")

        if self.c3.isChecked():
            with open (f"{self.module_name.text()}\\README.md", "w", encoding="utf-8") as f:
                f.write(ReadmeC)

        if self.c4.isChecked():
            with open (f"{self.module_name.text()}\\LICENSE", "w", encoding="utf-8") as f:
                f.write(LicenseC)

        if self.c5.isChecked():
            with open (f"{self.module_name.text()}\\.gitignore", "w", encoding="utf-8") as f:
                f.write(GitIgnoreC)

        if self.c6.isChecked():
            with open (f"{self.module_name.text()}\\MANIFEST.in", "w", encoding="utf-8") as f:
                f.write(ManifestC)

        msg = QMessageBox()
        msg.setWindowTitle("About Module Creator")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Files Created Successfully")
        msg.exec_()

    def about_crmod(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Module Creator")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Module Creator v1.0.0")
        msg.setInformativeText("Developed By 360modder")
        msg.exec_()

    def light_theme(self):
        qtmodern.styles.light(app)

    def dark_theme(self):
        qtmodern.styles.dark(app)

    def load_settings(self):
        with open (f"{abs_path}\\assets\\settings.txt", encoding="utf-8") as f:
            read = f.read()
            read = read.split("\n")
            if read[0] == 'True':
                self.light_theme()
            else:
                self.dark_theme()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CRModWindow = QtWidgets.QMainWindow()
    ui = Ui_CRModWindow()
    ui.setupUi(CRModWindow)
    qtmodern.styles.light(app)
    ui.load_settings()
    CRModWindow.show()
    sys.exit(app.exec_())
