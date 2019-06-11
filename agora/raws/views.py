from django.shortcuts import render, redirect
import bs4
import requests
import re
import math


def index(request):
    def cleanText(readData):
        text = re.sub('[,"\n\t\r ]', "", readData)
        return text
    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    html = requests.get(f'https://opinion.lawmaking.go.kr/gcom/govLm?pageIndex=1').text
    soup = bs4.BeautifulSoup(html, "html.parser")
    ranks = soup.select('.tbl_typeA tr td')
    data = []
    for i in range(len(ranks)):
        data.append(cleanText(ranks[i].text))
    groups = []
    for group in chunker(data, 6):
        groups.append(group)
    total_page = math.ceil(int(groups[0][0]) / 10)
    context={'groups':groups, 'total_page':total_page}
    return render(request, 'raws/index.html',context)