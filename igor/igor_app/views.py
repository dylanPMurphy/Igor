from django.shortcuts import render
from login_reg.models import User
from .models import *

# Create your views here.
def profile(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user':user
    }
    return render(request, 'pages/profile.html', context)

def about(request):
    return render(request, 'pages/about.html')

def questions(request):
    return render(request, 'pages/wanted.html')
