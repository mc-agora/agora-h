from django.shortcuts import render, redirect, get_object_or_404
from .models import RawData, LawData, ReguData

#from boards.models import Board, Comment
#from boards.forms import BoardForm, CommentForm

from django.core.paginator import Paginator # paging 을 하기 위해 사용
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return render(request, 'parsed_data/index.html')

@login_required()
def GOV(request):
    Raws = RawData.objects.all()[::-1]
    paginator = Paginator(Raws, 10)
    page = request.GET.get('page')
    Raws_lists = paginator.get_page(page)

    context = {'Raws': Raws, 'Raws_lists': Raws_lists,}
    return render(request, 'parsed_data/GOV.html', context)


@login_required()
def ASSEM(request):
    Laws = LawData.objects.all()[::-1]
    paginator = Paginator(Laws, 10)
    page = request.GET.get('page')
    Laws_lists = paginator.get_page(page)

    context = {'Laws': Laws, 'Laws_lists': Laws_lists}
    return render(request, 'parsed_data/ASSEM.html', context)


@login_required()
def ASSEM_REGU(request):
    Regus = ReguData.objects.all()[::-1]
    paginator = Paginator(Regus, 10)
    page = request.GET.get('page')
    Regus_lists = paginator.get_page(page)

    context = {'Regus': Regus, 'Regus_lists': Regus_lists}
    return render(request, 'parsed_data/ASSEM_REGU.html', context)


@login_required()
def GOV_DETAIL(request, gov_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    context = {'raw': raw}
    return render(request, 'parsed_data/gov_detail.html', context)

@login_required()
def ASSEM_DETAIL(request, assem_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    context = {'law': law}
    return render(request, 'parsed_data/assem_detail.html', context)

@login_required()
def REGU_DETAIL(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    context = {'regu': regu}
    return render(request, 'parsed_data/regu_detail.html', context)