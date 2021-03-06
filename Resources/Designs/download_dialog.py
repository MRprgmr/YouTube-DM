# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/download_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 278)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mw_icons/download_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.thumbnail = QtWidgets.QLabel(Dialog)
        self.thumbnail.setMinimumSize(QtCore.QSize(192, 108))
        self.thumbnail.setMaximumSize(QtCore.QSize(192, 108))
        self.thumbnail.setStyleSheet("border: 1px solid rgb(200, 200, 200);\n"
"background-color: white;")
        self.thumbnail.setText("")
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout_4.addWidget(self.thumbnail)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.length_l = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.length_l.setFont(font)
        self.length_l.setObjectName("length_l")
        self.verticalLayout_2.addWidget(self.length_l)
        self.size_l = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.size_l.setFont(font)
        self.size_l.setObjectName("size_l")
        self.verticalLayout_2.addWidget(self.size_l)
        self.downloaded_l = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.downloaded_l.setFont(font)
        self.downloaded_l.setObjectName("downloaded_l")
        self.verticalLayout_2.addWidget(self.downloaded_l)
        self.speed_l = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.speed_l.setFont(font)
        self.speed_l.setObjectName("speed_l")
        self.verticalLayout_2.addWidget(self.speed_l)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setMinimumSize(QtCore.QSize(0, 22))
        self.title.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setText("")
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setStyleSheet("border-color: rgb(195, 195, 195);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.a_f = QtWidgets.QComboBox(Dialog)
        self.a_f.setEnabled(True)
        self.a_f.setMinimumSize(QtCore.QSize(160, 28))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setKerning(True)
        self.a_f.setFont(font)
        self.a_f.setStyleSheet("QComboBox {\n"
"    border: 1px solid #7cd0ef;\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox:hover{\n"
"border-color: #5487ee;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
" \n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"  image: url(:/mw_icons/drop_down.png);\n"
"height: 18px;\n"
"width: 18px;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d8d7d7, stop: 1 #e9e9e9);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")
        self.a_f.setCurrentText("")
        self.a_f.setIconSize(QtCore.QSize(22, 22))
        self.a_f.setDuplicatesEnabled(False)
        self.a_f.setObjectName("a_f")
        self.horizontalLayout_3.addWidget(self.a_f)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.download_button = QtWidgets.QPushButton(Dialog)
        self.download_button.setEnabled(True)
        self.download_button.setMinimumSize(QtCore.QSize(180, 28))
        self.download_button.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        self.download_button.setFont(font)
        self.download_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_button.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border-radius: 6px;\n"
"border: 1px solid #6AF2F0;\n"
"}\n"
"QPushButton:hover {\n"
"color: white;\n"
"background-color: #6AF2F0;\n"
"}\n"
"QPushButton:pressed {\n"
"color: white;\n"
"background-color: rgb(47, 231, 247);\n"
"border: 1px solid #50A5FF;\n"
"}\n"
"QPushButton:disabled {\n"
"background-color: white;\n"
"border-radius: 6px;\n"
"border: 1px solid #6AF2F0;\n"
"color: black;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/mw_icons/download_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap(":/mw_icons/download_icon.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.download_button.setIcon(icon1)
        self.download_button.setIconSize(QtCore.QSize(24, 24))
        self.download_button.setCheckable(False)
        self.download_button.setObjectName("download_button")
        self.horizontalLayout_3.addWidget(self.download_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_path = QtWidgets.QLineEdit(Dialog)
        self.save_path.setMinimumSize(QtCore.QSize(0, 28))
        self.save_path.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(11)
        self.save_path.setFont(font)
        self.save_path.setStyleSheet("\n"
"QLineEdit{\n"
"background-color: white;\n"
"border: 1px solid #59CDF2;\n"
"border-right: None;\n"
"border-bottom-left-radius:3px;\n"
"border-top-left-radius:3px;\n"
"}")
        self.save_path.setText("")
        self.save_path.setReadOnly(True)
        self.save_path.setObjectName("save_path")
        self.horizontalLayout.addWidget(self.save_path)
        self.open_folder = QtWidgets.QPushButton(Dialog)
        self.open_folder.setEnabled(True)
        self.open_folder.setMinimumSize(QtCore.QSize(30, 28))
        self.open_folder.setStyleSheet("QPushButton{\n"
"background-color: white;\n"
"border: 1px solid #59CDF2;\n"
"border-left:None;\n"
"border-bottom-right-radius:5px;\n"
"border-top-right-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid #59CDF2;\n"
"border-left:None;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(225, 225, 225);\n"
"border: 1px solid #59CDF2;\n"
"border-left:None;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: white;\n"
"border: 1px solid #59CDF2;\n"
"border-left:None;\n"
"border-bottom-right-radius:5px;\n"
"border-top-right-radius:5px;\n"
"}")
        self.open_folder.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/mw_icons/open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon2.addPixmap(QtGui.QPixmap(":/mw_icons/open_folder.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.open_folder.setIcon(icon2)
        self.open_folder.setIconSize(QtCore.QSize(22, 22))
        self.open_folder.setObjectName("open_folder")
        self.horizontalLayout.addWidget(self.open_folder)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"text-align: center;\n"
"border: none;\n"
"border-style: None;\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.938, x2:1, y2:0.937318, stop:0 #f64f59, stop:0.440678 #c471ed, stop:0.988636 rgb(18,194,233));\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Videoni Yuklash"))
        self.length_l.setText(_translate("Dialog", "Davomiyligi"))
        self.size_l.setText(_translate("Dialog", "Hajmi"))
        self.downloaded_l.setText(_translate("Dialog", "Yuklandi"))
        self.speed_l.setText(_translate("Dialog", "Tezlik"))
        self.download_button.setText(_translate("Dialog", "Yuklash"))
        self.label.setText(_translate("Dialog", "Manzil"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
