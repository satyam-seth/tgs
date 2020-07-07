from django.urls import path
from contests import views

urlpatterns=[
    path('daily/', views.daily,name='daily'),
    path('weekly/', views.weekly,name='weekly'),
    path('monthly/', views.monthly,name='monthly')
]