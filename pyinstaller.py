"""
Main command-line interface to PyInstaller.
"""
import  os

if __name__ == '__main__':
    os.system('pyinstaller -i icon.ico -F -w main.py')