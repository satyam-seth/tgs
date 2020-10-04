from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('update/<int:id>/', views.update_winner, name='update_winner'),
]