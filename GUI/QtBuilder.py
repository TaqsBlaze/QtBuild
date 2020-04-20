# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from qtmodern.styles import dark,light
from qtmodern.windows import ModernWindow
import os
import subprocess

class Ui_QtBuilder(object):
    def setupUi(self, QtBuilder):
        QtBuilder.setObjectName("QtBuilder")
        QtBuilder.setWindowModality(QtCore.Qt.ApplicationModal)
        QtBuilder.resize(742, 650)
        QtBuilder.setMinimumSize(QtCore.QSize(742, 650))
        QtBuilder.setMaximumSize(QtCore.QSize(742, 650))
        self.version_string = "1.1.3"
        self.centralwidget = QtWidgets.QWidget(QtBuilder)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 61))
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
        self.frame.setGeometry(QtCore.QRect(20, 70, 701, 511))
        self.frame.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.UIEntry = QtWidgets.QLineEdit(self.frame)
        self.UIEntry.setGeometry(QtCore.QRect(30, 100, 441, 31))
        self.UIEntry.setObjectName("UIEntry")
        self.OutputEntry = QtWidgets.QLineEdit(self.frame)
        self.OutputEntry.setGeometry(QtCore.QRect(30, 160, 441, 31))
        self.OutputEntry.setObjectName("OutputEntry")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 290, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Trench")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:0px;\n"
"border-radius:4px;")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(30, 220, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 220, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(80, 350, 551, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.Update_notifs = QtWidgets.QLabel(self.frame_2)
        self.Update_notifs.setGeometry(QtCore.QRect(10, 35, 200, 90))
        self.Update_notifs.setMaximumSize(QtCore.QSize(1000, 1000))
        self.Update_notifs.setText("")
        self.Update_notifs.setObjectName("Update_notifs")
        self.Notifs = QtWidgets.QLabel(self.frame_2)
        self.Notifs.setGeometry(QtCore.QRect(10, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Trench")
        font.setPointSize(14)
        self.Notifs.setFont(font)
        self.Notifs.setText("")
        self.Notifs.setObjectName("Notifs")
        self.version_label = QtWidgets.QLabel(self.frame)
        self.version_label.setGeometry(QtCore.QRect(600, 480, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setText(f"{self.version_string}")
        self.version_label.setObjectName("version_label")
        QtBuilder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QtBuilder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
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
        self.actionUpdate = QtWidgets.QAction(QtBuilder)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuAbout.addAction(self.actionQt_Builder)
        self.menuAbout.addAction(self.actionChange_log)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(QtBuilder)
        self.actionQt_Builder.triggered.connect(QtBuilder.show)
        QtCore.QMetaObject.connectSlotsByName(QtBuilder)
        self.pushButton.clicked.connect(self.build)
    def retranslateUi(self, QtBuilder):
        _translate = QtCore.QCoreApplication.translate
        QtBuilder.setWindowTitle(_translate("QtBuilder", "QtBuilder"))
        self.label.setText(_translate("QtBuilder", "Qt Builder"))
        self.UIEntry.setPlaceholderText(_translate("QtBuilder", "UI source file"))
        self.OutputEntry.setPlaceholderText(_translate("QtBuilder", "Out put script Name"))
        self.pushButton.setText(_translate("QtBuilder", "Build"))
        self.comboBox.setItemText(0, _translate("QtBuilder", "Default folder"))
        self.comboBox.setItemText(1, _translate("QtBuilder", "Custom folder"))
        self.lineEdit.setPlaceholderText(_translate("QtBuilder", "Custom folder"))
        self.menuAbout.setTitle(_translate("QtBuilder", "About"))
        self.actionQt_Builder.setText(_translate("QtBuilder", "Qt Builder"))
        self.actionQt_Builder.setShortcut(_translate("QtBuilder", "Ctrl+A"))
        self.actionDeveloper.setText(_translate("QtBuilder", "Developer"))
        self.actionDeveloper.setShortcut(_translate("QtBuilder", "Ctrl+D"))
        self.actionChange_log.setText(_translate("QtBuilder", "Change log"))
        self.actionChange_log.setShortcut(_translate("QtBuilder", "Ctrl+L"))
        self.actionUpdate.setText(_translate("QtBuilder", "Update"))


    def build(self):
        import os
        UI = self.UIEntry.text()
        Script = self.OutputEntry.text()
        dir_check = os.system("cd Scripts")
        if(dir_check > 0):
            os.system("mkdir Scripts")
            script_dir = "Scripts"
        else:
            pass
    
        os.system("cd ../")
        script_dir = "Scripts"
        
        
        build_script = subprocess.getstatusoutput("""pyuic5 -x {} -o {}""".format(UI,script_dir +"/" + Script))
        if(build_script[0] < 1):
            self.Notifs.setStyleSheet("color:green;")
            self.Notifs.setText("Script built successfully")
        else:
            self.Notifs.setStyleSheet("color:red;")
            self.Notifs.setText("Could not build script!!")
            self.Update_notifs.setStyleSheet("color:red;font-size:13px;")
            self.Update_notifs.setText(f"Build error:{build_script[1][7:]}")
            
    def updater(self):
        from qtsys.update import updater
    def settings(self):
        from qtsys.config import settings

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtBuilder = QtWidgets.QMainWindow()
    dark(app)
    ui = Ui_QtBuilder()
    ui.setupUi(QtBuilder)
    mw = ModernWindow(QtBuilder)
    mw.show()
    sys.exit(app.exec_())
