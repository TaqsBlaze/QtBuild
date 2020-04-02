# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admire.BLAZE.000\Desktop\QT\QtBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtBuilder(object):
    def setupUi(self, QtBuilder):
        QtBuilder.setObjectName("QtBuilder")
        QtBuilder.setWindowModality(QtCore.Qt.ApplicationModal)
        QtBuilder.resize(669, 444)
        self.centralwidget = QtWidgets.QWidget(QtBuilder)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Trench")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgba(85, 255, 0,1);\n"
"color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 70, 561, 301))
        self.frame.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.UIEntry = QtWidgets.QLineEdit(self.frame)
        self.UIEntry.setGeometry(QtCore.QRect(10, 50, 381, 31))
        self.UIEntry.setObjectName("UIEntry")
        self.OutputEntry = QtWidgets.QLineEdit(self.frame)
        self.OutputEntry.setGeometry(QtCore.QRect(10, 110, 381, 31))
        self.OutputEntry.setObjectName("OutputEntry")
        self.Notifs = QtWidgets.QLabel(self.frame)
        self.Notifs.setGeometry(QtCore.QRect(0, 270, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Trench")
        font.setPointSize(14)
        self.Notifs.setFont(font)
        self.Notifs.setText("")
        self.Notifs.setObjectName("Notifs")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:0px;\n"
"border-radius:4px;")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(510, 280, 41, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 380, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        QtBuilder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QtBuilder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        QtBuilder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QtBuilder)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        self.statusbar.setFont(font)
        self.statusbar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.statusbar.setObjectName("statusbar")
        QtBuilder.setStatusBar(self.statusbar)
        self.actionQt_Builder = QtWidgets.QAction(QtBuilder)
        self.actionQt_Builder.setObjectName("actionQt_Builder")
        self.actionDeveloper = QtWidgets.QAction(QtBuilder)
        self.actionDeveloper.setObjectName("actionDeveloper")
        self.actionChange_log = QtWidgets.QAction(QtBuilder)
        self.actionChange_log.setObjectName("actionChange_log")
        self.menuAbout.addAction(self.actionQt_Builder)
        self.menuAbout.addAction(self.actionChange_log)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(QtBuilder)
        QtCore.QMetaObject.connectSlotsByName(QtBuilder)

    def retranslateUi(self, QtBuilder):
        _translate = QtCore.QCoreApplication.translate
        QtBuilder.setWindowTitle(_translate("QtBuilder", "MainWindow"))
        self.label.setText(_translate("QtBuilder", "Qt Builder"))
        self.UIEntry.setPlaceholderText(_translate("QtBuilder", "UI source file"))
        self.OutputEntry.setPlaceholderText(_translate("QtBuilder", "Out put script Name"))
        self.pushButton.setText(_translate("QtBuilder", "Build"))
        self.checkBox.setText(_translate("QtBuilder", "Dark"))
        self.label_2.setText(_translate("QtBuilder", "Version 1.0.2"))
        self.menuAbout.setTitle(_translate("QtBuilder", "About"))
        self.actionQt_Builder.setText(_translate("QtBuilder", "Qt Builder"))
        self.actionDeveloper.setText(_translate("QtBuilder", "Developer"))
        self.actionChange_log.setText(_translate("QtBuilder", "Change log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtBuilder = QtWidgets.QMainWindow()
    ui = Ui_QtBuilder()
    ui.setupUi(QtBuilder)
    QtBuilder.show()
    sys.exit(app.exec_())
