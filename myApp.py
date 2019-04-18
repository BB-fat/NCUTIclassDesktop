from PyQt5.QtWidgets import QWidget,QMessageBox,QFileDialog

from ui_py import login,list,confirm,coursewarelist,loading,processBar
from utils.threads import *

class myAPP(QWidget,login.Ui_Form):
    def __init__(self):
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.login)

    def login(self):
        courseList=getCourseList(self.LineEdit.text())
        if courseList==None:
            QMessageBox.warning(self,"错误","学号有误，请重新输入",QMessageBox.Ok)
            self.show()
            self.LineEdit.clear()
        else:
            self.close()
            self.listPage=listPage(courseList)
            self.listPage.show()


class listPage(QWidget,list.Ui_Form):
    '''
    课程列表页面
    '''
    def __init__(self,courseList):
        super(QWidget,self).__init__()
        self.courseList=courseList
        self.setupUi(self)
        self.listWidget.itemDoubleClicked['QListWidgetItem*'].connect(self.clickCourse)

    def clickCourse(self,item):
        self.hide()
        self.loadBox=loading.Loading()
        self.loadBox.show()
        self.thread_CoursewareList=ReqCoursewareList(self.courseList,item.text())
        self.thread_CoursewareList.start()
        self.thread_CoursewareList.empty.connect(self.showEmpty)
        self.thread_CoursewareList.finish.connect(self.toDownload)

    def showEmpty(self):
        self.loadBox.close()
        self.show()
        self.confirmBox = confirm.confirmBox('亲', '抱歉，暂无课件！')
        self.confirmBox.show()


    def toDownload(self,coursewareList):
        self.loadBox.close()
        self.downloadPage=downloadPage(coursewareList,self)
        self.downloadPage.show()


class downloadPage(QWidget,coursewarelist.Ui_Form):
    '''
    下载页面
    '''
    def __init__(self,coursewareList,father):
        self.father=father
        self.coursewareList=coursewareList
        super(QWidget,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.showFather)
        self.pushButton.clicked.connect(self.download)
        self.pushButton_3.clicked.connect(self.downloadAll)

    def showFather(self):
        self.close()
        self.father.show()

    def download(self):
        downloadList=[]
        for i in range(len(self.coursewareList)):
            if self.treeWidget.topLevelItem(i).checkState(0)!=0:
                downloadList.append(self.coursewareList[i])
        save_path=QFileDialog.getExistingDirectory(self,"选择保存位置",'.')
        if save_path=='':
            return
        self.processBar=processBar.ProcessBar()
        self.processBar.pushButton.clicked.connect(self.stopDownload)
        self.processBar.show()
        self.thread_download=DownloadCourseware(downloadList,save_path)
        self.thread_download.start()
        self.thread_download.finish.connect(self.downloadFinish)
        self.thread_download.process.connect(self.downloadProcess)

    def downloadAll(self):
        save_path=QFileDialog.getExistingDirectory(self,"选择保存位置",'.')
        if save_path=='':
            return
        self.processBar=processBar.ProcessBar()
        self.processBar.pushButton.clicked.connect(self.stopDownload)
        self.processBar.show()
        self.thread_download=DownloadCourseware(self.coursewareList,save_path)
        self.thread_download.start()
        self.thread_download.finish.connect(self.downloadFinish)
        self.thread_download.process.connect(self.downloadProcess)

    def downloadFinish(self):
        self.processBar.close()
        QMessageBox.information(self,"亲","下载完成！",QMessageBox.Ok)

    def downloadProcess(self,size):
        self.processBar.progressBar.setValue(size)

    def stopDownload(self):
        self.processBar.close()
        self.thread_download.quit()