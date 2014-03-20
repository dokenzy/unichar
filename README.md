unichar
=======

Show unicode codepoint and single character

Screenshot
----------
![unichar screenshot](https://raw.github.com/dokenzy/unichar/master/unichar.png)

Usage
-----
 * Character: Input a character and hit Enter. If multi-bytes character like '가', hit Enter 2 times.
 * Unicode: 'AC00' or 'U+AC00'(case insensitive)


Require
--------
Python 2.7, PyQt4


Build
-----
python setup.py py2app(Mac)


To Do
-----
* Packaging for Windows using cx_Freeze
* setup.py 하나로 Mac과 Windows 모두 빌드할 수 있도록.
