# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qml/Ui_CreateCompanyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_CreateCompanyDialog(object):
    def setupUi(self, CreateCompanyDialog):
        CreateCompanyDialog.setObjectName("CreateCompanyDialog")
        CreateCompanyDialog.setWindowModality(QtCore.Qt.WindowModal)
        CreateCompanyDialog.resize(435, 600)
        CreateCompanyDialog.setModal(True)
        self.tablesGroupBox = QtWidgets.QGroupBox(CreateCompanyDialog)
        self.tablesGroupBox.setGeometry(QtCore.QRect(10, 400, 415, 125))
        self.tablesGroupBox.setObjectName("tablesGroupBox")
        self.chartOfAccCheckBox = QtWidgets.QCheckBox(self.tablesGroupBox)
        self.chartOfAccCheckBox.setGeometry(QtCore.QRect(10, 40, 140, 30))
        self.chartOfAccCheckBox.setObjectName("chartOfAccCheckBox")
        self.journalCheckBox = QtWidgets.QCheckBox(self.tablesGroupBox)
        self.journalCheckBox.setGeometry(QtCore.QRect(10, 80, 140, 30))
        self.journalCheckBox.setObjectName("journalCheckBox")
        self.companyGroupBox = QtWidgets.QGroupBox(CreateCompanyDialog)
        self.companyGroupBox.setGeometry(QtCore.QRect(10, 10, 415, 195))
        self.companyGroupBox.setObjectName("companyGroupBox")
        self.nameLabel = QtWidgets.QLabel(self.companyGroupBox)
        self.nameLabel.setGeometry(QtCore.QRect(10, 40, 130, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setObjectName("nameLabel")
        self.addressLabel = QtWidgets.QLabel(self.companyGroupBox)
        self.addressLabel.setGeometry(QtCore.QRect(10, 80, 140, 30))
        self.addressLabel.setObjectName("addressLabel")
        self.addressText = QtWidgets.QTextEdit(self.companyGroupBox)
        self.addressText.setGeometry(QtCore.QRect(150, 80, 250, 60))
        self.addressText.setAcceptRichText(True)
        self.addressText.setObjectName("addressText")
        self.taxNumLabel = QtWidgets.QLabel(self.companyGroupBox)
        self.taxNumLabel.setGeometry(QtCore.QRect(10, 150, 140, 30))
        self.taxNumLabel.setObjectName("taxNumLabel")
        self.taxNumText = QtWidgets.QLineEdit(self.companyGroupBox)
        self.taxNumText.setGeometry(QtCore.QRect(150, 150, 250, 30))
        self.taxNumText.setObjectName("taxNumText")
        self.nameText = QtWidgets.QLineEdit(self.companyGroupBox)
        self.nameText.setGeometry(QtCore.QRect(150, 40, 250, 30))
        self.nameText.setObjectName("nameText")
        self.databaseGroupBox = QtWidgets.QGroupBox(CreateCompanyDialog)
        self.databaseGroupBox.setGeometry(QtCore.QRect(10, 220, 415, 165))
        self.databaseGroupBox.setObjectName("databaseGroupBox")
        self.userLabel = QtWidgets.QLabel(self.databaseGroupBox)
        self.userLabel.setGeometry(QtCore.QRect(10, 40, 140, 30))
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.databaseGroupBox)
        self.passLabel.setGeometry(QtCore.QRect(10, 80, 150, 30))
        self.passLabel.setObjectName("passLabel")
        self.retypePassLabel = QtWidgets.QLabel(self.databaseGroupBox)
        self.retypePassLabel.setGeometry(QtCore.QRect(10, 120, 140, 30))
        self.retypePassLabel.setObjectName("retypePassLabel")
        self.userText = QtWidgets.QLineEdit(self.databaseGroupBox)
        self.userText.setGeometry(QtCore.QRect(150, 40, 250, 30))
        self.userText.setObjectName("userText")
        self.passText = QtWidgets.QLineEdit(self.databaseGroupBox)
        self.passText.setGeometry(QtCore.QRect(150, 80, 250, 30))
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setObjectName("passText")
        self.retypePassText = QtWidgets.QLineEdit(self.databaseGroupBox)
        self.retypePassText.setGeometry(QtCore.QRect(150, 120, 250, 30))
        self.retypePassText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.retypePassText.setObjectName("retypePassText")
        self.horizontalLayoutWidget = QtWidgets.QWidget(CreateCompanyDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 537, 261, 48))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createButton.setObjectName("createButton")
        self.horizontalLayout.addWidget(self.createButton)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.retranslateUi(CreateCompanyDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateCompanyDialog)

    def retranslateUi(self, CreateCompanyDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateCompanyDialog.setWindowTitle(_translate("CreateCompanyDialog", "MainWindow"))
        self.tablesGroupBox.setTitle(_translate("CreateCompanyDialog", "Tables"))
        self.chartOfAccCheckBox.setText(_translate("CreateCompanyDialog", "Chart of Account"))
        self.journalCheckBox.setText(_translate("CreateCompanyDialog", "Journal"))
        self.companyGroupBox.setTitle(_translate("CreateCompanyDialog", "Company"))
        self.nameLabel.setText(_translate("CreateCompanyDialog", "Company Name"))
        self.addressLabel.setText(_translate("CreateCompanyDialog", "Address"))
        self.taxNumLabel.setText(_translate("CreateCompanyDialog", "Tax Number"))
        self.databaseGroupBox.setTitle(_translate("CreateCompanyDialog", "Database"))
        self.userLabel.setText(_translate("CreateCompanyDialog", "User"))
        self.passLabel.setText(_translate("CreateCompanyDialog", "Password"))
        self.retypePassLabel.setText(_translate("CreateCompanyDialog", "Retype Password"))
        self.createButton.setText(_translate("CreateCompanyDialog", "Create"))
        self.cancelButton.setText(_translate("CreateCompanyDialog", "Cancel"))
