import os
import platform
import subprocess


is_windows = platform.system().lower().startswith("win")

def main():
    subprocess.run(["python" if is_windows else "python3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")])


if __name__ == "__main__":
    main()
