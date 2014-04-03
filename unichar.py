# -*- coding: utf-8 -*-
from __future__ import unicode_literals
myname = "UniChar"
__version__ = '0.6.1.2'

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
        self.hexCode = QLineEdit()
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
        layout2.addWidget(self.hexCode)

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

        self.connect(self.myChar, SIGNAL("returnPressed()"), self.change_by_char)
        self.connect(self.hexCode, SIGNAL("returnPressed()"), self.change_by_hex)
        self.connect(self.decCode, SIGNAL("returnPressed()"), self.change_by_dec)

    def change_by_char(self):
        _char = self.myChar.text()
        self.displayText2(_char)

    def change_by_hex(self):
        # TODO
        # 한글을 입력한 후 10진수 입력하면 16진수값이 바뀌지 않는 문제 있음
        _code = self.hexCode.text()
        _code = _code.toUpper()
        if _code[0:2] == QString('U+'):
            _code = _code[2:]
        try:
            _code = int(unicode(_code), 16)  #convert hex to integer
            _char = unichr(_code)
            self.displayText2(_char)
        except:
            self.clear()

    def change_by_dec(self):
        _code = self.decCode.text()
        try:
            _char = unichr(int(_code))
            self.displayText2(_char)
        except:
            self.clear()

    def setFormatText(self, code):
        self.lblFileFormat.setText("<a href='http://www.fileformat.info/info/unicode/char/{}/index.htm'>more info</a>".format(unicode(code)))

    def setCharInfo(self, _char):
        ch = unicode(_char)  # ex) 'a', '가', ...
        uni_hex = "%04X" % (ord(unicode(_char)))  # if '가': AC00
        uni_dec = unicode(ord(ch))  # if '가': 44032
        uni_name = unicodedata.name(ch)  # if '가': HANGUL SYLLABLE GA
        cat = unicodedata.category(ch)  # if '가': Lo
        return dict(char=_char,
                    ch=ch,
                    uni_hex=uni_hex,
                    uni_dec=uni_dec,
                    uni_name=uni_name,
                    cat=cat
                    )

    def clear(self):
        self.myChar.setText("")
        self.hexCode.setText("")
        self.decCode.setText("")
        self.lblUniName.setText("")
        self.lblCategory.setText("")
        self.setFormatText("")

    def displayText(self, _char):
        ci = self.setCharInfo(_char)

        self.myChar.setText(QString(ci['char']))
        self.hexCode.setText(QString(ci['uni_hex']))
        self.decCode.setText(ci['uni_dec'])
        self.lblUniName.setText(ci['uni_name'])
        self.lblCategory.setText(get_category(ci['cat']))
        self.setFormatText(ci['uni_hex'])

    def displayText2(self, _char):
        ci = self.setCharInfo(_char)
        try:
            self.myChar.setText(QString(ci['char']))
            self.hexCode.setText(QString(ci['uni_hex']))
            self.decCode.setText(ci['uni_dec'])
            self.lblUniName.setText(ci['uni_name'])
            self.lblCategory.setText(get_category(ci['cat']))
            self.setFormatText(ci['uni_hex'])
        except:
            self.clear()
        finally:
            self.selectAll(self.sender())

    def selectAll(self, sender):
        sender.selectAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mycode = UniChar()
    mycode.show()
    sys.exit(app.exec_())
