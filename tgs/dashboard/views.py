from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm,WinnerUpdateForm
from core.models import Winner

# Create your views here.

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                messages.success(request,'Logged in Successfully !!')
                return HttpResponseRedirect('/manage/dashboard/')
        else:
            form=LoginForm()
        return render(request,'dashboard/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/manage/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        user=request.user
        full_name=user.get_full_name()

        winners=Winner.objects.all()

        context={
            'dashboard_active':'active',
            'dashboard_disabled':'disabled',
            'full_name':full_name,
            'winners':winners
        }
        return render(request,'dashboard/dashboard.html',context)
    else:
        return HttpResponseRedirect('/manage/login/')

def update_winner(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Winner.objects.get(pk=id)
            form=WinnerUpdateForm(request.POST,request.FILES,instance=pi)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/manage/dashboard')   
        else:
            pi=Winner.objects.get(pk=id)
            form=WinnerUpdateForm(instance=pi)
        return render(request,'dashboard/update_winner.html',{'form':form,'id':id})
    else:
        return HttpResponseRedirect('/login/')