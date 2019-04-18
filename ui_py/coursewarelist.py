# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coursewarelist.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QHeaderView
from PyQt5.QtCore import Qt
import sys
from settings import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.treeWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        for i in range(len(self.coursewareList)):
            QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "课件列表-iclassDesktop"+version))
        self.treeWidget.headerItem().setText(0, _translate("Form", "选择"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "文件名"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "文件大小"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        for i in range(len(self.coursewareList)):
            self.treeWidget.topLevelItem(i).setCheckState(0,Qt.Unchecked)
            self.treeWidget.topLevelItem(i).setText(1, _translate("Form", self.coursewareList[i]['file_name']))
            size=self.coursewareList[i]['size']/1000000
            self.treeWidget.topLevelItem(i).setText(2, _translate("Form", '%.2fM'%size))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.pushButton_3.setText(_translate("Form", "Downloadall"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.label.setText(_translate("Form", "Developed by BBfat"))



if __name__=="__main__":
    app=QApplication(sys.argv)
    w=QWidget()
    Ui_Form().setupUi(w)
    w.show()
    sys.exit(app.exec_())
