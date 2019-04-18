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
    process=pyqtSignal(float)
    def __init__(self,downloadList,save_path):
        super().__init__()
        self.downloadList=downloadList
        self.save_path=save_path

    def run(self):
        sumSize=0
        nowSize = 0
        for courseware in self.downloadList:
            sumSize+=courseware['size']
        for courseware in self.downloadList:
            if courseware['type'] != 'dir':
                data = {
                    'cidReset': True,
                    'cidReq': courseware['coursecode']
                }
                response=requests.get('http://iclass.ncut.edu.cn/iclass/netclass/backends/download_api.php?url=' + courseware['url'],
                    params=data,stream=True)
                with open(self.save_path + '/' + courseware['file_name'], 'wb') as f:
                    for data in response.iter_content(chunk_size=1024):
                        f.write(data)
                        nowSize+=len(data)
                        self.process.emit(nowSize/sumSize*100)
            else:
                pass
        self.finish.emit()