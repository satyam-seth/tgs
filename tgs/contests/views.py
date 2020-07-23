from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from contests.models import Daily,Weekly,Monthly,TGS_Weeks,Djoin,Wjoin,Mjoin
from contests.forms import JoinFrom
from datetime import datetime

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
    elif ctype=='TGS Weeks':
        contests=TGS_Weeks.objects.all().order_by('date')
        context={
            'tgs_weeks_disabled':'disabled',
            'ctype':ctype,
            'contests':contests,
            }
    return render(request,'contests/contests_list.html',context)

def daily_join(request,cid):
    if request.method=='POST':
        form=JoinFrom(request.POST,request.FILES)
        if form.is_valid():
            tn=form.cleaned_data['team_name']
            lpn=form.cleaned_data['leader_pname']
            spn=form.cleaned_data['second_pname']
            tpn=form.cleaned_data['third_pname']
            fopn=form.cleaned_data['fourth_pname']
            fipn=form.cleaned_data['fifth_pname']
            wn=form.cleaned_data['whats_num']
            el=form.cleaned_data['email']
            pss=form.cleaned_data['pay_ss']
            tl=form.cleaned_data['team_logo']
            current_dt=datetime.now()
            reg=Djoin(date_time=current_dt,cid=cid,team_name=tn,leader_pname=lpn,second_pname=spn,third_pname=tpn,fourth_pname=fopn,fifth_pname=fipn,whats_num=wn,email=el,pay_ss=pss,team_logo=tl)
            reg.save()
            messages.success(request,'Your team has successfully joined the daily contest.')
        else:
            messages.error(request,'Please check and fill all information correctly.')
            return HttpResponseRedirect(str(cid))
        return redirect('home')
    else:
        form=JoinFrom(label_suffix='')
        contest=Daily.objects.get(pk=cid)
        context={
            'contest':contest,
            'ctype':'DAILY',
            'form':form
            }
        return render(request,'contests/join.html',context)

def weekly_join(request,cid):
    if request.method=='POST':
        form=JoinFrom(request.POST,request.FILES)
        if form.is_valid():
            tn=form.cleaned_data['team_name']
            lpn=form.cleaned_data['leader_pname']
            spn=form.cleaned_data['second_pname']
            tpn=form.cleaned_data['third_pname']
            fopn=form.cleaned_data['fourth_pname']
            fipn=form.cleaned_data['fifth_pname']
            wn=form.cleaned_data['whats_num']
            el=form.cleaned_data['email']
            pss=form.cleaned_data['pay_ss']
            tl=form.cleaned_data['team_logo']
            current_dt=datetime.now()
            reg=Wjoin(date_time=current_dt,cid=cid,team_name=tn,leader_pname=lpn,second_pname=spn,third_pname=tpn,fourth_pname=fopn,fifth_pname=fipn,whats_num=wn,email=el,pay_ss=pss,team_logo=tl)
            reg.save()
            messages.success(request,'Your team has successfully joined the weekly contest.')
        else:
            messages.error(request,'Please check and fill all information correctly.')
            return HttpResponseRedirect(str(cid))
        return redirect('home')
    else:
        form=JoinFrom(label_suffix='')
        contest=Weekly.objects.get(pk=cid)
        context={
            'contest':contest,
            'ctype':'WEEKLY',
            'form':form
            }
        return render(request,'contests/join.html',context)

def monthly_join(request,cid):
    if request.method=='POST':
        form=JoinFrom(request.POST,request.FILES)
        if form.is_valid():
            tn=form.cleaned_data['team_name']
            lpn=form.cleaned_data['leader_pname']
            spn=form.cleaned_data['second_pname']
            tpn=form.cleaned_data['third_pname']
            fopn=form.cleaned_data['fourth_pname']
            fipn=form.cleaned_data['fifth_pname']
            wn=form.cleaned_data['whats_num']
            el=form.cleaned_data['email']
            pss=form.cleaned_data['pay_ss']
            tl=form.cleaned_data['team_logo']
            current_dt=datetime.now()
            reg=Mjoin(date_time=current_dt,cid=cid,team_name=tn,leader_pname=lpn,second_pname=spn,third_pname=tpn,fourth_pname=fopn,fifth_pname=fipn,whats_num=wn,email=el,pay_ss=pss,team_logo=tl)
            reg.save()
            messages.success(request,'Your team has successfully joined the monthly contest.')
        else:
            messages.error(request,'Please check and fill all information correctly.')
            return HttpResponseRedirect(str(cid))
        return redirect('home')
    else:
        form=JoinFrom(label_suffix='')
        contest=Monthly.objects.get(pk=cid)
        context={
            'contest':contest,
            'ctype':'MONTHLY',
            'form':form
            }
        return render(request,'contests/join.html',context)