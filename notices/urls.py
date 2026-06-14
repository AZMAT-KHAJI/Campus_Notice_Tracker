# notices/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Notice CRUD
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('create/', views.create_notice, name='create_notice'),
    path('update/<int:pk>/', views.update_notice, name='update_notice'),
    path('delete/<int:pk>/', views.delete_notice, name='delete_notice'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='notices/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
