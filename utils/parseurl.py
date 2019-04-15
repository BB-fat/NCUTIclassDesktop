from urllib import parse

def parseUrl(url):
    '''
    接受一个url，返回参数字典
    :param url:
    :return:
    '''
    return dict(parse.parse_qsl(url.split('?')[-1]))