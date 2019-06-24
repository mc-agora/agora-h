import bs4
import requests
import re
import math
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agora.settings")
import django
django.setup()

from parsed_data.models import ReguData, ReguNum


def cleanText(readData):
    text = re.sub('[,"\n\t\r ]', "", readData)
    return text


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def index():
    html = requests.get(
        f'https://opinion.lawmaking.go.kr/gcom/sts/better?edNsmPtYdFmt=2019.+6.+24.&srchSetYn=Y&stNsmPtYdFmt=2016.+5.+30.&pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_top_area')
    page_num2 = soup.select('.tbl_typeA tr td a')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = int(cleanText(str(page_num[0])[94:97]))

    data2 = []
    total_num = []
    regu_name = []
    regu_paper_num = []
    regu_department = []
    regu_dates = []
    regu_status = []
    regu_condition = []
    regu_num = []
    trash_val = []

    page_num_num = []  # 입법 세부 페이지 번호

    groups2 = []
    dict_objs = []

    for num in range(1, 5):
        html2 = requests.get(
            f'https://opinion.lawmaking.go.kr/gcom/sts/better?edNsmPtYdFmt=2019.+6.+24.&srchSetYn=Y&stNsmPtYdFmt=2016.+5.+30.&pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        ranks2 = soup2.select('.tbl_typeA tr td')

        for i in range(len(ranks2)):
            data2.append(cleanText(ranks2[i].text))

        for j in chunker(data2, 9):
            groups2.append(j)
            total_num.append(j[0])
            trash_val.append(j[1])
            regu_name.append(j[2])
            regu_paper_num.append(j[3])
            regu_department.append(j[4])
            regu_dates.append(j[5])
            regu_status.append(j[6])
            regu_condition.append(j[7])
            regu_num.append(j[8])

        for i in range(len(page_num2)):
            page_num_num.append(str(page_num2[i])[34:41])
        Link_Page_num = page_num_num[0::2]
        context = ['total_num',
                   'trash_val',
                   'regu_name',
                   'regu_paper_num',
                   'regu_department',
                   'regu_dates',
                   'regu_status',
                   'regu_condition',
                   'regu_num']

        for k in range(len(groups2)):
            zipbObj = zip(context, groups2[k])
            dict_objs.append(dict(zipbObj))

    return dict_objs

def pagenum():
    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    page_num = soup.select('.tbl_top_area')
    page_num2 = soup.select('.tbl_typeA tr td a')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = int(cleanText(str(page_num[0])[236:239]))

    page_num_num = []  # 입법 세부 페이지 번호
    dict_objs2 = []

    for num in range(1, 5):
        html2 = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex={num}').text
        soup2 = bs4.BeautifulSoup(html2, "html.parser")
        page_num2 = soup2.select('.tbl_typeA tr td a')

        for i in range(len(page_num2)):
            page_num_num.append(str(page_num2[i])[36:49])
        Link_Page_num = page_num_num[0::2]

        context2 = ['Link_Page_num']

        for k in range(len(Link_Page_num)):
            zipbObj2 = zip(context2, [Link_Page_num[k]])
            dict_objs2.append(dict(zipbObj2))

    return dict_objs2


if __name__ == '__main__':
    data_dict = index()
    num_dict = pagenum()
    for i in range(len(data_dict)):
        item = data_dict[i]
        ReguData(total_num=item['total_num'],
                regu_name=item['regu_name'],
                regu_paper_num=item['regu_paper_num'],
                regu_department=item['regu_department'],
                regu_dates=item['regu_dates'],
                regu_status=item['regu_status'],
                regu_condition=item['regu_condition'],
                regu_num=item['regu_num']).save()



    for j in range(len(num_dict)):
        number = num_dict[j]
        ReguNum(
            Link_Page_num=number['Link_Page_num']
        ).save()



