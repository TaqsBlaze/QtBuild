# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qtmodern.styles import dark,light
from qtmodern.windows import ModernWindow


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(690, 491)
        Frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(30, 60, 411, 31))
        self.label.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.Autodownload_checkBox = QtWidgets.QCheckBox(Frame)
        self.Autodownload_checkBox.setGeometry(QtCore.QRect(70, 110, 141, 31))
        self.Autodownload_checkBox.setObjectName("Autodownload_checkBox")
        self.Autocheck_checkBox = QtWidgets.QCheckBox(Frame)
        self.Autocheck_checkBox.setGeometry(QtCore.QRect(70, 140, 131, 17))
        self.Autocheck_checkBox.setObjectName("Autocheck_checkBox")
        self.AutoInstall_checkBox = QtWidgets.QCheckBox(Frame)
        self.AutoInstall_checkBox.setGeometry(QtCore.QRect(70, 160, 131, 17))
        self.AutoInstall_checkBox.setObjectName("AutoInstall_checkBox")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 411, 31))
        self.label_2.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.UI_setting_entry = QtWidgets.QLineEdit(Frame)
        self.UI_setting_entry.setGeometry(QtCore.QRect(70, 290, 331, 31))
        self.UI_setting_entry.setText("")
        self.UI_setting_entry.setClearButtonEnabled(True)
        self.UI_setting_entry.setObjectName("UI_setting_entry")
        self.Script_setting_entry = QtWidgets.QLineEdit(Frame)
        self.Script_setting_entry.setGeometry(QtCore.QRect(70, 370, 331, 31))
        self.Script_setting_entry.setText("")
        self.Script_setting_entry.setClearButtonEnabled(True)
        self.Script_setting_entry.setObjectName("Script_setting_entry")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 440, 111, 31))
        self.pushButton.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(179, 179, 179);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 331, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(60, 340, 331, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(0, 190, 691, 20))
        self.label_5.setStyleSheet("background-color: transparent;")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Settings"))
        self.label.setText(_translate("Frame", "<html><head/><body><p>\n"
"<div style=\"margin-left:12px;\">\n"
"<span style=\" font-size:15pt; font-weight:15;font-family:trench;\">Auto update settings</span></p>\n"
"</div>\n"
"</body></html>"))
        self.Autodownload_checkBox.setText(_translate("Frame", "Auto download updates"))
        self.Autocheck_checkBox.setText(_translate("Frame", "Auto check for updates"))
        self.AutoInstall_checkBox.setText(_translate("Frame", "Install updated"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p>\n"
"<div style=\"margin-left:12px;\">\n"
"<span style=\" font-size:15pt; font-weight:15;font-family:trench;\">Directory settings</span></p>\n"
"</div>\n"
"</body></html>"))
        self.UI_setting_entry.setPlaceholderText(_translate("Frame", "UI file directory"))
        self.Script_setting_entry.setPlaceholderText(_translate("Frame", "Script file directory"))
        self.pushButton.setText(_translate("Frame", "Save"))
        self.label_3.setText(_translate("Frame", "Set default locations to search for UI files"))
        self.label_4.setText(_translate("Frame", "Set default locations to save script files"))
        self.label_5.setText(_translate("Frame", "<hr>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    light(app)
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
