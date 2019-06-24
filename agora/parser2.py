import bs4
import requests
import re
import math
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agora.settings")
import django
django.setup()

from parsed_data.models import LawData, LawNum


def cleanText(readData):
    text = re.sub('[,"\n\t\r ]', "", readData)
    return text


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def index():
    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/nsmLmSts/out?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_top_area')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = int(cleanText(str(page_num[0])[205:210]))

    data2 = []
    law_name = []
    law_people = []
    law_department = []
    law_condition = []
    law_date = []
    law_doc_num = []

    page_num_num = []  # 입법 세부 페이지 번호

    groups2 = []
    dict_objs = []

    for num in range(1, 5):
        html2 = requests.get(f'https://opinion.lawmaking.go.kr/gcom/nsmLmSts/out?pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        ranks2 = soup2.select('.tbl_typeA tr td')

        for i in range(len(ranks2)):
            data2.append(cleanText(ranks2[i].text))

        for j in chunker(data2, 6):
            groups2.append(j)
            law_name.append(j[0])
            law_people.append(j[1])
            law_department.append(j[2])
            law_condition.append(j[3])
            law_date.append(j[4])
            law_doc_num.append(j[5])

        for i in page_num:
            page_num_num.append(str(i)[36:49])

        context = ['law_name',
                   'law_people',
                   'law_department',
                   'law_condition',
                   'law_date',
                   'law_doc_num']

        for k in range(len(groups2)):
            zipbObj = zip(context, groups2[k])
            dict_objs.append(dict(zipbObj))

    return dict_objs

def pagenum():
    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/nsmLmSts/out?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_top_area')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = int(cleanText(str(page_num[0])[205:210]))

    page_num_num = []  # 입법 세부 페이지 번호
    dict_objs2 = []

    for num in range(1, 5):
        html2 = requests.get(f'https://opinion.lawmaking.go.kr/gcom/nsmLmSts/out?pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        page_num = soup2.select('.tbl_typeA tr td a')

        for i in range(len(page_num)):
            page_num_num.append(str(page_num[i])[32:39])

        context2 = ['page_num_num']

        for k in range(len(page_num_num)):
            zipbObj2 = zip(context2, [page_num_num[k]])
            dict_objs2.append(dict(zipbObj2))

    return dict_objs2


if __name__ == '__main__':
    data_dict = index()
    num_dict = pagenum()
    for i in range(len(data_dict)):
        item = data_dict[i]
        LawData(law_name=item['law_name'],
                law_people=item['law_people'],
                law_department=item['law_department'],
                law_condition=item['law_condition'],
                law_date=item['law_date'],
                law_doc_num=item['law_doc_num']).save()
    for j in range(len(num_dict)):
        number = num_dict[j]
        LawNum(
            page_num_num=number['page_num_num']
        ).save()



