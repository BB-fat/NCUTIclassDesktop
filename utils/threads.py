from PyQt5.QtCore import *
from utils.iclass import *

class ReqCoursewareList(QThread):
    empty = pyqtSignal()
    finish = pyqtSignal(list)
    def __init__(self,courseList,course_name):
        super().__init__()
        self.courseList=courseList
        self.course_name=course_name

    def run(self):
        for course in self.courseList:
            if course['course_name']==self.course_name:
                coursewareList = getCoursewareList(course['course_code'])
                break
        if coursewareList == None:
            self.empty.emit()
        else:
            self.finish.emit(coursewareList)


class DownloadCourseware(QThread):
    finish=pyqtSignal()
    def __init__(self,downloadList,save_path):
        super().__init__()
        self.downloadList=downloadList
        self.save_path=save_path

    def run(self):
        downloadCourseware(self.downloadList, self.save_path)
        self.finish.emit()