from django.urls import path
from contests import views

urlpatterns=[
    path('<str:ctype>/', views.contest_show,name='clist'),
    path('daily/<int:cid>', views.daily_join,name='djoin'),
    path('weekly/<int:cid>', views.weekly_join,name='wjoin'),
    path('monthly/<int:cid>', views.monthly_join,name='mjoin'),
]