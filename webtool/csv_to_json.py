#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

fo = open("/Users/huaan720/Downloads/百度网盘/xmind2testcase-master/docs/case_csvfile/1201.csv", "r")  # 打开csv文件
ls = []
for line in fo:
    line = line.replace("\n", "")  # 将换行换成空
    ls.append(line.split(","))  # 以，为分隔符
fo.close()  # 关闭文件流
fw = open("/Users/huaan720/Downloads/百度网盘/xmind2testcase-master/docs/case_csvfile/csvToJson.json", "w")  # 打开json文件
for i in range(1, len(ls)):  # 遍历文件的每一行内容，除了列名
    ls[i] = dict(zip(ls[0], ls[i]))  # ls[0]为列名，所以为key,ls[i]为value,
    # zip()是一个内置函数，将两个长度相同的列表组合成一个关系对
json.dump(ls[1:], fw, sort_keys=True, indent=4)
# 将Python数据类型转换成json格式，编码过程
# 默认是顺序存放，sort_keys是对字典元素按照key进行排序
# indet参数用语增加数据缩进，使文件更具有可读性
fw.close()
