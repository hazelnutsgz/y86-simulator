# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\github\y86-simulator\gui\y86.ui'
#
# Created: Mon Jun 17 01:14:00 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Y86Simulator(object):
    def setupUi(self, Y86Simulator):
        Y86Simulator.setObjectName(_fromUtf8("Y86Simulator"))
        Y86Simulator.resize(971, 693)
        Y86Simulator.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Y86Simulator.setStyleSheet(_fromUtf8("QDialog\n"
"{\n"
"border-image:url(\'ps8.jpg\');\n"
"}\n"
"QMessageBox\n"
"{\n"
"border-image:none;\n"
"}\n"
"\n"
"QTextBrowser\n"
"{\n"
"background:rgb(243, 221, 255,0);\n"
"border:rgb(243, 221, 255,0);\n"
"font: 15pt \"Chiller\";\n"
"}\n"
"QLineEdit\n"
"{\n"
"background:rgb(243, 221, 255,0);\n"
"border:rgb(243, 221, 255,0);\n"
"font: 15pt \"Chiller\";\n"
"}\n"
"\n"
""))
        self.Slider = QtGui.QSlider(Y86Simulator)
        self.Slider.setGeometry(QtCore.QRect(559, 150, 171, 22))
        self.Slider.setStyleSheet(_fromUtf8("QSlider::groove:horizontal {\n"
"    border:none;\n"
"    background:none;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: none;\n"
"    border-image:url(\'bu.png\');\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 20px;\n"
"    margin: -2px 0;\n"
"    border-radius: 3px;\n"
"}"))
        self.Slider.setMinimum(50)
        self.Slider.setMaximum(200)
        self.Slider.setProperty("value", 200)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName(_fromUtf8("Slider"))
        self.layoutWidget_3 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget_3.setGeometry(QtCore.QRect(100, 330, 461, 70))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_27 = QtGui.QLabel(self.layoutWidget_3)
        self.label_27.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_5.addWidget(self.label_27, 0, 5, 1, 1)
        self.label_32 = QtGui.QLabel(self.layoutWidget_3)
        self.label_32.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_5.addWidget(self.label_32, 0, 9, 1, 1)
        self.label_31 = QtGui.QLabel(self.layoutWidget_3)
        self.label_31.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_5.addWidget(self.label_31, 0, 4, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget_3)
        self.label_30.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_5.addWidget(self.label_30, 0, 3, 1, 1)
        self.E_icode = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_icode.sizePolicy().hasHeightForWidth())
        self.E_icode.setSizePolicy(sizePolicy)
        self.E_icode.setMinimumSize(QtCore.QSize(20, 35))
        self.E_icode.setMaximumSize(QtCore.QSize(20, 24))
        self.E_icode.setBaseSize(QtCore.QSize(70, 20))
        self.E_icode.setStyleSheet(_fromUtf8(""))
        self.E_icode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.E_icode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.E_icode.setObjectName(_fromUtf8("E_icode"))
        self.gridLayout_5.addWidget(self.E_icode, 1, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.layoutWidget_3)
        self.label_26.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_5.addWidget(self.label_26, 0, 2, 1, 1)
        self.E_dstM = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_dstM.sizePolicy().hasHeightForWidth())
        self.E_dstM.setSizePolicy(sizePolicy)
        self.E_dstM.setMinimumSize(QtCore.QSize(20, 35))
        self.E_dstM.setMaximumSize(QtCore.QSize(20, 24))
        self.E_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.E_dstM.setStyleSheet(_fromUtf8(""))
        self.E_dstM.setObjectName(_fromUtf8("E_dstM"))
        self.gridLayout_5.addWidget(self.E_dstM, 1, 8, 1, 1)
        self.label_29 = QtGui.QLabel(self.layoutWidget_3)
        self.label_29.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_5.addWidget(self.label_29, 0, 1, 1, 1)
        self.E_valB = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valB.sizePolicy().hasHeightForWidth())
        self.E_valB.setSizePolicy(sizePolicy)
        self.E_valB.setMinimumSize(QtCore.QSize(50, 35))
        self.E_valB.setMaximumSize(QtCore.QSize(70, 24))
        self.E_valB.setBaseSize(QtCore.QSize(70, 20))
        self.E_valB.setStyleSheet(_fromUtf8(""))
        self.E_valB.setObjectName(_fromUtf8("E_valB"))
        self.gridLayout_5.addWidget(self.E_valB, 1, 5, 1, 1)
        self.E_valA = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valA.sizePolicy().hasHeightForWidth())
        self.E_valA.setSizePolicy(sizePolicy)
        self.E_valA.setMinimumSize(QtCore.QSize(50, 35))
        self.E_valA.setMaximumSize(QtCore.QSize(70, 24))
        self.E_valA.setBaseSize(QtCore.QSize(70, 20))
        self.E_valA.setStyleSheet(_fromUtf8(""))
        self.E_valA.setObjectName(_fromUtf8("E_valA"))
        self.gridLayout_5.addWidget(self.E_valA, 1, 4, 1, 1)
        self.E_srcA = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_srcA.sizePolicy().hasHeightForWidth())
        self.E_srcA.setSizePolicy(sizePolicy)
        self.E_srcA.setMinimumSize(QtCore.QSize(21, 35))
        self.E_srcA.setMaximumSize(QtCore.QSize(20, 24))
        self.E_srcA.setBaseSize(QtCore.QSize(70, 20))
        self.E_srcA.setStyleSheet(_fromUtf8(""))
        self.E_srcA.setObjectName(_fromUtf8("E_srcA"))
        self.gridLayout_5.addWidget(self.E_srcA, 1, 9, 1, 1)
        self.E_srcB = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_srcB.sizePolicy().hasHeightForWidth())
        self.E_srcB.setSizePolicy(sizePolicy)
        self.E_srcB.setMinimumSize(QtCore.QSize(21, 35))
        self.E_srcB.setMaximumSize(QtCore.QSize(20, 24))
        self.E_srcB.setBaseSize(QtCore.QSize(70, 20))
        self.E_srcB.setStyleSheet(_fromUtf8(""))
        self.E_srcB.setObjectName(_fromUtf8("E_srcB"))
        self.gridLayout_5.addWidget(self.E_srcB, 1, 10, 1, 1)
        self.label_33 = QtGui.QLabel(self.layoutWidget_3)
        self.label_33.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_5.addWidget(self.label_33, 0, 10, 1, 1)
        self.label_44 = QtGui.QLabel(self.layoutWidget_3)
        self.label_44.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_5.addWidget(self.label_44, 0, 0, 1, 1)
        self.E_stat = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_stat.sizePolicy().hasHeightForWidth())
        self.E_stat.setSizePolicy(sizePolicy)
        self.E_stat.setMinimumSize(QtCore.QSize(0, 35))
        self.E_stat.setMaximumSize(QtCore.QSize(40, 24))
        self.E_stat.setBaseSize(QtCore.QSize(70, 20))
        self.E_stat.setStyleSheet(_fromUtf8(""))
        self.E_stat.setObjectName(_fromUtf8("E_stat"))
        self.gridLayout_5.addWidget(self.E_stat, 1, 0, 1, 1)
        self.E_ifun = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_ifun.sizePolicy().hasHeightForWidth())
        self.E_ifun.setSizePolicy(sizePolicy)
        self.E_ifun.setMinimumSize(QtCore.QSize(20, 35))
        self.E_ifun.setMaximumSize(QtCore.QSize(20, 24))
        self.E_ifun.setBaseSize(QtCore.QSize(70, 20))
        self.E_ifun.setStyleSheet(_fromUtf8(""))
        self.E_ifun.setObjectName(_fromUtf8("E_ifun"))
        self.gridLayout_5.addWidget(self.E_ifun, 1, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.layoutWidget_3)
        self.label_28.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_5.addWidget(self.label_28, 0, 7, 1, 1)
        self.E_dstE = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_dstE.sizePolicy().hasHeightForWidth())
        self.E_dstE.setSizePolicy(sizePolicy)
        self.E_dstE.setMinimumSize(QtCore.QSize(20, 35))
        self.E_dstE.setMaximumSize(QtCore.QSize(20, 24))
        self.E_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.E_dstE.setStyleSheet(_fromUtf8(""))
        self.E_dstE.setObjectName(_fromUtf8("E_dstE"))
        self.gridLayout_5.addWidget(self.E_dstE, 1, 7, 1, 1)
        self.label_25 = QtGui.QLabel(self.layoutWidget_3)
        self.label_25.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_5.addWidget(self.label_25, 0, 8, 1, 1)
        self.E_valC = QtGui.QTextBrowser(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.E_valC.sizePolicy().hasHeightForWidth())
        self.E_valC.setSizePolicy(sizePolicy)
        self.E_valC.setMinimumSize(QtCore.QSize(50, 35))
        self.E_valC.setMaximumSize(QtCore.QSize(70, 24))
        self.E_valC.setBaseSize(QtCore.QSize(70, 20))
        self.E_valC.setStyleSheet(_fromUtf8(""))
        self.E_valC.setObjectName(_fromUtf8("E_valC"))
        self.gridLayout_5.addWidget(self.E_valC, 1, 3, 1, 1)
        self.layoutWidget_4 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget_4.setGeometry(QtCore.QRect(100, 420, 401, 70))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.D_valP = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_valP.sizePolicy().hasHeightForWidth())
        self.D_valP.setSizePolicy(sizePolicy)
        self.D_valP.setMinimumSize(QtCore.QSize(50, 35))
        self.D_valP.setMaximumSize(QtCore.QSize(70, 24))
        self.D_valP.setBaseSize(QtCore.QSize(70, 20))
        self.D_valP.setStyleSheet(_fromUtf8(""))
        self.D_valP.setObjectName(_fromUtf8("D_valP"))
        self.gridLayout_6.addWidget(self.D_valP, 1, 8, 1, 1)
        self.D_rA = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_rA.sizePolicy().hasHeightForWidth())
        self.D_rA.setSizePolicy(sizePolicy)
        self.D_rA.setMinimumSize(QtCore.QSize(21, 35))
        self.D_rA.setMaximumSize(QtCore.QSize(20, 24))
        self.D_rA.setBaseSize(QtCore.QSize(70, 20))
        self.D_rA.setStyleSheet(_fromUtf8(""))
        self.D_rA.setObjectName(_fromUtf8("D_rA"))
        self.gridLayout_6.addWidget(self.D_rA, 1, 4, 1, 1)
        self.D_rB = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_rB.sizePolicy().hasHeightForWidth())
        self.D_rB.setSizePolicy(sizePolicy)
        self.D_rB.setMinimumSize(QtCore.QSize(21, 35))
        self.D_rB.setMaximumSize(QtCore.QSize(20, 24))
        self.D_rB.setBaseSize(QtCore.QSize(70, 20))
        self.D_rB.setStyleSheet(_fromUtf8(""))
        self.D_rB.setObjectName(_fromUtf8("D_rB"))
        self.gridLayout_6.addWidget(self.D_rB, 1, 5, 1, 1)
        self.label_40 = QtGui.QLabel(self.layoutWidget_4)
        self.label_40.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_6.addWidget(self.label_40, 0, 5, 1, 1)
        self.label_36 = QtGui.QLabel(self.layoutWidget_4)
        self.label_36.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_6.addWidget(self.label_36, 0, 8, 1, 1)
        self.label_34 = QtGui.QLabel(self.layoutWidget_4)
        self.label_34.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_6.addWidget(self.label_34, 0, 1, 1, 1)
        self.label_39 = QtGui.QLabel(self.layoutWidget_4)
        self.label_39.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_6.addWidget(self.label_39, 0, 4, 1, 1)
        self.label_35 = QtGui.QLabel(self.layoutWidget_4)
        self.label_35.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_6.addWidget(self.label_35, 0, 7, 1, 1)
        self.D_icode = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_icode.sizePolicy().hasHeightForWidth())
        self.D_icode.setSizePolicy(sizePolicy)
        self.D_icode.setMinimumSize(QtCore.QSize(21, 35))
        self.D_icode.setMaximumSize(QtCore.QSize(20, 24))
        self.D_icode.setBaseSize(QtCore.QSize(70, 20))
        self.D_icode.setStyleSheet(_fromUtf8(""))
        self.D_icode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.D_icode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.D_icode.setObjectName(_fromUtf8("D_icode"))
        self.gridLayout_6.addWidget(self.D_icode, 1, 1, 1, 1)
        self.D_valC = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_valC.sizePolicy().hasHeightForWidth())
        self.D_valC.setSizePolicy(sizePolicy)
        self.D_valC.setMinimumSize(QtCore.QSize(50, 35))
        self.D_valC.setMaximumSize(QtCore.QSize(70, 24))
        self.D_valC.setBaseSize(QtCore.QSize(70, 20))
        self.D_valC.setStyleSheet(_fromUtf8(""))
        self.D_valC.setObjectName(_fromUtf8("D_valC"))
        self.gridLayout_6.addWidget(self.D_valC, 1, 7, 1, 1)
        self.label_38 = QtGui.QLabel(self.layoutWidget_4)
        self.label_38.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_6.addWidget(self.label_38, 0, 2, 1, 1)
        self.label_45 = QtGui.QLabel(self.layoutWidget_4)
        self.label_45.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_6.addWidget(self.label_45, 0, 0, 1, 1)
        self.D_ifun = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_ifun.sizePolicy().hasHeightForWidth())
        self.D_ifun.setSizePolicy(sizePolicy)
        self.D_ifun.setMinimumSize(QtCore.QSize(21, 35))
        self.D_ifun.setMaximumSize(QtCore.QSize(20, 24))
        self.D_ifun.setBaseSize(QtCore.QSize(70, 20))
        self.D_ifun.setStyleSheet(_fromUtf8(""))
        self.D_ifun.setObjectName(_fromUtf8("D_ifun"))
        self.gridLayout_6.addWidget(self.D_ifun, 1, 2, 1, 1)
        self.D_stat = QtGui.QTextBrowser(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.D_stat.sizePolicy().hasHeightForWidth())
        self.D_stat.setSizePolicy(sizePolicy)
        self.D_stat.setMinimumSize(QtCore.QSize(0, 35))
        self.D_stat.setMaximumSize(QtCore.QSize(40, 24))
        self.D_stat.setBaseSize(QtCore.QSize(70, 20))
        self.D_stat.setStyleSheet(_fromUtf8(""))
        self.D_stat.setObjectName(_fromUtf8("D_stat"))
        self.gridLayout_6.addWidget(self.D_stat, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(18, 32, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(18, 32, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 6, 1, 1)
        self.layoutWidget_5 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget_5.setGeometry(QtCore.QRect(100, 510, 473, 41))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.layoutWidget_5)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_43 = QtGui.QLabel(self.layoutWidget_5)
        self.label_43.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_7.addWidget(self.label_43, 0, 2, 1, 1)
        self.label_46 = QtGui.QLabel(self.layoutWidget_5)
        self.label_46.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_7.addWidget(self.label_46, 0, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.layoutWidget_5)
        self.label_23.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_7.addWidget(self.label_23, 0, 4, 1, 1)
        self.F_stat = QtGui.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.F_stat.sizePolicy().hasHeightForWidth())
        self.F_stat.setSizePolicy(sizePolicy)
        self.F_stat.setMinimumSize(QtCore.QSize(0, 35))
        self.F_stat.setMaximumSize(QtCore.QSize(40, 24))
        self.F_stat.setBaseSize(QtCore.QSize(70, 20))
        self.F_stat.setStyleSheet(_fromUtf8(""))
        self.F_stat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.F_stat.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.F_stat.setObjectName(_fromUtf8("F_stat"))
        self.gridLayout_7.addWidget(self.F_stat, 0, 1, 1, 1)
        self.F_predPC = QtGui.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.F_predPC.sizePolicy().hasHeightForWidth())
        self.F_predPC.setSizePolicy(sizePolicy)
        self.F_predPC.setMinimumSize(QtCore.QSize(70, 35))
        self.F_predPC.setMaximumSize(QtCore.QSize(70, 24))
        self.F_predPC.setBaseSize(QtCore.QSize(70, 20))
        self.F_predPC.setStyleSheet(_fromUtf8(""))
        self.F_predPC.setObjectName(_fromUtf8("F_predPC"))
        self.gridLayout_7.addWidget(self.F_predPC, 0, 3, 1, 1)
        self.ZF = QtGui.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.ZF.sizePolicy().hasHeightForWidth())
        self.ZF.setSizePolicy(sizePolicy)
        self.ZF.setMinimumSize(QtCore.QSize(20, 35))
        self.ZF.setMaximumSize(QtCore.QSize(20, 24))
        self.ZF.setBaseSize(QtCore.QSize(70, 20))
        self.ZF.setStyleSheet(_fromUtf8(""))
        self.ZF.setObjectName(_fromUtf8("ZF"))
        self.gridLayout_7.addWidget(self.ZF, 0, 5, 1, 1)
        self.OF = QtGui.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.OF.sizePolicy().hasHeightForWidth())
        self.OF.setSizePolicy(sizePolicy)
        self.OF.setMinimumSize(QtCore.QSize(20, 35))
        self.OF.setMaximumSize(QtCore.QSize(20, 24))
        self.OF.setBaseSize(QtCore.QSize(70, 20))
        self.OF.setStyleSheet(_fromUtf8(""))
        self.OF.setObjectName(_fromUtf8("OF"))
        self.gridLayout_7.addWidget(self.OF, 0, 9, 1, 1)
        self.label_24 = QtGui.QLabel(self.layoutWidget_5)
        self.label_24.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_7.addWidget(self.label_24, 0, 6, 1, 1)
        self.SF = QtGui.QTextBrowser(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.SF.sizePolicy().hasHeightForWidth())
        self.SF.setSizePolicy(sizePolicy)
        self.SF.setMinimumSize(QtCore.QSize(20, 35))
        self.SF.setMaximumSize(QtCore.QSize(20, 24))
        self.SF.setBaseSize(QtCore.QSize(70, 20))
        self.SF.setStyleSheet(_fromUtf8(""))
        self.SF.setObjectName(_fromUtf8("SF"))
        self.gridLayout_7.addWidget(self.SF, 0, 7, 1, 1)
        self.label_37 = QtGui.QLabel(self.layoutWidget_5)
        self.label_37.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_7.addWidget(self.label_37, 0, 8, 1, 1)
        self.loadButton = QtGui.QPushButton(Y86Simulator)
        self.loadButton.setGeometry(QtCore.QRect(570, 60, 61, 31))
        self.loadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.loadButton.setText(_fromUtf8(""))
        self.loadButton.setDefault(False)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.frequency = QtGui.QLineEdit(Y86Simulator)
        self.frequency.setGeometry(QtCore.QRect(750, 150, 61, 21))
        self.frequency.setStyleSheet(_fromUtf8("border:white;\n"
"background:white;\n"
"font: 75 22pt \"Chiller\";\n"
""))
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.saveButton = QtGui.QPushButton(Y86Simulator)
        self.saveButton.setGeometry(QtCore.QRect(560, 100, 61, 31))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.cycle = QtGui.QLineEdit(Y86Simulator)
        self.cycle.setGeometry(QtCore.QRect(830, 150, 41, 21))
        self.cycle.setStyleSheet(_fromUtf8("border:white;\n"
"background:rgb(255, 255, 255,0);\n"
"font: 75 22pt \"Chiller\";\n"
""))
        self.cycle.setObjectName(_fromUtf8("cycle"))
        self.layoutWidget = QtGui.QWidget(Y86Simulator)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 240, 401, 70))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 4, 1, 1)
        self.M_valE = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_valE.sizePolicy().hasHeightForWidth())
        self.M_valE.setSizePolicy(sizePolicy)
        self.M_valE.setMinimumSize(QtCore.QSize(50, 35))
        self.M_valE.setMaximumSize(QtCore.QSize(70, 24))
        self.M_valE.setBaseSize(QtCore.QSize(70, 20))
        self.M_valE.setStyleSheet(_fromUtf8(""))
        self.M_valE.setObjectName(_fromUtf8("M_valE"))
        self.gridLayout_3.addWidget(self.M_valE, 1, 4, 1, 1)
        self.label_15 = QtGui.QLabel(self.layoutWidget)
        self.label_15.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 0, 8, 1, 1)
        self.M_valA = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_valA.sizePolicy().hasHeightForWidth())
        self.M_valA.setSizePolicy(sizePolicy)
        self.M_valA.setMinimumSize(QtCore.QSize(50, 35))
        self.M_valA.setMaximumSize(QtCore.QSize(70, 24))
        self.M_valA.setBaseSize(QtCore.QSize(70, 20))
        self.M_valA.setStyleSheet(_fromUtf8(""))
        self.M_valA.setObjectName(_fromUtf8("M_valA"))
        self.gridLayout_3.addWidget(self.M_valA, 1, 5, 1, 1)
        self.label_17 = QtGui.QLabel(self.layoutWidget)
        self.label_17.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 0, 5, 1, 1)
        self.M_dstE = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_dstE.sizePolicy().hasHeightForWidth())
        self.M_dstE.setSizePolicy(sizePolicy)
        self.M_dstE.setMinimumSize(QtCore.QSize(20, 35))
        self.M_dstE.setMaximumSize(QtCore.QSize(20, 24))
        self.M_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.M_dstE.setStyleSheet(_fromUtf8(""))
        self.M_dstE.setObjectName(_fromUtf8("M_dstE"))
        self.gridLayout_3.addWidget(self.M_dstE, 1, 7, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 7, 1, 1)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.M_bch = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_bch.sizePolicy().hasHeightForWidth())
        self.M_bch.setSizePolicy(sizePolicy)
        self.M_bch.setMinimumSize(QtCore.QSize(20, 35))
        self.M_bch.setMaximumSize(QtCore.QSize(20, 24))
        self.M_bch.setBaseSize(QtCore.QSize(70, 20))
        self.M_bch.setStyleSheet(_fromUtf8(""))
        self.M_bch.setObjectName(_fromUtf8("M_bch"))
        self.gridLayout_3.addWidget(self.M_bch, 1, 2, 1, 1)
        self.M_dstM = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_dstM.sizePolicy().hasHeightForWidth())
        self.M_dstM.setSizePolicy(sizePolicy)
        self.M_dstM.setMinimumSize(QtCore.QSize(20, 35))
        self.M_dstM.setMaximumSize(QtCore.QSize(20, 24))
        self.M_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.M_dstM.setStyleSheet(_fromUtf8(""))
        self.M_dstM.setObjectName(_fromUtf8("M_dstM"))
        self.gridLayout_3.addWidget(self.M_dstM, 1, 8, 1, 1)
        self.M_icode = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_icode.sizePolicy().hasHeightForWidth())
        self.M_icode.setSizePolicy(sizePolicy)
        self.M_icode.setMinimumSize(QtCore.QSize(20, 35))
        self.M_icode.setMaximumSize(QtCore.QSize(20, 24))
        self.M_icode.setBaseSize(QtCore.QSize(70, 20))
        self.M_icode.setStyleSheet(_fromUtf8(""))
        self.M_icode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.M_icode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.M_icode.setObjectName(_fromUtf8("M_icode"))
        self.gridLayout_3.addWidget(self.M_icode, 1, 1, 1, 1)
        self.label_42 = QtGui.QLabel(self.layoutWidget)
        self.label_42.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_3.addWidget(self.label_42, 0, 0, 1, 1)
        self.M_stat = QtGui.QTextBrowser(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.M_stat.sizePolicy().hasHeightForWidth())
        self.M_stat.setSizePolicy(sizePolicy)
        self.M_stat.setMinimumSize(QtCore.QSize(0, 35))
        self.M_stat.setMaximumSize(QtCore.QSize(40, 24))
        self.M_stat.setBaseSize(QtCore.QSize(70, 20))
        self.M_stat.setStyleSheet(_fromUtf8(""))
        self.M_stat.setObjectName(_fromUtf8("M_stat"))
        self.gridLayout_3.addWidget(self.M_stat, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(18, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(13, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 6, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 150, 404, 71))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.W_valM = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_valM.sizePolicy().hasHeightForWidth())
        self.W_valM.setSizePolicy(sizePolicy)
        self.W_valM.setMinimumSize(QtCore.QSize(70, 35))
        self.W_valM.setMaximumSize(QtCore.QSize(70, 24))
        self.W_valM.setBaseSize(QtCore.QSize(70, 20))
        self.W_valM.setStyleSheet(_fromUtf8(""))
        self.W_valM.setObjectName(_fromUtf8("W_valM"))
        self.gridLayout.addWidget(self.W_valM, 1, 4, 1, 1)
        self.W_valE = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_valE.sizePolicy().hasHeightForWidth())
        self.W_valE.setSizePolicy(sizePolicy)
        self.W_valE.setMinimumSize(QtCore.QSize(70, 35))
        self.W_valE.setMaximumSize(QtCore.QSize(70, 35))
        self.W_valE.setBaseSize(QtCore.QSize(70, 20))
        self.W_valE.setStyleSheet(_fromUtf8(""))
        self.W_valE.setObjectName(_fromUtf8("W_valE"))
        self.gridLayout.addWidget(self.W_valE, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 7, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.W_dstM = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.W_dstM.sizePolicy().hasHeightForWidth())
        self.W_dstM.setSizePolicy(sizePolicy)
        self.W_dstM.setMinimumSize(QtCore.QSize(20, 35))
        self.W_dstM.setMaximumSize(QtCore.QSize(20, 24))
        self.W_dstM.setBaseSize(QtCore.QSize(70, 20))
        self.W_dstM.setStyleSheet(_fromUtf8(""))
        self.W_dstM.setObjectName(_fromUtf8("W_dstM"))
        self.gridLayout.addWidget(self.W_dstM, 1, 7, 1, 1)
        self.W_dstE = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.W_dstE.sizePolicy().hasHeightForWidth())
        self.W_dstE.setSizePolicy(sizePolicy)
        self.W_dstE.setMinimumSize(QtCore.QSize(20, 35))
        self.W_dstE.setMaximumSize(QtCore.QSize(20, 24))
        self.W_dstE.setBaseSize(QtCore.QSize(70, 20))
        self.W_dstE.setStyleSheet(_fromUtf8(""))
        self.W_dstE.setObjectName(_fromUtf8("W_dstE"))
        self.gridLayout.addWidget(self.W_dstE, 1, 6, 1, 1)
        self.label_41 = QtGui.QLabel(self.layoutWidget1)
        self.label_41.setStyleSheet(_fromUtf8("QLabel\n"
"{\n"
"font: 18pt \"Chiller\";\n"
"}"))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout.addWidget(self.label_41, 0, 0, 1, 1)
        self.W_stat = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.W_stat.sizePolicy().hasHeightForWidth())
        self.W_stat.setSizePolicy(sizePolicy)
        self.W_stat.setMinimumSize(QtCore.QSize(0, 35))
        self.W_stat.setMaximumSize(QtCore.QSize(40, 35))
        self.W_stat.setBaseSize(QtCore.QSize(70, 20))
        self.W_stat.setStyleSheet(_fromUtf8(""))
        self.W_stat.setObjectName(_fromUtf8("W_stat"))
        self.gridLayout.addWidget(self.W_stat, 1, 0, 1, 1)
        self.W_icode = QtGui.QTextBrowser(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(35)
        sizePolicy.setHeightForWidth(self.W_icode.sizePolicy().hasHeightForWidth())
        self.W_icode.setSizePolicy(sizePolicy)
        self.W_icode.setMinimumSize(QtCore.QSize(0, 35))
        self.W_icode.setMaximumSize(QtCore.QSize(20, 45))
        self.W_icode.setBaseSize(QtCore.QSize(70, 20))
        self.W_icode.setStyleSheet(_fromUtf8(""))
        self.W_icode.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.W_icode.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.W_icode.setObjectName(_fromUtf8("W_icode"))
        self.gridLayout.addWidget(self.W_icode, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(38, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.runButton = QtGui.QPushButton(Y86Simulator)
        self.runButton.setEnabled(True)
        self.runButton.setGeometry(QtCore.QRect(90, 80, 71, 41))
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.runButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.runButton.setText(_fromUtf8(""))
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.pauseButton = QtGui.QPushButton(Y86Simulator)
        self.pauseButton.setGeometry(QtCore.QRect(170, 80, 71, 41))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.pauseButton.setText(_fromUtf8(""))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.stepButton = QtGui.QPushButton(Y86Simulator)
        self.stepButton.setGeometry(QtCore.QRect(260, 80, 71, 41))
        self.stepButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stepButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.stepButton.setText(_fromUtf8(""))
        self.stepButton.setObjectName(_fromUtf8("stepButton"))
        self.backButton = QtGui.QPushButton(Y86Simulator)
        self.backButton.setGeometry(QtCore.QRect(340, 80, 71, 41))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.backButton.setText(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.resetButton = QtGui.QPushButton(Y86Simulator)
        self.resetButton.setGeometry(QtCore.QRect(430, 80, 71, 41))
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setStyleSheet(_fromUtf8("\n"
"QPushButton {\n"
"    selection-color: none;\n"
"    background-color:none;\n"
"    border-color:rgb(0, 0, 0);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 255, 255,50);\n"
"    \"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(222,222,222,10%), stop:1 rgb(222,222,222,20%));\"\n"
"}\n"
"\n"
"QPushButton:pressed,QPushButton:on {\n"
"    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,0,0,18%), stop:1 rgb(0,0,0,25%));\n"
"}\n"
""))
        self.resetButton.setText(_fromUtf8(""))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.loadAdd = QtGui.QTextBrowser(Y86Simulator)
        self.loadAdd.setGeometry(QtCore.QRect(650, 60, 251, 31))
        self.loadAdd.setStyleSheet(_fromUtf8("font: 15pt \"Chiller\";"))
        self.loadAdd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loadAdd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loadAdd.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.loadAdd.setObjectName(_fromUtf8("loadAdd"))
        self.saveAdd = QtGui.QTextBrowser(Y86Simulator)
        self.saveAdd.setGeometry(QtCore.QRect(650, 103, 251, 31))
        self.saveAdd.setStyleSheet(_fromUtf8("font: 15pt \"Chiller\";"))
        self.saveAdd.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.saveAdd.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.saveAdd.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.saveAdd.setObjectName(_fromUtf8("saveAdd"))
        self.label = QtGui.QLabel(Y86Simulator)
        self.label.setGeometry(QtCore.QRect(660, 643, 261, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 18pt \"Chiller\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget2 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget2.setGeometry(QtCore.QRect(390, 560, 101, 120))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.esp = QtGui.QLineEdit(self.layoutWidget2)
        self.esp.setObjectName(_fromUtf8("esp"))
        self.verticalLayout_2.addWidget(self.esp)
        self.ebp = QtGui.QLineEdit(self.layoutWidget2)
        self.ebp.setObjectName(_fromUtf8("ebp"))
        self.verticalLayout_2.addWidget(self.ebp)
        self.esi = QtGui.QLineEdit(self.layoutWidget2)
        self.esi.setObjectName(_fromUtf8("esi"))
        self.verticalLayout_2.addWidget(self.esi)
        self.edi = QtGui.QLineEdit(self.layoutWidget2)
        self.edi.setObjectName(_fromUtf8("edi"))
        self.verticalLayout_2.addWidget(self.edi)
        self.layoutWidget3 = QtGui.QWidget(Y86Simulator)
        self.layoutWidget3.setGeometry(QtCore.QRect(210, 558, 101, 120))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.eax = QtGui.QLineEdit(self.layoutWidget3)
        self.eax.setObjectName(_fromUtf8("eax"))
        self.verticalLayout.addWidget(self.eax)
        self.ecx = QtGui.QLineEdit(self.layoutWidget3)
        self.ecx.setObjectName(_fromUtf8("ecx"))
        self.verticalLayout.addWidget(self.ecx)
        self.edx = QtGui.QLineEdit(self.layoutWidget3)
        self.edx.setObjectName(_fromUtf8("edx"))
        self.verticalLayout.addWidget(self.edx)
        self.ebx = QtGui.QLineEdit(self.layoutWidget3)
        self.ebx.setObjectName(_fromUtf8("ebx"))
        self.verticalLayout.addWidget(self.ebx)
        self.Tab = QtGui.QTabWidget(Y86Simulator)
        self.Tab.setEnabled(True)
        self.Tab.setGeometry(QtCore.QRect(580, 420, 341, 211))
        self.Tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tab.setStyleSheet(_fromUtf8("\n"
"QTabWidget::tab-bar {\n"
"border:rgb(243, 221, 255,0);\n"
"background:rgb(0,0,0,0%);\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"border:rgb(243, 221, 255,0);\n"
"  background:rgb(0,0,0,0%);\n"
"  color: rgb(0,0,0,0%);\n"
"  padding: 16px;\n"
"  width: 20ex;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background:rgb(0,0,0,0%);\n"
" }\n"
"\n"
"QTabWidget::pane { \n"
"border:rgb(243, 221, 255,0);\n"
"background:rgb(0,0,0,0%);\n"
"background-color:rgb(0,0,0,0%);\n"
"}\n"
""))
        self.Tab.setTabPosition(QtGui.QTabWidget.North)
        self.Tab.setTabShape(QtGui.QTabWidget.Rounded)
        self.Tab.setIconSize(QtCore.QSize(30, 20))
        self.Tab.setObjectName(_fromUtf8("Tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.Memory = QtGui.QTextBrowser(self.tab)
        self.Memory.setGeometry(QtCore.QRect(0, 0, 351, 171))
        self.Memory.setStyleSheet(_fromUtf8("background:rgb(0,0,0,0%);\n"
"background-color:rgb(0,0,0,0%);\n"
"font: 15px;\n"
"font: 9pt \"å®‹ä½“\";"))
        self.Memory.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Memory.setObjectName(_fromUtf8("Memory"))
        self.Tab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Cache = QtGui.QTextBrowser(self.tab_2)
        self.Cache.setGeometry(QtCore.QRect(0, 0, 341, 161))
        self.Cache.setStyleSheet(_fromUtf8("font: 9px;\n"
"font: 9pt \"å®‹ä½“\";"))
        self.Cache.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Cache.setObjectName(_fromUtf8("Cache"))
        self.Tab.addTab(self.tab_2, _fromUtf8(""))
        self.Code = QtGui.QTextBrowser(Y86Simulator)
        self.Code.setGeometry(QtCore.QRect(560, 211, 361, 181))
        self.Code.setStyleSheet(_fromUtf8("font: 9pt \"å®‹ä½“\";\n"
"font: 12px;"))
        self.Code.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.Code.setObjectName(_fromUtf8("Code"))

        self.retranslateUi(Y86Simulator)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Y86Simulator)

    def retranslateUi(self, Y86Simulator):
        Y86Simulator.setWindowTitle(_translate("Y86Simulator", "Y86 Simulator", None))
        self.label_27.setText(_translate("Y86Simulator", "valB", None))
        self.label_32.setText(_translate("Y86Simulator", "srcA", None))
        self.label_31.setText(_translate("Y86Simulator", "valA", None))
        self.label_30.setText(_translate("Y86Simulator", "valC", None))
        self.label_26.setText(_translate("Y86Simulator", "iFun", None))
        self.label_29.setText(_translate("Y86Simulator", "iCode", None))
        self.label_33.setText(_translate("Y86Simulator", "srcB", None))
        self.label_44.setText(_translate("Y86Simulator", "E_stat", None))
        self.label_28.setText(_translate("Y86Simulator", "dstE", None))
        self.label_25.setText(_translate("Y86Simulator", "dstM", None))
        self.label_40.setText(_translate("Y86Simulator", "rB", None))
        self.label_36.setText(_translate("Y86Simulator", "valP", None))
        self.label_34.setText(_translate("Y86Simulator", "iCode", None))
        self.label_39.setText(_translate("Y86Simulator", "rA", None))
        self.label_35.setText(_translate("Y86Simulator", "valC", None))
        self.label_38.setText(_translate("Y86Simulator", "iFun", None))
        self.label_45.setText(_translate("Y86Simulator", "D_stat", None))
        self.label_43.setText(_translate("Y86Simulator", "predPC", None))
        self.label_46.setText(_translate("Y86Simulator", "F_stat", None))
        self.label_23.setText(_translate("Y86Simulator", "ZF", None))
        self.label_24.setText(_translate("Y86Simulator", "SF", None))
        self.label_37.setText(_translate("Y86Simulator", "OF", None))
        self.label_16.setText(_translate("Y86Simulator", "valE", None))
        self.label_15.setText(_translate("Y86Simulator", "dstM", None))
        self.label_17.setText(_translate("Y86Simulator", "Bch", None))
        self.label_12.setText(_translate("Y86Simulator", "valA", None))
        self.label_14.setText(_translate("Y86Simulator", "dstE", None))
        self.label_13.setText(_translate("Y86Simulator", "iCode", None))
        self.label_42.setText(_translate("Y86Simulator", "M_stat", None))
        self.label_2.setText(_translate("Y86Simulator", "iCode", None))
        self.label_4.setText(_translate("Y86Simulator", "valM", None))
        self.label_5.setText(_translate("Y86Simulator", "dstE", None))
        self.label_6.setText(_translate("Y86Simulator", "dstM", None))
        self.label_3.setText(_translate("Y86Simulator", "valE", None))
        self.label_41.setText(_translate("Y86Simulator", "W_stat", None))
        self.label.setText(_translate("Y86Simulator", "Published by: CatMiaoMiaoMiao", None))
        self.Tab.setTabText(self.Tab.indexOf(self.tab), _translate("Y86Simulator", "Tab 1", None))
        self.Tab.setTabText(self.Tab.indexOf(self.tab_2), _translate("Y86Simulator", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Y86Simulator = QtGui.QDialog()
    ui = Ui_Y86Simulator()
    ui.setupUi(Y86Simulator)
    Y86Simulator.show()
    sys.exit(app.exec_())

