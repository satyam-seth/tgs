from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html',{'home_active':'active','home_disabled':'disabled',})

def contact(request):
    return render(request,'core/contact.html',{'contact_active':'active','contact_disabled':'disabled'})

def about(request):
    return render(request,'core/about.html',{'about_active':'active','about_disabled':'disabled'})

def policy(request):
    return render(request,'core/policy.html',{'policy_active':'active','policy_disabled':'disabled'})