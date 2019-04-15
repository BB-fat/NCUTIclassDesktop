import requests
import json


def getCourseList(uid):
    data = {
        'sno': uid
    }
    res = json.loads(requests.get('http://v.ncut.edu.cn/course', params=data).text)
    if res['data']==[]:
        return None
    return res['data']




if __name__=="__main__":
    pass