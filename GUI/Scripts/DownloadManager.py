# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\admire.BLAZE.000\Desktop\QT\downloader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Downloder(object):
    def setupUi(self, Downloder):
        Downloder.setObjectName("Downloder")
        Downloder.setWindowModality(QtCore.Qt.WindowModal)
        Downloder.setEnabled(True)
        Downloder.resize(704, 583)
        Downloder.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Downloder.setWindowIcon(icon)
        Downloder.setWindowOpacity(1.0)
        Downloder.setToolTipDuration(2)
        self.label = QtWidgets.QLabel(Downloder)
        self.label.setGeometry(QtCore.QRect(0, -10, 701, 71))
        self.label.setStyleSheet("background-color: rgb(0, 197, 95);\n"
"color: rgb(255, 255, 255);\n"
"font: 0 28pt \"Trench\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.URL = QtWidgets.QLineEdit(Downloder)
        self.URL.setGeometry(QtCore.QRect(60, 120, 501, 31))
        self.URL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.URL.setDragEnabled(True)
        self.URL.setClearButtonEnabled(True)
        self.URL.setObjectName("URL")
        self.DownloadButton = QtWidgets.QPushButton(Downloder)
        self.DownloadButton.setGeometry(QtCore.QRect(570, 120, 121, 31))
        self.DownloadButton.setObjectName("DownloadButton")
        self.Status_show = QtWidgets.QLabel(Downloder)
        self.Status_show.setGeometry(QtCore.QRect(30, 160, 311, 31))
        self.Status_show.setStyleSheet("font: 0 18pt \"Trench\";\n"
"text-decoration: underline;\n"
"color: rgb(0, 0, 0);")
        self.Status_show.setText("")
        self.Status_show.setObjectName("Status_show")
        self.FiletreeWidget = QtWidgets.QTreeWidget(Downloder)
        self.FiletreeWidget.setGeometry(QtCore.QRect(60, 190, 551, 331))
        self.FiletreeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FiletreeWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.FiletreeWidget.setLineWidth(3)
        self.FiletreeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.FiletreeWidget.setWordWrap(False)
        self.FiletreeWidget.setHeaderHidden(False)
        self.FiletreeWidget.setColumnCount(3)
        self.FiletreeWidget.setObjectName("FiletreeWidget")
        self.FiletreeWidget.header().setVisible(True)
        self.FiletreeWidget.header().setCascadingSectionResizes(False)
        self.FiletreeWidget.header().setHighlightSections(True)
        self.FiletreeWidget.header().setSortIndicatorShown(True)
        self.FiletreeWidget.header().setStretchLastSection(True)
        self.actionOpen = QtWidgets.QAction(Downloder)
        self.actionOpen.setCheckable(True)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(Downloder)
        QtCore.QMetaObject.connectSlotsByName(Downloder)

    def retranslateUi(self, Downloder):
        _translate = QtCore.QCoreApplication.translate
        Downloder.setWindowTitle(_translate("Downloder", "Downlaoder"))
        Downloder.setToolTip(_translate("Downloder", "File Downloader"))
        Downloder.setWhatsThis(_translate("Downloder", "A file downloder"))
        Downloder.setWindowFilePath(_translate("Downloder", "file:///"))
        self.label.setText(_translate("Downloder", "DOWNLOADER"))
        self.URL.setPlaceholderText(_translate("Downloder", " URL"))
        self.DownloadButton.setText(_translate("Downloder", "Download"))
        self.FiletreeWidget.headerItem().setText(0, _translate("Downloder", "Name"))
        self.FiletreeWidget.headerItem().setText(1, _translate("Downloder", "Date"))
        self.FiletreeWidget.headerItem().setText(2, _translate("Downloder", "Size"))
        self.actionOpen.setText(_translate("Downloder", "Open"))
        self.actionOpen.setToolTip(_translate("Downloder", "<html><head/><body><p><span style=\" font-weight:600;\">Open files</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Downloder = QtWidgets.QFrame()
    ui = Ui_Downloder()
    ui.setupUi(Downloder)
    Downloder.show()
    sys.exit(app.exec_())
