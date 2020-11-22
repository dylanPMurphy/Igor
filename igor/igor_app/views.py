from django.shortcuts import render
from login_reg.models import User
from .models import *

# Create your views here.
def profile(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'user':user
    }
    return render(request, 'mypage.html', context)

def about(request):
    return render(request, 'about.html')

def questions(request):
    return render(request, 'want_ad.html')
