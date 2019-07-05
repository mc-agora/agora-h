from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


### 자신의 페이지
@login_required()
def userprofile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)

    if not person.image:
        pic_url = ""
    else:
        pic_url = person.image.url
    context = {
        'id': person.username,
        'name': person.user_name,
        'date_of_birth': person.date_of_birth,
        'job': person.job,
        'gender': person.gender,
        'pic': pic_url,
        'text': person.text
    }
    return render(request, 'mypage/userprofile.html', context)


