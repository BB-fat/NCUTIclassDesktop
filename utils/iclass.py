import requests
import json
from utils.parseurl import parseUrl


def getCourseList(uid):
    data = {
        'sno': uid
    }
    res = json.loads(requests.get('http://v.ncut.edu.cn/course', params=data).text)
    if res['data']==[]:
        return None
    return res['data']


def getCoursewareList(courseCode=None):
    data = {
        'code' :courseCode
    }
    res = json.loads(requests.get('http://v.ncut.edu.cn/document', params=data).text)
    wareList=[]
    if res['data']==[]:
        return None
    for key,value in res['data'].items():
        tempDict=value
        quote=parseUrl(tempDict['url'])
        tempDict['url']=quote['url']
        tempDict['coursecode']=quote['cidReq']
        tempDict['file_name'] = key.split('/')[-1]
        if tempDict['type']!='dir':
            tempDict['type'] = key.split('.')[-1]
        wareList.append(tempDict)
    return wareList



if __name__=="__main__":
    pass