from django.shortcuts import render
from core.models import Winner

# Create your views here.

def home(request):
    first=Winner.objects.get(pk=1)
    second=Winner.objects.get(pk=2)
    third=Winner.objects.get(pk=3)

    context={
        'home_active':'active',
        'home_disabled':'disabled',
        'first':first,
        'second':second,
        'third':third,
        }

    return render(request,'core/home.html',context)

def contact(request):
    return render(request,'core/contact.html',{'contact_active':'active','contact_disabled':'disabled'})

def about(request):
    return render(request,'core/about.html',{'about_active':'active','about_disabled':'disabled'})

def policy(request):
    return render(request,'core/policy.html',{'policy_active':'active','policy_disabled':'disabled'})