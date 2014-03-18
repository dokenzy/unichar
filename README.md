unichar
=======

Show unicode codepoint and single character

Require
--------
Python 2.7, PyQt4

Bug
---
* Can't input non-ascii character like '가'. But can input 'ac00' in input box 'Unicode'.

To Do
-----
* Packaging for Windows using cx_Freeze
* setup.py 하나로 Mac과 Windows 모두 빌드할 수 있도록.
* 코드를 입력할 때 U+AC00 처럼 입력해도 처리할 수 있도록 수정