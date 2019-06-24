from django.shortcuts import render, redirect
import bs4
import requests
import re
import math
import request

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agora.settings")
import django
django.setup()
from parsed_data.models import RawData, NumData


def cleanText(readData):
    text = re.sub('[,"\n\t\r ]', "", readData)
    return text


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def index():
    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_typeA tr td a')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = math.ceil(int(groups[0][0]) / 10)

    data2 = []
    raw_num = []
    raw_name = []
    raw_attribue = []
    raw_condition = []
    raw_department = []
    raw_status = []

    page_num_num = []  # 입법 세부 페이지 번호

    groups2 = []
    dict_objs = []

    for num in range(1, 3):
        html2 = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        ranks2 = soup2.select('.tbl_typeA tr td')

        for i in range(len(ranks2)):
            data2.append(cleanText(ranks2[i].text))

        for j in chunker(data2, 6):
            groups2.append(j)
            raw_num.append(j[0])
            raw_name.append(j[1])
            raw_attribue.append(j[2])
            raw_condition.append(j[3])
            raw_department.append(j[4])
            raw_status.append(j[5])

        for i in page_num:
            page_num_num.append(str(i)[36:49])

        context = ['raw_num',
                   'raw_name',
                   'raw_attribue',
                   'raw_condition',
                   'raw_department',
                   'raw_status']

        for k in range(len(groups2)):
            zipbObj = zip(context, groups2[k])
            dict_objs.append(dict(zipbObj))

    return dict_objs

def pagenum():
    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_typeA tr td a')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = math.ceil(int(groups[0][0]) / 10)

    page_num_num = []  # 입법 세부 페이지 번호
    dict_objs2 = []

    for num in range(1, 3):
        html2 = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        page_num = soup2.select('.tbl_typeA tr td a')

        for i in page_num:
            page_num_num.append(str(i)[36:49])

        context = ['page_num_num']

        for k in range(len(page_num_num)):
            zipbObj2 = zip(context, page_num_num[k])
            dict_objs2.append(dict(zipbObj2))

    return dict_objs2


if __name__ == '__main__':
    data_dict = index()
    num_dict = pagenum()
    for i in range(len(data_dict)):
        item = data_dict[i]
    for j in range(len(num_dict)):
        number = num_dict[j]

    RawData(raw_name=item['raw_name'],
            raw_attribue=item['raw_attribue'],
            raw_condition=item['raw_condition'],
            raw_department=item['raw_department'],
            raw_status=item['raw_status']).save()

    NumData(
        page_num_num=number['page_num_num']
    ).save()