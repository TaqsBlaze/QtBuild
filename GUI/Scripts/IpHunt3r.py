# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admire.BLAZE.000\Desktop\QT\iphunter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IpHunt3r(object):
    def setupUi(self, IpHunt3r):
        IpHunt3r.setObjectName("IpHunt3r")
        IpHunt3r.resize(754, 654)
        IpHunt3r.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        IpHunt3r.setAcceptDrops(True)
        IpHunt3r.setFrameShape(QtWidgets.QFrame.Box)
        IpHunt3r.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lineEdit = QtWidgets.QLineEdit(IpHunt3r)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam")
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setFrame(False)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(IpHunt3r)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 71))
        font = QtGui.QFont()
        font.setFamily("Trench")
        font.setPointSize(33)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(0)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 0 33pt \"Trench\";\n"
"text-decoration: underline;\n"
"background-color: rgb(184, 10, 10);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(5)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(IpHunt3r)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 401, 121))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(IpHunt3r)
        self.pushButton.setGeometry(QtCore.QRect(410, 220, 71, 21))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(IpHunt3r)
        self.frame.setGeometry(QtCore.QRect(20, 270, 701, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 681, 341))
        self.scrollArea.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"color: rgb(0, 188, 0);\n"
"font: 14pt \"Gautami\";")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(660, 0, 16, 331))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(IpHunt3r)
        QtCore.QMetaObject.connectSlotsByName(IpHunt3r)

    def retranslateUi(self, IpHunt3r):
        _translate = QtCore.QCoreApplication.translate
        IpHunt3r.setWindowTitle(_translate("IpHunt3r", "IpHunt3r"))
        self.lineEdit.setPlaceholderText(_translate("IpHunt3r", "IP"))
        self.label.setText(_translate("IpHunt3r", "IP Hunt3r"))
        self.label_2.setText(_translate("IpHunt3r", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">IP HUNT3R</span></p><p><span style=\" color:#90ee90;\">Version 1.0</span></p><p><span style=\" color:#ffa500;\">Developed by TaqsBlaz3</span></p><p align=\"justify\" style=\'color:white\'>Ip hunter is a network tool for guthering information</p><p align=\"justify\" style=\'color:white\'>on targeted Ip address</p></body></html>"))
        self.pushButton.setText(_translate("IpHunt3r", "Hunt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IpHunt3r = QtWidgets.QFrame()
    ui = Ui_IpHunt3r()
    ui.setupUi(IpHunt3r)
    IpHunt3r.show()
    sys.exit(app.exec_())
