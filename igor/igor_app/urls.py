from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.profile),
    path('registration/', views.finish_profile),
    path('create/', views.create_profile),
    path('about/', views.about),
    path('questions/', views.questions),
    path('questions/ask/', views.ask_question),
    path('questions/<int:question_id>/', views.view_question),
    path('questions/<int:question_id>/answer', views.view_question)

]