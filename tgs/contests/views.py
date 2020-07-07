from django.shortcuts import render

# Create your views here.

def daily(request):
    return render(request,'contests/daily.html',{'daily_disabled':'disabled'})

def weekly(request):
    return render(request,'contests/weekly.html',{'weekly_disabled':'disabled'})

def monthly(request):
    return render(request,'contests/monthly.html',{'monthly_disabled':'disabled'})
