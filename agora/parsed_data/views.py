from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import RawData, LawData, ReguData, Pg_Board, Pg_Comment, Pg_Board2, Pg_Comment2, Pa_Board, Pa_Board2, Pa_Comment, Pa_Comment2,Par_Board, Par_Board2, Par_Comment, Par_Comment2
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
    boards = Pg_Board.objects.all()[::-1]
    boardcount = Pg_Board.objects.count()
    board_list = Pg_Board.objects.all().order_by('id')

    boards2 = Pg_Board2.objects.all()[::-1]
    boardcount2 = Pg_Board2.objects.count()
    board_list2 = Pg_Board2.objects.all().order_by('id')

    context = {'raw': raw, 'boardcount': boardcount, 'board_list':board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2':board_list2, 'boards2':boards2}
    return render(request, 'parsed_data/gov_detail.html', context)

@login_required()
def ASSEM_DETAIL(request, assem_pk):
    law = get_object_or_404(LawData, pk=assem_pk)
    boards = Pa_Board.objects.all()[::-1]
    boardcount = Pa_Board.objects.count()
    board_list = Pa_Board.objects.all().order_by('id')

    boards2 = Pa_Board2.objects.all()[::-1]
    boardcount2 = Pa_Board2.objects.count()
    board_list2 = Pa_Board2.objects.all().order_by('id')

    context = {'law': law, 'boardcount': boardcount, 'board_list': board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2': board_list2, 'boards2':boards2}
    return render(request, 'parsed_data/assem_detail.html', context)

@login_required()
def REGU_DETAIL(request, regu_pk):
    regu = get_object_or_404(ReguData, pk=regu_pk)

    boards = Par_Board.objects.all()[::-1]
    boardcount = Par_Board.objects.count()
    board_list = Par_Board.objects.all().order_by('id')

    boards2 = Par_Board2.objects.all()[::-1]
    boardcount2 = Par_Board2.objects.count()
    board_list2 = Par_Board2.objects.all().order_by('id')

    context = {'regu': regu, 'boardcount': boardcount, 'board_list': board_list, 'boards':boards,
               'boardcount2': boardcount2, 'board_list2': board_list2, 'boards2':boards2}
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


###################  좋아요 함수 ##############
@login_required()
def likepg(request, gov_pk):
    board = get_object_or_404(Pg_Board, pk=gov_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:gov_detail', gov_pk)

@login_required()
def likepg2(request, gov_pk):
    board = get_object_or_404(Pg_Board2, pk=gov_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:gov_detail', gov_pk)

@login_required()
def likepa(request, assem_pk):
    board = get_object_or_404(Pa_Board, pk=assem_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:assem_detail', assem_pk)

@login_required()
def likepa2(request, assem_pk):
    board = get_object_or_404(Pa_Board2, pk=assem_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:assem_detail',assem_pk)

@login_required()
def likepar(request, regu_pk):
    board = get_object_or_404(Par_Board, pk=regu_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:regu_detail',regu_pk)

@login_required()
def likepar2(request, regu_pk):
    board = get_object_or_404(Par_Board2, pk=regu_pk)
    if request.user in board.like_users.all(): # 이 게시글에 좋아요를 누른 유저 중 요청을 한 유저(request.user)가 있다면
        board.like_users.remove(request.user)  # 목록에서 지워준다. (즉 좋아요를 취소 한다는 의미)
    else:
        board.like_users.add(request.user)
    return redirect('parsed_data:regu_detail', regu_pk)