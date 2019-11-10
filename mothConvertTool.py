from math import *
print("月份转换工具")
mothNumber = input("请用阿拉伯数据输入月份：")
mothEnum = "JanFebMarAprMayJunJulAugSepOctNovDec"
step = (int(mothNumber)-1)*3
mothAbbrev = mothEnum[step:step+3]
print("该月份的对应的英文缩写是："+mothAbbrev)
