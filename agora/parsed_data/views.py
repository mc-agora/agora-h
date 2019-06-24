from django.shortcuts import render, redirect
from .models import RawData, NumData, LawData, LawNum, ReguData, ReguNum
from django.core.paginator import Paginator # paging 을 하기 위해 사용
from django.contrib.auth.decorators import login_required
from IPython import embed

@login_required()
def index(request):
    Raws = RawData.objects.all()
    Laws = LawData.objects.all()
    Regus = ReguData.objects.all()
    Raw_Page_Num = NumData.objects.all()
    Law_Page_Num = LawNum.objects.all()
    Regu_page_Num = ReguNum.objects.all()
    paginator1 = Paginator(Raws, 10)
    paginator2 = Paginator(Laws, 10)
    paginator3 = Paginator(Regus, 10)
    page = request.GET.get('page')
    Raws_lists = paginator1.get_page(page)
    Laws_lists = paginator2.get_page(page)
    Regus_lists = paginator3.get_page(page)

    context={'Raws': Raws,
             'Laws':Laws,
             'Regus':Regus ,
             'Raws_lists': Raws_lists,
             'Laws_lists':Laws_lists,
             'Regus_lists':Regus_lists,
             'Raw_Page_Num':Raw_Page_Num,
             'Law_Page_Num':Law_Page_Num,
             'Regu_page_Num':Regu_page_Num,
             }
    # embed()
    return render(request, 'parsed_data/index.html', context)