def normal(input):
    try:
        arg = input.split(' ')
        if len(arg)<4:
            x = float(arg[0])
            s = float(arg[1])
            base = float(arg[2])
            # (base*(s*(1+0.002))-x)x = n
            number = base / x
            # y1 * number - x * number - y1 * number *0.02 = -s
            y1 = (s + (1.002 * x * number)) / (0.998  * number)
            n = (y1-x) / x
            y2 = (-s + (1.002 * x * number)) / (0.998  * number)
            return '涨幅比: '+str(round(n,4))+'  建议卖出价: '+str(round(y1,4))+'  建议止损价: '+str(round(y2,4))
        else:
            return "格式错误"
    except:
        return "格式错误"
def Kong(input):
    try:
        arg = input.split(' ')
        if len(arg) < 6:
            # 借币卖出价
            x = float(arg[0])
            # 盈利额
            s = float(arg[1])
            # 基础资产
            base = float(arg[2])
            # 杠杆倍数
            bei = float(arg[3])
            number = round((base / x) * bei, 2)
            # 借币天数
            day = int(arg[4])
            # 预计买入价(赚s利润):
            print((0.00098 * day) + 1.002)
            y1 = ((0.998 * number * x) - s) / ((1.002 + (0.00098 * day)) * number)
            # 涨跌百分比:
            n = (y1 - x) / x
            # 预计买入价(赔s利润):
            y2 = ((0.998 * number * x) + s) / ((1.002 + (0.00098 * day)) * number)
            # 爆仓价:
            p = ((base + (x * number)) / 1.1) / (number * (1 + (0.00098 * day)))
            # 风险率:
            k = (base + (y1 * number)) / (x * number + (x * number * 0.00098 * day))
            return '借币数量: '+str(round(number,4))+'  涨幅比: '+str(round(n,4))+'  预计买入价(赚'+str(s)+'利润): '+str(round(y1,4))+'  预计买入价(赔'+str(s)+'利润): '+str(round(y2,4))+'  风险值: '+str(round(k,4))+'  爆仓价: '+str(round(p,4))
        else:
            return "格式错误"
    except:
        return "格式错误"

#print(Kong('89 2 88 2 2'))
# k线风险率: 0.0092  建议卖出价: 90.4921  建议止损价: 89.2073
#print(normal('89.67 2 279.73'))

#x = 281.82-279.73
#print(x)