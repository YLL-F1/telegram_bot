import base64

def base64_de(input):
    try:
        encodestr = base64.b64decode(bytes(input, encoding="gbk"))
        return str(encodestr,'utf-8')
    except:
        return "格式错误"
def assic_de(input):
    try:
        sum = ''
        encodestr = input.split(' ')
        for i in encodestr:
            sum += chr((eval(i)))
        return sum
    except:
        return "格式错误"

