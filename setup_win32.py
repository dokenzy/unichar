# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"optimize": 2, }
includes = ["sip", "PyQt4.QtCore", "PyQt4.QtGui", "atexit"]
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="The Code",
    version="0.2",
    description="This app show unicode info",
    options={"build_exe": {"includes": includes}},
    executables=[Executable("thecode.py", base=base)])

"""
v0.2 2012. 9. 27
문자입력 후 엔터키 치면 자동으로 전체선택되도록 수정. 다른 문자 입력을 편하게 하기 위해.

v0.1
기본 기능 구현
"""
