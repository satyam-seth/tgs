from django.shortcuts import render
from contests.models import Daily,Weekly,Monthly,Djoin

# Create your views here.

def contest_show(request,ctype):
    if ctype=='daily':
        contests=Daily.objects.all().order_by('date')
        context={
            'daily_disabled':'disabled',
            'ctype':ctype,
            'contests':contests,
            }
    elif ctype=='weekly':
        contests=Weekly.objects.all().order_by('date')
        context={
            'weekly_disabled':'disabled',
            'ctype':ctype,
            'contests':contests,
            }
    elif ctype=='monthly':
        contests=Weekly.objects.all().order_by('date')
        context={
            'monthly_disabled':'disabled',
            'ctype':ctype,
            'contests':contests,
            }
    return render(request,'contests/contests_list.html',context)

def daily_join(request,cid):
    contest=Daily.objects.get(pk=cid)
    return render(request,'contests/join.html',{'contest':contest,'ctype':'DAILY'})

def weekly_join(request,cid):
    contest=Weekly.objects.get(pk=cid)
    return render(request,'contests/join.html',{'contest':contest,'ctype':'WEEKLY'})

def monthly_join(request,cid):
    contest=Monthly.objects.get(pk=cid)
    return render(request,'contests/join.html',{'contest':contest,'ctype':'MONTHLY'})