# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FormloginObXcwY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 682)
        icon = QIcon()
        icon.addFile(u":/img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_Shadow = QFrame(self.centralwidget)
        self.frame_Shadow.setObjectName(u"frame_Shadow")
        self.frame_Shadow.setAutoFillBackground(False)
        self.frame_Shadow.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
" background: url(\":/img/bg.jpg\") no-repeat;\n"
" border-radius: 10px;\n"
"}\n"
"")
        self.frame_Shadow.setFrameShape(QFrame.StyledPanel)
        self.frame_Shadow.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Shadow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_Object = QFrame(self.frame_Shadow)
        self.frame_Object.setObjectName(u"frame_Object")
        self.frame_Object.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
" background: none;\n"
"}")
        self.frame_Object.setFrameShape(QFrame.StyledPanel)
        self.frame_Object.setFrameShadow(QFrame.Raised)
        self.pushButton_Login = QPushButton(self.frame_Object)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setGeometry(QRect(160, 590, 131, 41))
        font = QFont()
        font.setFamily(u"Noto Sans CJK HK")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Login.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 51, 102);\n"
"	color:#fff;\n"
"	font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 50, 121);\n"
"	border-radius: 15px;\n"
"	border:1px solid rgb(255, 51, 102);\n"
"}\n"
"\n"
"")
        self.lbl_NewUser = QLabel(self.frame_Object)
        self.lbl_NewUser.setObjectName(u"lbl_NewUser")
        self.lbl_NewUser.setGeometry(QRect(170, 540, 71, 17))
        self.lbl_NewUser.setCursor(QCursor(Qt.PointingHandCursor))
        self.lbl_NewUser.setStyleSheet(u"QLabel{\n"
"\n"
"color: rgb(255, 51, 102);\n"
"\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(255, 50, 121);\n"
"}")
        self.lbl_SignUp = QLabel(self.frame_Object)
        self.lbl_SignUp.setObjectName(u"lbl_SignUp")
        self.lbl_SignUp.setGeometry(QRect(240, 540, 54, 17))
        self.lbl_SignUp.setFont(font)
        self.lbl_SignUp.setStyleSheet(u"QLabel{\n"
"\n"
"color:#fff;\n"
"}")
        self.lbl_UserLogin = QLabel(self.frame_Object)
        self.lbl_UserLogin.setObjectName(u"lbl_UserLogin")
        self.lbl_UserLogin.setGeometry(QRect(110, 330, 241, 51))
        self.lbl_UserLogin.setStyleSheet(u"QLabel{\n"
"\n"
"color:#fff;\n"
"font-size:30px;\n"
"}")
        self.lbl_UserLogin.setAlignment(Qt.AlignCenter)
        self.lineEdit_Login = QLineEdit(self.frame_Object)
        self.lineEdit_Login.setObjectName(u"lineEdit_Login")
        self.lineEdit_Login.setGeometry(QRect(60, 400, 341, 51))
        self.lineEdit_Login.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.lineEdit_Password = QLineEdit(self.frame_Object)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(60, 470, 341, 51))
        self.lineEdit_Password.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(238, 238, 236);\n"
"    border-radius: 20px;\n"
"    padding: 15px;\n"
"    background-color: #fff;\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(186, 189, 182);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid   rgb(114, 159, 207);\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.frame_Logo = QFrame(self.frame_Object)
        self.frame_Logo.setObjectName(u"frame_Logo")
        self.frame_Logo.setGeometry(QRect(120, 70, 241, 211))
        self.frame_Logo.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
" background: url(\":/img/logo.png\");\n"
"  background-repeat: no-repeat;\n"
" border-radius: 10px;\n"
"}\n"
"")
        self.frame_Logo.setFrameShape(QFrame.StyledPanel)
        self.frame_Logo.setFrameShadow(QFrame.Raised)
        self.frame_TopBar = QFrame(self.frame_Object)
        self.frame_TopBar.setObjectName(u"frame_TopBar")
        self.frame_TopBar.setGeometry(QRect(0, 0, 456, 41))
        self.frame_TopBar.setMinimumSize(QSize(456, 41))
        self.frame_TopBar.setMaximumSize(QSize(456, 41))
        self.frame_TopBar.setLayoutDirection(Qt.RightToLeft)
        self.frame_TopBar.setStyleSheet(u"QFrame{\n"
"background-color:rgb(42, 42, 42);\n"
"}")
        self.frame_TopBar.setFrameShape(QFrame.StyledPanel)
        self.frame_TopBar.setFrameShadow(QFrame.Raised)
        self.pushButton_Exit = QPushButton(self.frame_TopBar)
        self.pushButton_Exit.setObjectName(u"pushButton_Exit")
        self.pushButton_Exit.setGeometry(QRect(410, 5, 41, 31))
        self.pushButton_Exit.setMinimumSize(QSize(41, 0))
        self.pushButton_Exit.setMaximumSize(QSize(50, 50))
        self.pushButton_Exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Exit.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_Exit.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(46, 52, 54);\n"
"	color:#fff;\n"
"	font-size:15px;\n"
"	text-align:center;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 50, 121);\n"
"}\n"
"\n"
"")
        self.pushButton_Exit.setText(u"X")

        self.verticalLayout.addWidget(self.frame_Object)


        self.horizontalLayout.addWidget(self.frame_Shadow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" Login User", None))
        self.pushButton_Login.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lbl_NewUser.setText(QCoreApplication.translate("MainWindow", u"New User?", None))
        self.lbl_SignUp.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.lbl_UserLogin.setText(QCoreApplication.translate("MainWindow", u"User Login", None))
        self.lineEdit_Login.setText("")
        self.lineEdit_Login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_Password.setText("")
        self.lineEdit_Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
    # retranslateUi

