import urllib.request
import urllib
import gzip
import http.cookiejar


def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def ungzip(data):
    try:        
        data = gzip.decompress(data)
    except:
       pass
    return data


header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'ssfree.me',
    'Pragma':'no-cache',
    'Origin':'http://ssfree.me',
    'Connection':'keep-alive',
    'Referer':'http://ssfree.me/auth/login',
    'Cache-Control':'no-cache',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
}


url_login = 'http://ssfree.me/auth/login'
url_checkin = 'http://ssfree.me/user/checkin'

email=['32731964@qq.com','184029788@qq.com','aixy.oul@gmail.com','gnix.oag+1@gmail.com','gnix.oag@gmail.com']
password = '024573ss'

for i in email:
    opener = getOpener(header)
    postDict = {
        'email': i,
        'passwd': password,
        'code':'',
        'remember_me':'week',
    }
    print("use %s checkin" % (i) )
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(url_login, postData)
    data = op.read()
    
    op = opener.open(url_checkin,postData)
    data = op.read()
    data = ungzip(data)
    print(data)
    opener.close()
    del postData
    del data
    del op
    del postDict
    del opener
    
    