import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['string', 'random'], 'includes': ['customtkinter', 'pyperclip']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name = 'Gerador de Senhas',
    version = '0.1',
    description = 'Um projeto desenvolvido em Python, com interface gráfica moderna utilizando CustomTkinter',
    options = {'build_exe': build_exe_options},
    executables = [Executable('main.py', base=base)]
)