# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(570, 306)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        for i in range(len(self.courseList)):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "课程列表-iclassDesktop"))
        self.label_2.setText(_translate("Form", "双击课程进入课件列表(请耐心等待)"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i in range(len(self.courseList)):
            item = self.listWidget.item(i)
            item.setText(_translate("Form", self.courseList[i]['course_name']))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "Developed by BBfat"))


