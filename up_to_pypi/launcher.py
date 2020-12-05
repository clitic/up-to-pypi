import os

abs_path = os.path.dirname(__file__)

def main():
	try:
		import PyQt5
		import qtmodern.styles
		import qtmodern.windows
	except:
		# Slow Loading
		os.startfile(f"{abs_path}\\up_to_pypi.exe")
		print("Loading EXE . . .")
		exit()

	# Faster Loading
	os.startfile(f"{abs_path}\\main.pyw")
	print("Loading PYW . . .")
	exit()

if __name__ == '__main__':
	main()