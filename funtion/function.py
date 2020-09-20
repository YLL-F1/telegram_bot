import base64
import hashlib
import binascii

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

def hex_en_0x(input):
    try:
        sum = ''
        for i in input:
            str_bin = i.encode('utf-8')
            sum += '\\0x'+binascii.hexlify(str_bin).decode('utf-8')
        return sum
    except:
        return "格式错误"
def hex_en(input):
    try:
        str_bin = input.encode('utf-8')
        return binascii.hexlify(str_bin).decode('utf-8')
    except:
        return "格式错误"