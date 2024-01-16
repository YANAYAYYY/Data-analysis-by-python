#coding=gbk
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np

# #��ȡ��ҳ
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
# response = requests.get("https://www.ctma.com.cn/chukoujianbao.html?orderway=desc&orderby=publishtime", headers = headers)
# # print(response)   #�������Ƿ���Ӧ�ɹ�
# # print(response.status_code)   #��״̬�룬�鿴����ʧ�ܵ����⣬200���ǳɹ�
# # print(response.text)
# html = response.text
#
# #��ȡ��ҳ�е�����Ҫ��ÿ���²�Ҷ���ڵ����ӵ�����
# soup = BeautifulSoup(html,"html.parser")
# all_listcontents = soup.find_all("ul",attrs={"class":"info-list info-list-1"})
# # for link in all_listcontents:
# #     print(link)
#
# #������Щ�����зֱ���ȡÿ���²�Ҷ���ڵ�����
# links = []
# for listcontent in all_listcontents:
#     tags = listcontent.find_all("a")   #��ȡ��ǩ��href����
#     for tag in tags:
#         href = tag.get("href")
#         links.append(href)
# # print(links)
#
# #����ÿ���µ������ڣ���ȡ�ı�����
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

# ����������ʽ��ȡÿ���µ���Ҫ���ݣ�����Ҫע��ÿһ���µ����ݶ����ۼ�ǰ�����µ�����
pattern1 = r"2023��1-(\d+)��"
pattern2 = r'�̲������Ϊ(\d+(\.\d+)?(��)?)��'
pattern3 = r"��������Ϊ(\d+(\.\d+)?(��)?)��"
pattern4 = r"�����������Ϊ(\d+(\.\d+)?(��)?)��"
pattern5 = r"���򻨲������Ϊ(\d+(\.\d+)?(��)?)��"
pattern6 = r"�ն��������Ϊ(\d+(\.\d+)?(��)?)��"
pattern7 = r"�������������Ϊ(\d+(\.\d+)?(��)?)��"
pattern8 = r"�ڲ������Ϊ(\d+(\.\d+)?(��)?)��"
pattern9 = r"�ײ������Ϊ(\d+(\.\d+)?(��)?)��"
pattern10 = r"�й���Ҷ�ۼƳ�����Ϊ(\d+(\.\d+)?(��)?)��"
pattern11 = r"�ۼƳ��ڶ�Ϊ(\d+(\.\d+)?)����Ԫ"     #(?!�ۼ�)��ʾ���ڶ�ܽ����ۼ�
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

#�����д�����"��λ������x10000��ȥ����λ���������µ��б��������򡱵�λ������ת���ɸ�������ʽ�����ں�������
for lst in Search_list:
    for index, num in enumerate(lst):
        if "��" in num:
            number = float(num[:-1]) * 10000
            lst[index] = number
        else:
            number = float(num)
            lst[index] = number
    # print(lst)

# ��ÿ���µĳ������� = ������µ��ۼ����� - �ϸ��µ��ۼ�����
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

#�����̲������
# list_GreenTeaExportVolumeMonthly = [float(list_GreenTeaExportVolume[i]) - float(list_GreenTeaExportVolume[i + 1]) for i in range(len(list_GreenTeaExportVolume) - 1)]
# # print(list_GreenTeaExportVolume)
# # print(list_GreenTeaExportVolumeMonthly)

#�����еĵ�������
for n in range(len(Search_list)):
    monthly_diffs = [float(Search_list[n][i]) - float(Search_list[n][i + 1]) for i in range(len(Search_list[n]) - 1)]
    Search_list_Monthly[n].append(monthly_diffs)

print("�·�",list_Month,"��λ����")
print("�̲�ÿ���ۼƳ�����",list_GreenTeaExportVolume,"��λ����")
print("�̲�ÿ�µ��³�����",list_GreenTeaExportVolumeMonthly,"��λ����")
print("���ÿ���ۼƳ�����",list_RedTeaExportVolume,"��λ����")
print("���ÿ�µ��³�����",list_RedTeaExportVolumeMonthly,"��λ����")
print("������ÿ���ۼƳ�����",list_OolongTeaExportVolume,"��λ����")
print("������ÿ�µ��³�����",list_OolongTeaExportVolumeMonthly,"��λ����")
print("���򻨲�ÿ���ۼƳ�����",list_JasmineTeaExportVolume,"��λ����")
print("���򻨲�ÿ�µ��³�����",list_JasmineTeaExportVolumeMonthly,"��λ����")
print("�ն���ÿ���ۼƳ�����",list_PuerTeaExportVolume,"��λ����")
print("�ն���ÿ�µ��³�����",list_PuerTeaExportVolumeMonthly,"��λ����")
print("��������ÿ���ۼƳ�����",list_FlowerTeaExportVolume,"��λ����")
print("��������ÿ�µ��³�����",list_FlowerTeaExportVolumeMonthly,"��λ����")
print("�ڲ�ÿ���ۼƳ�����",list_BlackTeaExportVolume,"��λ����")
print("�ڲ�ÿ�µ��³�����",list_BlackTeaExportVolumeMonthly,"��λ����")
print("�ײ�ÿ���ۼƳ�����",list_WhiteTeaExportVolume,"��λ����")
print("�ײ�ÿ�µ��³�����",list_WhiteTeaExportVolumeMonthly,"��λ����")
print("�й���Ҷ�ۼƳ�����",list_ChineseTeaExportVolume,"��λ����")
print("�й���Ҷ����ÿ�³�����",list_ChineseTeaExportVolumeMonthly,"��λ����")
print("�й���Ҷ�ۼƳ��ڶ�",list_ExportValue,"����Ԫ")
print("�й���Ҷÿ�³��ڶ�",list_ExportValueMonthly,"����Ԫ")