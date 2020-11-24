import platform, os

abs_path = os.path.dirname(__file__)
operating_system = platform.system()

def main():
	if operating_system == 'Windows':
		os.startfile(f"{abs_path}\main_win.pyw")
	else:
		os.system("python3 main_linux.py")

if __name__ == '__main__':
	main()