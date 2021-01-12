import sys
from cx_Freeze import setup, Executable
import PySimpleGUI
import subprocess

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("Ponto_Format.py", base=base, icon='C:\icon.ico')]

buildOptions = dict(
        packages=[],
        includes=['PySimpleGUI', 'subprocess'],
        include_files=[],
        excludes=[]
)

setup(
    name="ponto_format",
    version="0.1",
    description="Edicao basica de textos",
    author="Lucas Vitor",
    options=dict(build_exe=buildOptions),
    executables=executables
)

