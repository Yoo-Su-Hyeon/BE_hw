from django.shortcuts import render, redirect
from .models import Phone

def list(request):
    phones = Phone.objects.all().order_by('name')
    return render(request, 'list.html', {'phones': phones})

def result(request):
    keyword = request.GET.get('keyword', '').strip()
    phones = Phone.objects.filter(name__contains=keyword).order_by('name')

    if keyword != '없는이름' and not phones.exists():
        return redirect('/result/?keyword=없는이름')

    return render(request, 'result.html', {
        'phones': phones,
        'keyword': keyword,
    })