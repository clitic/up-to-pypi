import os
import sys
import platform
import subprocess
import traceback
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox


is_windows = sys.platform.lower().startswith("win")

class SubprocessWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def __init__(self, cmd) -> None:
        super().__init__()
        self.cmd = cmd
        self.read_output = True

    def run(self):
    	process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, encoding="utf-8")

    	while True:
    		realtime_output = process.stdout.readline()

    		if not self.read_output:
    			try:
    				process.terminate()
    			except:
    				process.kill()
    			break

    		if realtime_output == "" and process.poll() is not None:
    			break

    		if realtime_output:
    			self.progress.emit(realtime_output.strip())

    	self.finished.emit()

    def stop(self):
        self.read_output = False

def error_message(title, message):
	msg = QMessageBox()
	msg.setWindowTitle("Up To PyPi Error")
	msg.setIcon(QMessageBox.Critical)
	msg.setText(title)
	msg.setInformativeText(message)
	msg.exec_()

def traceback_catch(fn):
	def wrapper(*args, **kwargs):
		return_obj = None
		try:
			return_obj = fn(args[0])
		except Exception as e:
			msg = QMessageBox()
			msg.setWindowTitle(e.__class__.__name__)
			msg.setIcon(QMessageBox.Critical)
			msg.setText(e.__str__())
			msg.setInformativeText(traceback.format_exc())
			msg.exec_()			
		return return_obj
	return wrapper

def cwd_of_script(basepath):
	"""
	returns base path of script
	"""
	
	try:
		cwd = os.path.dirname(os.path.abspath(basepath))
	except:
		cwd = sys.executable

	return cwd

def platform_path(path):
	return path.replace("/", "\\") if is_windows else path.replace("\\", "/")
