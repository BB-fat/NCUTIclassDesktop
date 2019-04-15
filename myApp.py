from PyQt5.QtWidgets import QWidget,QMessageBox

from iclass import *
from ui_py import login,list

class myAPP(QWidget,login.Ui_Form):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        # 连接登陆确认函数
        self.buttonBox.accepted.connect(self.login)

    def login(self):
        courseList=getCourseList(self.LineEdit.text())
        if courseList==None:
            QMessageBox.warning(self,"错误","学号有误，请重新输入",QMessageBox.Ok)
            self.show()
            self.LineEdit.clear()
        else:
            self.hide()
            self.listPage=listPage(courseList)
            self.listPage.show()




class listPage(QWidget,list.Ui_Form):
    def __init__(self,courseList):
        super(QWidget,self).__init__()
        self.courseList=courseList
        self.setupUi(self)