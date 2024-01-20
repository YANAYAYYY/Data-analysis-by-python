#coding=gbk
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

# #获取网页
# headers = {"User-Agent":"xxxxxxxxxxxxxxxxxxx"}
# response = requests.get("https://www.ctma.com.cn/chukoujianbao.html?orderway=desc&orderby=publishtime", headers = headers)
# # print(response)   #看请求是否响应成功
# # print(response.status_code)   #看状态码，查看具体失败的问题，200就是成功
# # print(response.text)
# html = response.text
#
# #提取网页中的所需要的每个月茶叶出口的链接的容器
# soup = BeautifulSoup(html,"html.parser")
# all_listcontents = soup.find_all("ul",attrs={"class":"info-list info-list-1"})
# # for link in all_listcontents:
# #     print(link)
#
# #再在这些容器中分别提取每个月茶叶出口的链接
# links = []
# for listcontent in all_listcontents:
#     tags = listcontent.find_all("a")   #获取标签的href属性
#     for tag in tags:
#         href = tag.get("href")
#         links.append(href)
# # print(links)
#
# #进入每个月的链接内，提取文本内容
# f1 = open("texts for tea export information.csv","a",encoding='utf-8')
# for link in links:
#     response02 = requests.get(f"https://www.ctma.com.cn/{link}", headers=headers)
#     html02 = response02.text
#     soup02 = BeautifulSoup(html02, "html.parser")
#     all_texts = soup02.find_all("p")
#     for texts in all_texts:
#         text_contents = texts.get_text().strip()
#         f1.write(text_contents + "\n")
# f1.close()

# 利用正则表达式提取每个月的重要数据，但是要注意每一个月的数据都是累计前几个月的数据
pattern1 = r"2023年1-(\d+)月"
pattern2 = r'绿茶出口量为(\d+(\.\d+)?(万)?)吨'
pattern3 = r"红茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern4 = r"乌龙茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern5 = r"茉莉花茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern6 = r"普洱茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern7 = r"其他花茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern8 = r"黑茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern9 = r"白茶出口量为(\d+(\.\d+)?(万)?)吨"
pattern10 = r"中国茶叶累计出口量为(\d+(\.\d+)?(万)?)吨"
pattern11 = r"累计出口额为(\d+(\.\d+)?)亿美元"     #(?!累计)表示出口额不能紧跟累计
list_Month = []
list_GreenTeaExportVolume = []
list_RedTeaExportVolume = []
list_OolongTeaExportVolume = []
list_JasmineTeaExportVolume = []
list_PuerTeaExportVolume = []
list_FlowerTeaExportVolume = []
list_BlackTeaExportVolume = []
list_WhiteTeaExportVolume = []
list_ChineseTeaExportVolume = []
list_ExportValue = []

Search_Pattern = [pattern1,pattern2,pattern3,pattern4,pattern5,pattern6,pattern7,pattern8,pattern9,pattern10,pattern11]
Search_list = [list_Month,list_GreenTeaExportVolume,list_RedTeaExportVolume,list_OolongTeaExportVolume,
               list_JasmineTeaExportVolume,list_PuerTeaExportVolume,list_FlowerTeaExportVolume,list_BlackTeaExportVolume,
               list_WhiteTeaExportVolume,list_ChineseTeaExportVolume, list_ExportValue]

f1 = open("texts for tea export information.csv","r",encoding='utf-8')
for i in f1:
    for j in range(len(Search_Pattern)):
        match = re.search(Search_Pattern[j], i)
        if match:
            Search_list[j].append(match.group(1))

# for lst in Search_list:
#     print(lst)

#将其中带“万"单位的数字x10000并去掉单位重新生成新的列表，不带“万”单位的数字转换成浮点数格式，便于后续计算
for lst in Search_list:
    for index, num in enumerate(lst):
        if "万" in num:
            number = float(num[:-1]) * 10000
            lst[index] = number
        else:
            number = float(num)
            lst[index] = number
    # print(lst)

# 求每个月的出口数据 = 用这个月的累计数据 - 上个月的累计数据
list_MonthMonthly = []
list_GreenTeaExportVolumeMonthly = []
list_RedTeaExportVolumeMonthly = []
list_OolongTeaExportVolumeMonthly = []
list_JasmineTeaExportVolumeMonthly = []
list_PuerTeaExportVolumeMonthly = []
list_FlowerTeaExportVolumeMonthly = []
list_BlackTeaExportVolumeMonthly = []
list_WhiteTeaExportVolumeMonthly = []
list_ChineseTeaExportVolumeMonthly = []
list_ExportValueMonthly = []

Search_list_Monthly = [list_MonthMonthly,list_GreenTeaExportVolumeMonthly,list_RedTeaExportVolumeMonthly,list_OolongTeaExportVolumeMonthly,
               list_JasmineTeaExportVolumeMonthly, list_PuerTeaExportVolumeMonthly,list_FlowerTeaExportVolumeMonthly,list_BlackTeaExportVolumeMonthly,
               list_WhiteTeaExportVolumeMonthly, list_ChineseTeaExportVolumeMonthly, list_ExportValueMonthly]

#单月绿茶出口量
# list_GreenTeaExportVolumeMonthly = [float(list_GreenTeaExportVolume[i]) - float(list_GreenTeaExportVolume[i + 1]) for i in range(len(list_GreenTeaExportVolume) - 1)]
# # print(list_GreenTeaExportVolume)
# # print(list_GreenTeaExportVolumeMonthly)

#求所有的单月数据
for n in range(len(Search_list)):
    monthly_diffs = [float(Search_list[n][i]) - float(Search_list[n][i + 1]) for i in range(len(Search_list[n]) - 1)]
    Search_list_Monthly[n].append(monthly_diffs)

print("月份",list_Month,"单位：月")
print("绿茶每月累计出口量",list_GreenTeaExportVolume,"单位：吨")
print("绿茶每月单月出口量",list_GreenTeaExportVolumeMonthly,"单位：吨")
print("红茶每月累计出口量",list_RedTeaExportVolume,"单位：吨")
print("红茶每月单月出口量",list_RedTeaExportVolumeMonthly,"单位：吨")
print("乌龙茶每月累计出口量",list_OolongTeaExportVolume,"单位：吨")
print("乌龙茶每月单月出口量",list_OolongTeaExportVolumeMonthly,"单位：吨")
print("茉莉花茶每月累计出口量",list_JasmineTeaExportVolume,"单位：吨")
print("茉莉花茶每月单月出口量",list_JasmineTeaExportVolumeMonthly,"单位：吨")
print("普洱茶每月累计出口量",list_PuerTeaExportVolume,"单位：吨")
print("普洱茶每月单月出口量",list_PuerTeaExportVolumeMonthly,"单位：吨")
print("其他花茶每月累计出口量",list_FlowerTeaExportVolume,"单位：吨")
print("其他花茶每月单月出口量",list_FlowerTeaExportVolumeMonthly,"单位：吨")
print("黑茶每月累计出口量",list_BlackTeaExportVolume,"单位：吨")
print("黑茶每月单月出口量",list_BlackTeaExportVolumeMonthly,"单位：吨")
print("白茶每月累计出口量",list_WhiteTeaExportVolume,"单位：吨")
print("白茶每月单月出口量",list_WhiteTeaExportVolumeMonthly,"单位：吨")
print("中国茶叶累计出口量",list_ChineseTeaExportVolume,"单位：吨")
print("中国茶叶出口每月出口量",list_ChineseTeaExportVolumeMonthly,"单位：吨")
print("中国茶叶累计出口额",list_ExportValue,"亿美元")
print("中国茶叶每月出口额",list_ExportValueMonthly,"亿美元")
