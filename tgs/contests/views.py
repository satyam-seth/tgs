from django.shortcuts import render
from contests.models import Daily,Weekly,Monthly

# Create your views here.

def daily(request):
    contests=Daily.objects.all().order_by('d_date')
    context={
        'daily_disabled':'disabled',
        'contests':contests,
        }
    return render(request,'contests/daily.html',context)

def weekly(request):
    contests=Weekly.objects.all().order_by('w_date')
    context={
        'weekly_disabled':'disabled',
        'contests':contests,
        }
    return render(request,'contests/weekly.html',context)

def monthly(request):
    contests=Monthly.objects.all().order_by('m_date')
    context={
        'monthly_disabled':'disabled',
        'contests':contests,
        }
    return render(request,'contests/monthly.html',context)