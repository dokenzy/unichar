# -*- coding: utf-8 -*-
from __future__ import unicode_literals
myname = "UniChar"
__version__ = '0.6'

import sys
import unicodedata
from PyQt4.QtGui import QDialog, QApplication, QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt4.QtCore import Qt, SIGNAL, QString

from categories import CATEGORIES


def get_category(cat):
    return CATEGORIES[cat]


class UniChar(QDialog):
    def __init__(self, parent=None):
        super(UniChar, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("{0} v{1}".format(myname, __version__))
        lblScript = QLabel('Character')
        self.myChar = QLineEdit()
        self.myChar.setMaxLength(1)
        self.btnCode = QPushButton("Code")
        self._lblUnicode = QLabel()
        self.lblUnicode = QLabel("Unicode Hex")
        # TODO
        # 변수명 변경 myCode > hexCode
        self.myCode = QLineEdit()
        self.lblUnicodeDec = QLabel("Unicode Dec")
        self.decCode = QLineEdit()
        self._lblUniName = QLabel("Unicode Name")
        self.lblUniName = QLabel()
        self.lblUniName.setAlignment(Qt.AlignRight)
        self._lblCategory = QLabel("Category")
        self.lblCategory = QLabel()
        self.lblCategory.setAlignment(Qt.AlignRight)
        self.lblFileFormat = QLabel("More Info")
        self.lblFileFormat.setOpenExternalLinks(True)
        self.lblFileFormat.setAlignment(Qt.AlignRight)
        self.lblUniDataVersion = QLabel('Unicode DB Ver: {}'.format(unicodedata.unidata_version))
        self.lblUniDataVersion.setAlignment(Qt.AlignRight)

        layout = QGridLayout()

        layout1 = QHBoxLayout()
        layout1.addWidget(lblScript)
        layout1.addWidget(self.myChar)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.lblUnicode)
        layout2.addWidget(self.myCode)

        layout3 = QHBoxLayout()
        layout3.addWidget(self.lblUnicodeDec)
        layout3.addWidget(self.decCode)

        layout4 = QVBoxLayout()
        layout4.addWidget(self._lblUniName)
        layout4.addWidget(self.lblUniName)

        layout5 = QHBoxLayout()
        layout5.addWidget(self._lblCategory)
        layout5.addWidget(self.lblCategory)

        layout6 = QVBoxLayout()
        layout6.addWidget(self.lblFileFormat)
        layout6.addWidget(self.lblUniDataVersion)

        layout.addLayout(layout1, 0, 0)
        layout.addLayout(layout2, 1, 0)
        layout.addLayout(layout3, 2, 0)
        layout.addLayout(layout4, 3, 0)
        layout.addLayout(layout5, 4, 0)
        layout.addLayout(layout6, 5, 0)

        self.setLayout(layout)

        self.connect(self.myChar, SIGNAL("returnPressed()"), self.showCode)
        self.connect(self.myCode, SIGNAL("returnPressed()"), self.showChar)
        self.connect(self.decCode, SIGNAL("returnPressed()"), self.showCharHex)

    def _setText(self, code):
        self.lblFileFormat.setText("<a href='http://www.fileformat.info/info/unicode/char/{}/index.htm'>more info</a>".format(unicode(code)))

    def showCode(self):
        _char = self.myChar.text()
        _unicode = "%04X" % (ord(unicode(_char)))
        self._setText(_unicode)
        self.myCode.setText(QString(_unicode))
        try:
            ch = unicode(_char)
            UNINAME = unicodedata.name(ch)
            cat = unicodedata.category(ch)
            DEC = unicode(ord(unicode(_char)))
            self.lblUniName.setText(UNINAME)
            self.lblCategory.setText(get_category(cat))
            self.decCode.setText(DEC)
        except:
            self.lblUniName.setText("")
            self.lblCategory.setText("")
            self.decCode.setText("")
        finally:
            self.myChar.selectAll()

    def showChar(self):
        # TODO
        # 한글을 입력한 후 10진수 입력하면 16진수값이 바뀌지 않는 문제 있음
        _code = self.myCode.text()
        _code = _code.toUpper()
        if _code[0:2] == QString('U+'):
            _code = _code[2:]
        self._setText(_code)
        self.myCode.setText(_code.toUpper())
        try:
            DEC = unicode(_code)
            _code = int(DEC, 16)  #convert hex to integer
            _unicode = unichr(_code)
            self.myChar.setText(QString(_unicode))
            UNINAME = unicodedata.name(unichr(_code))
            cat = unicodedata.category(unichr(_code))
            self.lblUniName.setText(UNINAME)
            self.lblCategory.setText(get_category(cat))
            self.decCode.setText(unicode(_code))
        except:
            self.lblUniName.setText("")
            self.lblCategory.setText("")
            self.decCode.setText("")
        finally:
            self.myCode.selectAll()

    def showCharHex(self):
        _code = self.decCode.text()
        self._setText(_code)
        self.decCode.setText(_code)
        try:
            # TODO
            # refactoring
            _code = int(_code)
            DEC = unicode(_code)
            hexcode = hex(_code)[2:]  #convert integer to hex
            _unicode = unichr(_code)
            self.myChar.setText(QString(_unicode))
            UNINAME = unicodedata.name(unichr(_code))
            cat = unicodedata.category(unichr(_code))
            self.lblUniName.setText(UNINAME)
            self.myCode.setText(unicode(hexcode))
            self.lblCategory.setText(get_category(cat))
            self.decCode.setText(DEC)
        except:
            self.lblUniName.setText("")
            self.lblCategory.setText("")
            self.decCode.setText("")
        finally:
            self.decCode.selectAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycode = UniChar()
    mycode.show()
    sys.exit(app.exec_())
