import base64
import hashlib


def base64_en(input):
    try:
        encodestr = base64.b64encode(input.encode('utf-8'))
        return str(encodestr,'utf-8')
    except:
        return "格式错误"
def assic_en(input):
    try:
        encodestr = ''
        for i in input:
            encodestr = encodestr +str(ord(i)) + ' '
        encodestr = encodestr[0:-1]
        return encodestr
    except:
        return "格式错误"
def md5_en(input):
    try:
        h1 = hashlib.md5()
        h1.update(input.encode(encoding='utf-8'))
        return h1.hexdigest()
    except:
        return "格式错误"
