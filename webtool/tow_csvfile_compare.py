# _*_ coding:utf-8 _*_

'''
csv文件的合并和去重
主要是针对测试用例增加使用此脚本
'''
import pandas as pd
import glob
#输出文件
outputfile = '/Users/huaan720/Downloads/百度网盘/xmind2testcase-master/docs/case_csvfile/new.csv'
#合并csv的文件夹
csv_list = glob.glob('/Users/huaan720/Downloads/百度网盘/xmind2testcase-master/docs/case_csvfile/*.csv')
print(u'共发现%s个CSV文件' % len(csv_list))
print(u'正在处理............')

def hebing():
    for inputfile in csv_list:
        f = open(inputfile,encoding='gbk')
        data = pd.read_csv(f)
        data.to_csv(outputfile, mode='a', index=False, header=None)
    print('完成合并')

def quchong(file):
    df = pd.read_csv(file, header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv(file)
    print('完成去重')

if __name__ == '__main__':
    hebing()
    quchong(outputfile)
