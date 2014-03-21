# -*- coding: utf-8 -*-
from __future__ import unicode_literals
myname = "UniChar"
__version__ = '0.5'

import sys
import unicodedata
from PyQt4.QtGui import QDialog, QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt4.QtCore import Qt, SIGNAL, QString


class TheCode(QDialog):
    def __init__(self, parent=None):
        super(TheCode, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("{0} v{1}".format(myname, __version__))
        lblScript = QLabel('Character')
        self.myChar = QLineEdit()
        self.myChar.setMaxLength(1)
        self.btnCode = QPushButton("Code")
        self._lblUnicode = QLabel()
        self.lblUnicode = QLabel("Unicode")
        self.myCode = QLineEdit()
        self._lblUniName = QLabel("Unicode Name")
        self.lblUniName = QLabel()
        self.lblUniName.setAlignment(Qt.AlignRight)
        self.lblFileFormat = QLabel("More Info")
        self.lblFileFormat.setOpenExternalLinks(True)
        self.lblFileFormat.setAlignment(Qt.AlignRight)

        layout = QGridLayout()

        layout1 = QHBoxLayout()
        layout1.addWidget(lblScript)
        layout1.addWidget(self.myChar)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.lblUnicode)
        layout2.addWidget(self.myCode)

        layout3 = QVBoxLayout()
        layout3.addWidget(self._lblUniName)
        layout3.addWidget(self.lblUniName)
        layout3.addWidget(self.lblFileFormat)

        layout.addLayout(layout1, 0, 0)
        layout.addLayout(layout2, 1, 0)
        layout.addLayout(layout3, 4, 0)

        self.setLayout(layout)

        self.connect(self.myChar, SIGNAL("returnPressed()"), self.showCode)
        self.connect(self.myCode, SIGNAL("returnPressed()"), self.showChar)

    def _setText(self, code):
        self.lblFileFormat.setText("<a href='http://www.fileformat.info/info/unicode/char/{}/index.htm'>more info</a>".format(unicode(code)))

    def showCode(self):
        _char = self.myChar.text()
        _unicode = "%04X" % (ord(unicode(_char)))
        self._setText(_unicode)
        self.myCode.setText(QString(_unicode))
        try:
            UNINAME = unicodedata.name(unicode(_char))
            self.lblUniName.setText(UNINAME)
        except:
            self.lblUniName.setText("")
        finally:
            self.myChar.selectAll()

    def showChar(self):
        _code = self.myCode.text()
        _code = _code.toUpper()
        if _code[0:2] == QString('U+'):
            _code = _code[2:]
        self._setText(_code)
        self.myCode.setText(_code.toUpper())
        try:
            _code = int(unicode(_code), 16)  #convert hex to integer
            _unicode = unichr(_code)
            self.myChar.setText(QString(_unicode))
            UNINAME = unicodedata.name(unichr(_code))
            self.lblUniName.setText(UNINAME)
        except:
            self.lblUniName.setText("")
        finally:
            self.myCode.selectAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycode = TheCode()
    mycode.show()
    sys.exit(app.exec_())
