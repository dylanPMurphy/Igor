from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.profile),
    path(r'logout', include('login_reg.urls')),
    path('about/', views.about),
    path('questions', views.questions),
]