from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name="home"),
    path('app/', views.app_searcher, name="app_searcher"),
    path('app/ajax/', views.ajax_app_searcher, name="ajax"),
    path('app/ajax/apple', views.apple_ajax_app_searcher, name="apple"),
    path('keyword/', views.keyword_finder, name="keyword"),
    path('keyword/ajax', views.ajax_keyword_finder, name="ajax_keyword"),
    path("login/", views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout")
]
