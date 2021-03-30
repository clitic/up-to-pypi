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
opf_folder_location = ""
loaded = False
abs_path = os.path.dirname(__file__)
reader = ProcessOutputReader()

class Ui_WheelWindow(object):
    def setupUi(self, WheelWindow):
        WheelWindow.setObjectName("WheelWindow")
        WheelWindow.resize(600, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{abs_path}\\images\\upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WheelWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WheelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.output_box = output_console(self.centralwidget)
        self.output_box.setObjectName("output_box")
        self.gridLayout_3.addWidget(self.output_box, 6, 0, 1, 2)
        self.commands = QtWidgets.QLabel(self.centralwidget)
        self.commands.setObjectName("commands")
        self.gridLayout_3.addWidget(self.commands, 3, 0, 1, 2)
        self.commands_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.commands_box.setObjectName("commands_box")
        self.gridLayout_3.addWidget(self.commands_box, 4, 0, 1, 2)
        self.open_setup = QtWidgets.QPushButton(self.centralwidget)
        self.open_setup.setObjectName("open_setup")
        self.gridLayout_3.addWidget(self.open_setup, 1, 0, 1, 1)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout_3.addWidget(self.output, 5, 0, 1, 2)
        self.create_wheel = QtWidgets.QPushButton(self.centralwidget)
        self.create_wheel.setObjectName("create_wheel")
        self.gridLayout_3.addWidget(self.create_wheel, 2, 0, 1, 2)
        self.abort = QtWidgets.QPushButton(self.centralwidget)
        self.abort.setObjectName("abort")
        self.gridLayout_3.addWidget(self.abort, 1, 1, 1, 1)
        self.gridLayout_MainCheck = QtWidgets.QGridLayout()
        self.gridLayout_MainCheck.setObjectName("gridLayout_MainCheck")
        self.c10 = QtWidgets.QCheckBox(self.centralwidget)
        self.c10.setObjectName("c10")
        self.gridLayout_MainCheck.addWidget(self.c10, 3, 4, 1, 1)
        self.c12 = QtWidgets.QCheckBox(self.centralwidget)
        self.c12.setObjectName("c12")
        self.gridLayout_MainCheck.addWidget(self.c12, 4, 1, 1, 1)
        self.c8 = QtWidgets.QCheckBox(self.centralwidget)
        self.c8.setObjectName("c8")
        self.gridLayout_MainCheck.addWidget(self.c8, 3, 2, 1, 1)
        self.c9 = QtWidgets.QCheckBox(self.centralwidget)
        self.c9.setObjectName("c9")
        self.gridLayout_MainCheck.addWidget(self.c9, 3, 3, 1, 1)
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setObjectName("l5")
        self.gridLayout_MainCheck.addWidget(self.l5, 8, 0, 1, 1)
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setObjectName("c3")
        self.gridLayout_MainCheck.addWidget(self.c3, 2, 2, 1, 1)
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setObjectName("c4")
        self.gridLayout_MainCheck.addWidget(self.c4, 2, 3, 1, 1)
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setObjectName("c5")
        self.gridLayout_MainCheck.addWidget(self.c5, 2, 4, 1, 1)
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setObjectName("c6")
        self.gridLayout_MainCheck.addWidget(self.c6, 3, 0, 1, 1)
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setObjectName("l1")
        self.gridLayout_MainCheck.addWidget(self.l1, 1, 0, 1, 1)
        self.c20 = QtWidgets.QCheckBox(self.centralwidget)
        self.c20.setObjectName("c20")
        self.gridLayout_MainCheck.addWidget(self.c20, 7, 0, 1, 1)
        self.c17 = QtWidgets.QCheckBox(self.centralwidget)
        self.c17.setObjectName("c17")
        self.gridLayout_MainCheck.addWidget(self.c17, 5, 2, 1, 1)
        self.c13 = QtWidgets.QCheckBox(self.centralwidget)
        self.c13.setObjectName("c13")
        self.gridLayout_MainCheck.addWidget(self.c13, 4, 2, 1, 1)
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setObjectName("c1")
        self.gridLayout_MainCheck.addWidget(self.c1, 2, 0, 1, 1)
        self.c11 = QtWidgets.QCheckBox(self.centralwidget)
        self.c11.setObjectName("c11")
        self.gridLayout_MainCheck.addWidget(self.c11, 4, 0, 1, 1)
        self.c14 = QtWidgets.QCheckBox(self.centralwidget)
        self.c14.setObjectName("c14")
        self.gridLayout_MainCheck.addWidget(self.c14, 4, 3, 1, 1)
        self.c18 = QtWidgets.QCheckBox(self.centralwidget)
        self.c18.setObjectName("c18")
        self.gridLayout_MainCheck.addWidget(self.c18, 6, 0, 1, 1)
        self.c19 = QtWidgets.QCheckBox(self.centralwidget)
        self.c19.setObjectName("c19")
        self.gridLayout_MainCheck.addWidget(self.c19, 6, 2, 1, 1)
        self.cu1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cu1.setObjectName("cu1")
        self.gridLayout_MainCheck.addWidget(self.cu1, 9, 0, 1, 1)
        self.c15 = QtWidgets.QCheckBox(self.centralwidget)
        self.c15.setObjectName("c15")
        self.gridLayout_MainCheck.addWidget(self.c15, 5, 0, 1, 1)
        self.c16 = QtWidgets.QCheckBox(self.centralwidget)
        self.c16.setObjectName("c16")
        self.gridLayout_MainCheck.addWidget(self.c16, 5, 1, 1, 1)
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        self.l4.setObjectName("l4")
        self.gridLayout_MainCheck.addWidget(self.l4, 1, 4, 1, 1)
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setObjectName("c2")
        self.gridLayout_MainCheck.addWidget(self.c2, 2, 1, 1, 1)
        self.c7 = QtWidgets.QCheckBox(self.centralwidget)
        self.c7.setObjectName("c7")
        self.gridLayout_MainCheck.addWidget(self.c7, 3, 1, 1, 1)
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setObjectName("l3")
        self.gridLayout_MainCheck.addWidget(self.l3, 1, 3, 1, 1)
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setObjectName("l2")
        self.gridLayout_MainCheck.addWidget(self.l2, 1, 2, 1, 1)
        self.cu2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cu2.setObjectName("cu2")
        self.gridLayout_MainCheck.addWidget(self.cu2, 9, 2, 1, 1)
        self.cu1val = QtWidgets.QLineEdit(self.centralwidget)
        self.cu1val.setObjectName("cu1val")
        self.gridLayout_MainCheck.addWidget(self.cu1val, 10, 0, 1, 2)
        self.cu3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cu3.setObjectName("cu3")
        self.gridLayout_MainCheck.addWidget(self.cu3, 9, 4, 1, 1)
        self.cu2val = QtWidgets.QLineEdit(self.centralwidget)
        self.cu2val.setObjectName("cu2val")
        self.gridLayout_MainCheck.addWidget(self.cu2val, 10, 2, 1, 2)
        self.cu3val = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cu3val.sizePolicy().hasHeightForWidth())
        self.cu3val.setSizePolicy(sizePolicy)
        self.cu3val.setObjectName("cu3val")
        self.gridLayout_MainCheck.addWidget(self.cu3val, 10, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_MainCheck, 0, 0, 1, 2)
        WheelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WheelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuOptions_2 = QtWidgets.QMenu(self.menubar)
        self.menuOptions_2.setObjectName("menuOptions_2")
        WheelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WheelWindow)
        self.statusbar.setObjectName("statusbar")
        WheelWindow.setStatusBar(self.statusbar)
        self.actionOpen_Project_Folder = QtWidgets.QAction(WheelWindow)
        self.actionOpen_Project_Folder.setObjectName("actionOpen_Project_Folder")
        self.actionAdvance_Wheel_Creator = QtWidgets.QAction(WheelWindow)
        self.actionAdvance_Wheel_Creator.setObjectName("actionAdvance_Wheel_Creator")
        self.actionSave_AWC_Settings = QtWidgets.QAction(WheelWindow)
        self.actionSave_AWC_Settings.setCheckable(True)
        self.actionSave_AWC_Settings.setObjectName("actionSave_AWC_Settings")
        self.actionReport_A_Bug = QtWidgets.QAction(WheelWindow)
        self.actionReport_A_Bug.setObjectName("actionReport_A_Bug")
        self.actionRequest_New_Features = QtWidgets.QAction(WheelWindow)
        self.actionRequest_New_Features.setObjectName("actionRequest_New_Features")
        self.actionNeed_Help = QtWidgets.QAction(WheelWindow)
        self.actionNeed_Help.setObjectName("actionNeed_Help")
        self.actionCreate_Wheel = QtWidgets.QAction(WheelWindow)
        self.actionCreate_Wheel.setObjectName("actionCreate_Wheel")
        self.actionAbort = QtWidgets.QAction(WheelWindow)
        self.actionAbort.setObjectName("actionAbort")
        self.actionReset_To_Default = QtWidgets.QAction(WheelWindow)
        self.actionReset_To_Default.setObjectName("actionReset_To_Default")
        self.actionSave_A_bat_File = QtWidgets.QAction(WheelWindow)
        self.actionSave_A_bat_File.setObjectName("actionSave_A_bat_File")
        self.menuFile.addAction(self.actionOpen_Project_Folder)
        self.menuFile.addAction(self.actionSave_A_bat_File)
        self.menuHelp.addAction(self.actionAdvance_Wheel_Creator)
        self.menuOptions.addAction(self.actionSave_AWC_Settings)
        self.menuOptions.addAction(self.actionReset_To_Default)
        self.menuOptions_2.addAction(self.actionCreate_Wheel)
        self.menuOptions_2.addAction(self.actionAbort)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions_2.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(WheelWindow)
        QtCore.QMetaObject.connectSlotsByName(WheelWindow)

        WheelWindow.resizeEvent = self.resize_text
        WheelWindow.closeEvent = self.save_settings

        self.abort.clicked.connect(self.abort_qprocess)
        self.actionAbort.triggered.connect(lambda: self.abort_qprocess())
        self.create_wheel.clicked.connect(self.build_wheel)
        self.actionCreate_Wheel.triggered.connect(lambda: self.build_wheel())

        self.open_setup.clicked.connect(self.opf_popup)
        self.actionOpen_Project_Folder.triggered.connect(lambda: self.opf_popup())
        self.actionAdvance_Wheel_Creator.triggered.connect(lambda: self.about_awc())
        self.actionReset_To_Default.triggered.connect(lambda: self.Settings_Reset_To_Default())
        self.actionSave_A_bat_File.triggered.connect(lambda: self.save_bat())

        self.c1.stateChanged.connect(self.preview_commands)
        self.c2.stateChanged.connect(self.preview_commands)
        self.c3.stateChanged.connect(self.preview_commands)
        self.c4.stateChanged.connect(self.preview_commands)
        self.c5.stateChanged.connect(self.preview_commands)
        self.c6.stateChanged.connect(self.preview_commands)
        self.c7.stateChanged.connect(self.preview_commands)
        self.c8.stateChanged.connect(self.preview_commands)
        self.c9.stateChanged.connect(self.preview_commands)
        self.c10.stateChanged.connect(self.preview_commands)
        self.c11.stateChanged.connect(self.preview_commands)
        self.c12.stateChanged.connect(self.preview_commands)
        self.c13.stateChanged.connect(self.preview_commands)
        self.c14.stateChanged.connect(self.preview_commands)
        self.c15.stateChanged.connect(self.preview_commands)
        self.c16.stateChanged.connect(self.preview_commands)
        self.c17.stateChanged.connect(self.preview_commands)
        self.c18.stateChanged.connect(self.preview_commands)
        self.c19.stateChanged.connect(self.preview_commands)
        self.c20.stateChanged.connect(self.preview_commands)
        self.cu1.stateChanged.connect(self.preview_commands)
        self.cu2.stateChanged.connect(self.preview_commands)
        self.cu3.stateChanged.connect(self.preview_commands)
        self.cu1val.textEdited.connect(self.preview_commands)
        self.cu2val.textEdited.connect(self.preview_commands)
        self.cu3val.textEdited.connect(self.preview_commands)

        # Moving Window To Center
        qr = QtCore.QRect(0, 0, 750, 550)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        WheelWindow.move(qr.topLeft())

    def retranslateUi(self, WheelWindow):
        _translate = QtCore.QCoreApplication.translate
        WheelWindow.setWindowTitle(_translate("WheelWindow", "Advance Wheel Creator"))
        self.c2.setText(_translate("WheelWindow", "win_amd64"))
        self.c1.setText(_translate("WheelWindow", "manylinux2014_x86_64"))
        self.c18.setText(_translate("WheelWindow", "manylinux1_i686"))
        self.c4.setText(_translate("WheelWindow", "abi3"))
        self.c9.setText(_translate("WheelWindow", "cp33m"))
        self.c11.setText(_translate("WheelWindow", "manylinux2010_i686"))
        self.l1.setText(_translate("WheelWindow", "Platform Tags :-"))
        self.c7.setText(_translate("WheelWindow", "win32"))
        self.l3.setText(_translate("WheelWindow", "ABI Tags (Experimental) :-"))
        self.c3.setText(_translate("WheelWindow", "cp39"))
        self.c8.setText(_translate("WheelWindow", "cp38"))
        self.c15.setText(_translate("WheelWindow", "manylinux2010_x86_64"))
        self.c5.setText(_translate("WheelWindow", "Universal Wheel"))
        self.c10.setToolTip(_translate("WheelWindow", "Removes/Delete unwanted folders\n"
                                    "created by running commands\n"
                                    "only dist folder will be left"))
        self.c10.setText(_translate("WheelWindow", "Keep Dist Only"))
        self.c17.setText(_translate("WheelWindow", "cp36"))
        self.c12.setText(_translate("WheelWindow", "macosx_10_13_intel"))
        self.l4.setText(_translate("WheelWindow", "Others :-"))
        self.l2.setText(_translate("WheelWindow", "Limit API :-"))
        self.c6.setText(_translate("WheelWindow", "manylinux2014_aarch64"))
        self.c19.setText(_translate("WheelWindow", "cp27"))
        self.c13.setText(_translate("WheelWindow", "cp37"))
        self.c20.setText(_translate("WheelWindow", "manylinux1_x86_64"))
        self.c16.setText(_translate("WheelWindow", "macosx_10_9_x86_64"))
        self.c14.setText(_translate("WheelWindow", "none"))
        self.open_setup.setText(_translate("WheelWindow", "Open Project Folder"))
        self.abort.setText(_translate("WheelWindow", "Abort"))
        self.commands_box.setText(_translate("WheelWindow", "NULL"))
        self.create_wheel.setText(_translate("WheelWindow", "Create Wheel"))
        self.commands.setText(_translate("WheelWindow", "Commands Going To Execute :-"))
        self.menuFile.setTitle(_translate("WheelWindow", "File"))
        self.menuHelp.setTitle(_translate("WheelWindow", "Help"))
        self.menuOptions.setTitle(_translate("WheelWindow", "Settings"))
        self.menuOptions_2.setTitle(_translate("WheelWindow", "Options"))
        self.actionOpen_Project_Folder.setText(_translate("WheelWindow", "Open Project Folder"))
        self.actionAdvance_Wheel_Creator.setText(_translate("WheelWindow", "About Advance Wheel Creator"))
        self.actionSave_AWC_Settings.setText(_translate("WheelWindow", "Save AWC Settings"))
        self.actionReport_A_Bug.setText(_translate("WheelWindow", "Report A Bug"))
        self.actionRequest_New_Features.setText(_translate("WheelWindow", "Request New Features"))
        self.actionNeed_Help.setText(_translate("WheelWindow", "Need Help ?"))
        self.actionCreate_Wheel.setText(_translate("WheelWindow", "Create Wheel"))
        self.actionAbort.setText(_translate("WheelWindow", "Abort"))
        self.actionReset_To_Default.setText(_translate("WheelWindow", "Reset To Default"))
        self.actionSave_A_bat_File.setText(_translate("WheelWindow", "Save A .bat File"))
        self.actionSave_A_bat_File.setShortcut(_translate("WheelWindow", "Ctrl+S"))
        self.output.setText(_translate("WheelWindow", "Output Terminal :-"))
        self.output_box.setText(_translate("WheelWindow", "NULL"))
        self.l5.setText(_translate("WheelWindow", "Customs :-"))
        self.cu1.setText(_translate("WheelWindow", "custom platform"))
        self.cu2.setText(_translate("WheelWindow", "custom api"))
        self.cu3.setText(_translate("WheelWindow", "build number"))

        self.output.deleteLater()
        self.output_box.deleteLater()

    def resize_text(self, event):
        default_size = 11
        width = WheelWindow.frameGeometry().width()

        if width // 100> default_size:
            font_size_change = QtGui.QFont('Roboto', width // 100)
            font_size_change2 = QtGui.QFont('Roboto', width // 100)
        else:
            font_size_change = QtGui.QFont('Roboto', default_size)
            font_size_change2 = QtGui.QFont()

        self.l1.setFont(font_size_change2)
        self.l2.setFont(font_size_change2)
        self.l3.setFont(font_size_change2)
        self.l4.setFont(font_size_change2)
        self.l5.setFont(font_size_change2)

        self.c1.setFont(font_size_change)
        self.c2.setFont(font_size_change)
        self.c3.setFont(font_size_change)
        self.c4.setFont(font_size_change)
        self.c5.setFont(font_size_change)
        self.c6.setFont(font_size_change)
        self.c7.setFont(font_size_change)
        self.c8.setFont(font_size_change)
        self.c9.setFont(font_size_change)
        self.c10.setFont(font_size_change)
        self.c11.setFont(font_size_change)
        self.c12.setFont(font_size_change)
        self.c13.setFont(font_size_change)
        self.c14.setFont(font_size_change)
        self.c15.setFont(font_size_change)
        self.c16.setFont(font_size_change)
        self.c17.setFont(font_size_change)
        self.c18.setFont(font_size_change)
        self.c19.setFont(font_size_change)
        self.c20.setFont(font_size_change)
        self.cu1.setFont(font_size_change)
        self.cu2.setFont(font_size_change)
        self.cu3.setFont(font_size_change)
        self.cu1val.setFont(font_size_change)
        self.cu2val.setFont(font_size_change)
        self.cu3val.setFont(font_size_change)

        self.open_setup.setFont(font_size_change2)
        self.abort.setFont(font_size_change2)
        self.create_wheel.setFont(font_size_change2)

        self.commands.setFont(font_size_change2)

        self.commands_box.setFont(font_size_change)

        if loaded:
        	self.output.setFont(font_size_change2)

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
    	platforms = []

    	if self.cu2.isChecked():
    		apis = f"--py-limited-api {self.cu2val.text()}"
    	else:
    		all_api = []
    		if self.c3.isChecked(): all_api.append("cp39")
    		if self.c8.isChecked(): all_api.append("cp38")
    		if self.c13.isChecked(): all_api.append("cp37")
    		if self.c17.isChecked(): all_api.append("cp36")
    		if self.c19.isChecked(): all_api.append("cp27")
    		all_api = ".".join(all_api)
    		if len(all_api) == 0:
    			apis = ""
    		else:
    			apis = f"--py-limited-api {all_api} --python-tag {all_api}"

    	if self.cu3.isChecked():
    		buildno = f"--build-number {self.cu3val.text()}"
    	else:
    		buildno = ""

    	if self.cu1.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name {self.cu1val.text()}")    			
    	if self.c5.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {buildno} --universal")
    	if self.c1.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux2014_x86_64")
    	if self.c6.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux2014_aarch64")
    	if self.c11.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux2010_i686")
    	if self.c15.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux2010_x86_64")
    	if self.c18.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux1_i686")
    	if self.c20.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name manylinux1_x86_64")
    	if self.c2.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name win_amd64")
    	if self.c7.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name win32")
    	if self.c12.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {apis} {buildno} --plat-name macosx_10_13_intel")
    	if self.c16.isChecked():
    		platforms.append(f"python setup.py sdist bdist_wheel {buildno} --plat-name macosx_10_9_x86_64")
    	if len(platforms) == 0:
    		return [f"python setup.py sdist bdist_wheel {apis} {buildno} "]
    	else:
    		return platforms

    def preview_commands(self):
    	with open(f"{abs_path}\\assets\\wheel_commands.txt", "w", encoding="utf-8") as f:
    		for commands in self.all_commands():
    			f.write(f"{commands}\n")

    	with open (f"{abs_path}\\assets\\wheel_commands.txt", encoding="utf-8") as f:
    		readings = f.read()
    		_translate = QtCore.QCoreApplication.translate
    		self.commands_box.setText(_translate("MainWindow", readings))

    def create_bat(self, location):
    	module_dir = opf_folder_location.replace("/", "\\")
    	with open (location, "w", encoding="utf-8") as f:
		    f.write(f'cd /d "{module_dir}"\n')
		    for commands in self.all_commands():
		    	f.write(f"{commands}\n")
		    if self.c10.isChecked():
		    	f.write("rmdir /s /q build\n")
		    	f.write(f'for /f "usebackq tokens=*" %%i in (`dir /b /s /a:d *egg-info*`) do (rd /s /q "%%i")\n')
		    if self.c4.isChecked() or self.c9.isChecked() or self.c14.isChecked():
			    f.write(f'cd /d "{module_dir}\\dist"\n')
			    if self.c14.isChecked():
			    	f.write(r'''powershell -C "gci | %% {rni $_.Name ($_.Name -replace '-none', '')}"''')
			    	f.write("\n")
			    if self.c4.isChecked():
			    	f.write(r'''powershell -C "gci | %% {rni $_.Name ($_.Name -replace '-none', '-abi3')}"''')
			    	f.write("\n")
			    if self.c9.isChecked():
			    	f.write(r'''powershell -C "gci | %% {rni $_.Name ($_.Name -replace '-none', '-cp33m')}"''')
			    	f.write("\n")			    	
		    f.write("echo off\n"
		        "echo =======\n"
		        "echo FINISHED\n"
		        "echo =======\n")

    def build_wheel(self):
    	global loaded

    	if loaded:
    		pass
    	else:
    		self.output = QtWidgets.QLabel(self.centralwidget)
    		self.output.setObjectName("output")
    		self.gridLayout_3.addWidget(self.output, 5, 0, 1, 2)
    		self.output_box = output_console(self.centralwidget)
    		self.output_box.setObjectName("output_box")
    		self.output_box.setFont(QtGui.QFont('Roboto', 11))
    		self.gridLayout_3.addWidget(self.output_box, 6, 0, 1, 2)
    		_translate = QtCore.QCoreApplication.translate
    		self.output.setText(_translate("WheelWindow", "Output Terminal :-"))
    		self.output_box.setText(_translate("WheelWindow", "NULL"))
    		loaded = True

    	self.create_bat(f"{abs_path}\\assets\\wheel_commands.bat")
    	os.chdir(f"{abs_path}\\assets")
    	self.output_box = output_console(self.centralwidget)
    	self.output_box.setObjectName("output_box")
    	self.output_box.setFont(QtGui.QFont('Roboto', 11))
    	self.gridLayout_3.addWidget(self.output_box, 6, 0, 1, 2)
    	reader.produce_output.connect(self.output_box.append_output)
    	reader.start('wheel_commands.bat')

    def save_bat(self):
        opf_folder = QtWidgets.QFileDialog.getSaveFileName(filter="Batch Files (*.bat)")
        location_to_save = opf_folder[0].replace("/", "\\")
        filename = opf_folder[0].split("/")[-1]
        try:
        	self.create_bat(location_to_save)
        	_translate = QtCore.QCoreApplication.translate
        	WheelWindow.setStatusTip(_translate("WheelWindow", f"{filename} Saved At {opf_folder[0]}"))

        except FileNotFoundError:
        	pass

    def about_awc(self):
        msg = QMessageBox()
        msg.setWindowTitle("About Advance Wheel Creator")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Advance Wheel Creator v1.0.0")
        msg.setInformativeText("Developed By 360modder")
        msg.exec_()

    def Settings_Reset_To_Default(self):
        self.c1.setChecked(False)
        self.c2.setChecked(False)
        self.c3.setChecked(False)
        self.c4.setChecked(False)
        self.c5.setChecked(False)
        self.c6.setChecked(False)
        self.c7.setChecked(False)
        self.c8.setChecked(False)
        self.c9.setChecked(False)
        self.c10.setChecked(False)
        self.c11.setChecked(False)
        self.c12.setChecked(False)
        self.c13.setChecked(False)
        self.c14.setChecked(False)
        self.c15.setChecked(False)
        self.c16.setChecked(False)
        self.c17.setChecked(False)
        self.c18.setChecked(False)
        self.c19.setChecked(False)
        self.c20.setChecked(False)
        self.cu1.setChecked(False)
        self.cu2.setChecked(False)
        self.cu3.setChecked(False)
        self.cu1val.clear()
        self.cu2val.clear()
        self.cu3val.clear()
        self.actionSave_AWC_Settings.setChecked(True)

        _translate = QtCore.QCoreApplication.translate
        if loaded:
        	self.output_box.setText(_translate("WheelWindow", "NULL")) 
        WheelWindow.setStatusTip(_translate("WheelWindow", "Settings Resetted To Default"))

    def light_theme(self):
        qtmodern.styles.light(app)

    def dark_theme(self):
        qtmodern.styles.dark(app)

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

        with open (f"{abs_path}\\assets\\settings_wheel.txt", encoding="utf-8") as f:
            read = f.read()
            read = read.split("\n")

            if read[26] == "True":
                self.cu1val.setText(read[23])
                self.cu2val.setText(read[24])            	
                self.cu3val.setText(read[25])            	
                check_boxes(read[0], self.c1)
                check_boxes(read[1], self.c2)
                check_boxes(read[2], self.c3)
                check_boxes(read[3], self.c4)
                check_boxes(read[4], self.c5)
                check_boxes(read[5], self.c6)
                check_boxes(read[6], self.c7)
                check_boxes(read[7], self.c8)
                check_boxes(read[8], self.c9)
                check_boxes(read[9], self.c10)
                check_boxes(read[10], self.c11)
                check_boxes(read[11], self.c12)
                check_boxes(read[12], self.c13)
                check_boxes(read[13], self.c14)
                check_boxes(read[14], self.c15)
                check_boxes(read[15], self.c16)
                check_boxes(read[16], self.c17)
                check_boxes(read[17], self.c18)
                check_boxes(read[18], self.c19)
                check_boxes(read[19], self.c20)
                check_boxes(read[20], self.cu1)
                check_boxes(read[21], self.cu2)
                check_boxes(read[22], self.cu3)
                check_boxes(read[26], self.actionSave_AWC_Settings)
            else:
                pass

    def save_settings(self, event):
        with open (f"{abs_path}\\assets\\settings_wheel.txt", "w", encoding="utf-8") as f:
            f.write(f"{self.c1.isChecked()}\n")
            f.write(f"{self.c2.isChecked()}\n")
            f.write(f"{self.c3.isChecked()}\n")
            f.write(f"{self.c4.isChecked()}\n")
            f.write(f"{self.c5.isChecked()}\n")
            f.write(f"{self.c6.isChecked()}\n")
            f.write(f"{self.c7.isChecked()}\n")
            f.write(f"{self.c8.isChecked()}\n")
            f.write(f"{self.c9.isChecked()}\n")
            f.write(f"{self.c10.isChecked()}\n")
            f.write(f"{self.c11.isChecked()}\n")
            f.write(f"{self.c12.isChecked()}\n")
            f.write(f"{self.c13.isChecked()}\n")
            f.write(f"{self.c14.isChecked()}\n")
            f.write(f"{self.c15.isChecked()}\n")
            f.write(f"{self.c16.isChecked()}\n")
            f.write(f"{self.c17.isChecked()}\n")
            f.write(f"{self.c18.isChecked()}\n")
            f.write(f"{self.c19.isChecked()}\n")
            f.write(f"{self.c20.isChecked()}\n")
            f.write(f"{self.cu1.isChecked()}\n")
            f.write(f"{self.cu2.isChecked()}\n")
            f.write(f"{self.cu3.isChecked()}\n")
            f.write(f"{self.cu1val.text()}\n")
            f.write(f"{self.cu2val.text()}\n")
            f.write(f"{self.cu3val.text()}\n")
            f.write(f"{self.actionSave_AWC_Settings.isChecked()}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    WheelWindow = QtWidgets.QMainWindow()
    ui = Ui_WheelWindow()
    ui.setupUi(WheelWindow)
    qtmodern.styles.light(app)
    ui.load_settings()
    WheelWindow.show()
    sys.exit(app.exec_())
