from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import RawData, LawData, ReguData, Pg_Board, Pg_Comment, Pg_Board2, Pg_Comment2, Pa_Board, Pa_Board2, Pa_Comment, Pa_Comment2,Par_Board, Par_Board2, Par_Comment, Par_Comment2, NumData, LawNum,ReguNum
from .forms import Pg_BoardForm, Pg_CommentForm, Pg_BoardForm2, Pg_CommentForm2, Pa_BoardForm, Pa_BoardForm2, Pa_CommentForm, Pa_CommentForm2, Par_BoardForm, Par_BoardForm2, Par_CommentForm, Par_CommentForm2

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
    raw_num = NumData.objects.all()[::-1]

    paginator = Paginator(Raws, 10)
    page = request.GET.get('page')
    Raws_lists = paginator.get_page(page)

    paginator2 = Paginator(raw_num, 10)
    page2 = request.GET.get('page')
    raw_num_lists = paginator2.get_page(page2)


    context = {'Raws': Raws, 'Raws_lists': Raws_lists,'raw_num':raw_num,'raw_num_lists':raw_num_lists}
    return render(request, 'parsed_data/GOV.html', context)


@login_required()
def ASSEM(request):
    Laws = LawData.objects.all()[::-1]
    law_num = LawNum.objects.all()[::-1]
    paginator = Paginator(Laws, 10)
    page = request.GET.get('page')
    Laws_lists = paginator.get_page(page)

    paginator2 = Paginator(law_num, 10)
    page2 = request.GET.get('page')
    law_num_lists = paginator2.get_page(page2)

    context = {'Laws': Laws, 'Laws_lists': Laws_lists, 'law_num':law_num,'law_num_lists':law_num_lists}
    return render(request, 'parsed_data/ASSEM.html', context)


@login_required()
def ASSEM_REGU(request):
    Regus = ReguData.objects.all()[::-1]
    regu_num = ReguNum.objects.all()[::-1]
    paginator = Paginator(Regus, 10)
    page = request.GET.get('page')
    Regus_lists = paginator.get_page(page)

    paginator2 = Paginator(regu_num, 10)
    page2 = request.GET.get('page')
    regu_num_lists = paginator2.get_page(page2)

    context = {'Regus': Regus, 'Regus_lists': Regus_lists, 'regu_num':regu_num,'regu_num_lists':regu_num_lists}
    return render(request, 'parsed_data/ASSEM_REGU.html', context)


@login_required()
def GOV_DETAIL(request, gov_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    boards = Pg_Board.objects.all()[::-1]

    boardcount = Pg_Board.objects.count()
    board_list = Pg_Board.objects.all().order_by('id')

    paginator = Paginator(boards, 5)
    page = request.GET.get('page')
    raw_lists = paginator.get_page(page)

    boards2 = Pg_Board2.objects.all()[::-1]
    boardcount2 = Pg_Board2.objects.count()

    board_list2 = Pg_Board2.objects.all().order_by('id')
    paginator2 = Paginator(boards2, 5)
    page2 = request.GET.get('page')
    raw_lists2 = paginator2.get_page(page2)


    context = {'raw': raw, 'boardcount': boardcount, 'board_list':board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2':board_list2, 'boards2':boards2,'raw_lists':raw_lists,"raw_lists2":raw_lists2}
    return render(request, 'parsed_data/gov_detail.html', context)

@login_required()
def ASSEM_DETAIL(request, assem_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    boards = Pa_Board.objects.all()[::-1]
    boardcount = Pa_Board.objects.count()
    board_list = Pa_Board.objects.all().order_by('id')
    paginator = Paginator(boards, 5)
    page = request.GET.get('page')
    law_lists = paginator.get_page(page)

    boards2 = Pa_Board2.objects.all()[::-1]
    boardcount2 = Pa_Board2.objects.count()
    board_list2 = Pa_Board2.objects.all().order_by('id')
    paginator2 = Paginator(boards2, 5)
    page2 = request.GET.get('page')
    law_lists2 = paginator2.get_page(page2)

    context = {'law': law, 'boardcount': boardcount, 'board_list': board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2': board_list2, 'boards2':boards2,'law_lists':law_lists,"law_lists2":law_lists2}
    return render(request, 'parsed_data/assem_detail.html', context)

@login_required()
def REGU_DETAIL(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)

    boards = Par_Board.objects.all()[::-1]
    boardcount = Par_Board.objects.count()
    board_list = Par_Board.objects.all().order_by('id')
    paginator = Paginator(boards, 5)
    page = request.GET.get('page')
    regu_lists = paginator.get_page(page)

    boards2 = Par_Board2.objects.all()[::-1]
    boardcount2 = Par_Board2.objects.count()
    board_list2 = Par_Board2.objects.all().order_by('id')
    paginator2 = Paginator(boards2, 5)
    page2 = request.GET.get('page')
    regu_lists2 = paginator2.get_page(page2)


    context = {'regu': regu, 'boardcount': boardcount, 'board_list': board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2': board_list2, 'boards2':boards2,'regu_lists':regu_lists,"regu_lists2":regu_lists2}
    return render(request, 'parsed_data/regu_detail.html', context)

################################ GOV ###################################################

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def ga_new(request, gov_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    if request.method == 'POST':
        form = Pg_BoardForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:ga_agree', gov_pk, board.pk)
    else:
        form = Pg_BoardForm()
    context = {'form': form, 'raw': raw}
    return render(request, 'parsed_data/R_form.html', context)

@login_required()
def ga_agree(request, gov_pk, ga_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    board = get_object_or_404(Pg_Board, pk=ga_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.pd_comments.all()
    comment_form = Pg_CommentForm()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'raw':raw,
    }
    return render(request, 'parsed_data/ga_a_detail.html', context)

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def gd_new(request, gov_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    if request.method == 'POST':
        form = Pg_BoardForm2(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:ga_disagree', gov_pk, board.pk)
    else:
        form = Pg_BoardForm2()
    context = {'form': form, 'raw':raw}
    return render(request, 'parsed_data/R_form.html', context)

@login_required()
def ga_disagree(request, gov_pk, gd_pk):
    raw = get_object_or_404(RawData, pk=gov_pk)
    board = get_object_or_404(Pg_Board2, pk=gd_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.pd_comments2.all()
    comment_form = Pg_CommentForm2()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'raw':raw,
    }
    return render(request, 'parsed_data/ga_d_detail.html', context)

################################# ASSEM ################################################

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def aa_new(request, assem_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    if request.method == 'POST':
        form = Pa_BoardForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:aa_agree', assem_pk, board.pk)
    else:
        form = Pa_BoardForm()
    context = {'form': form, 'law':law}
    return render(request, 'parsed_data/La_form.html', context)

@login_required()
def aa_agree(request, assem_pk, aa_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    board = get_object_or_404(Pa_Board, pk=aa_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.pa_comments.all()
    comment_form = Pa_CommentForm()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'law':law,
    }
    return render(request, 'parsed_data/aa_a_detail.html', context)

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def ad_new(request, assem_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    if request.method == 'POST':
        form = Pa_BoardForm2(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:aa_disagree', assem_pk, board.pk)
    else:
        form = Pa_BoardForm2()
    context = {'form': form, 'law':law}
    return render(request, 'parsed_data/La_form.html', context)

@login_required()
def aa_disagree(request, assem_pk, ad_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    board = get_object_or_404(Pa_Board2, pk=ad_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.pa_comments2.all()
    comment_form = Pa_CommentForm2()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'law':law,
    }
    return render(request, 'parsed_data/aa_d_detail.html', context)

################################## REGU ################################################

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def ra_new(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    if request.method == 'POST':
        form = Par_BoardForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:ra_agree', regu_pk, board.pk)
    else:
        form = Par_BoardForm()
    context = {'form': form, 'regu':regu}
    return render(request, 'parsed_data/Re_form.html', context)

@login_required()
def ra_agree(request, regu_pk, ra_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    board = get_object_or_404(Par_Board, pk=ra_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.par_comments.all()
    comment_form = Par_CommentForm()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'regu':regu,
    }
    return render(request, 'parsed_data/ra_a_detail.html', context)

@login_required() # 로그인한 사람만 글을 쓸 수 있도록
def rd_new(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    if request.method == 'POST':
        form = Par_BoardForm2(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            board = form.save(commit=False)   # 잠시 저장되지 않게 함
            board.user = request.user
            board.save()
            return redirect('parsed_data:ra_disagree', regu_pk, board.pk)
    else:
        form = Par_BoardForm2()
    context = {'form': form, 'regu':regu}
    return render(request, 'parsed_data/Re_form.html', context)

@login_required()
def ra_disagree(request, regu_pk, rd_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    board = get_object_or_404(Par_Board2, pk=rd_pk)
    person = get_object_or_404(get_user_model(), pk=board.user.pk)  # 글쓴 사람
    comments = board.par_comments2.all()
    comment_form = Par_CommentForm2()
    context = {
        'board': board,
        'comments': comments,
        'comment_form': comment_form,
        'person': person,
        'regu':regu,
    }
    return render(request, 'parsed_data/ra_d_detail.html', context)

######################################################
def like(request, gov_pk):
    gov = get_object_or_404(RawData, pk=gov_pk)
    if request.user in gov.like_users.all():
        gov.like_users.remove(request.user)
    else:
        gov.like_users.add(request.user)
        # embed()
    return redirect('parsed_data:gov_detail', gov_pk)
######################################################
def like2(request, assem_pk):
    assem = get_object_or_404(LawData, pk=assem_pk)
    if request.user in assem.like2_users.all():
        assem.like2_users.remove(request.user)
    else:
        assem.like2_users.add(request.user)
    return redirect('parsed_data:assem_detail', assem_pk)
####################################################
def like3(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    if request.user in regu.like3_users.all():
        regu.like3_users.remove(request.user)
    else:
        regu.like3_users.add(request.user)                                  #
    return redirect('parsed_data:regu_detail', regu_pk)
####################################################
def unlike(request, gov_pk):
    gov = get_object_or_404(RawData, pk=gov_pk)
    if request.user in gov.unlike_users.all():
        gov.unlike_users.remove(request.user)
    else:
        gov.unlike_users.add(request.user)
    return redirect('parsed_data:gov_detail', gov_pk)
#########################################################
def unlike2(request, assem_pk):
    assem = get_object_or_404(LawData, pk=assem_pk)
    if request.user in assem.unlike2_users.all():
        assem.unlike2_users.remove(request.user)
    else:
        assem.unlike2_users.add(request.user)
    return redirect('parsed_data:assem_detail', assem_pk)
##########################################################
def unlike3(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)
    if request.user in regu.unlike3_users.all():
        regu.unlike3_users.remove(request.user)
    else:
        regu.unlike3_users.add(request.user)
    return redirect('parsed_data:regu_detail', regu_pk)