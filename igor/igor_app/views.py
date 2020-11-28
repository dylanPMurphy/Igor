from django.shortcuts import render, redirect, HttpResponse
from login_reg.models import User
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage
import bcrypt 
from .forms import ProfileForm




# Create your views here.
def profile(request):
    user = User.objects.get(id=request.session['userid'])
    try:
        user.profile
    except:
        return redirect('registration/')
    else:
        user = User.objects.get(id=request.session['userid'])
        context = {
            'user':user,
            'users_questions':user.posts.all()
        }
        return render(request, 'mypage.html', context)


def finish_profile(request):
    profile_form = ProfileForm()
    context={
        "profile_form": profile_form,
        "user": User.objects.get(id=request.session['userid'])
    }
    return render(request, 'registration.html', context)


def create_profile(request):
    if request.method == 'POST':
        errors=Profile.objects.profile_validator(request.POST)
        if len(errors) !=0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/create')
        form = ProfileForm(request.POST, request.FILES) 
        owner_id=request.session['userid']
        workout_type =request.POST.getlist('workout_type')
        Profile.objects.create(
            owner=User.objects.get(id=owner_id),
            first_name=request.POST['first_name'],
            occupation=request.POST['occupation'],
            about=request.POST['about'],
            img=request.FILES['img']
        )

    print(request.FILES)
    return redirect('/igor/')



def about(request):
    return render(request, 'about.html')

def questions(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'authenticated_user':user,
        'questions':Question.objects.all()
    }

    return render(request, 'want_ad.html', context)

def ask_question(request):
    if request.method =="POST":
        if 'userid' in request.session:
            authenticated_user = User.objects.get(id=request.session['userid'])
            question_content = request.POST['question_content']
            question_specialty = request.POST['specialty']
            Question.objects.create(
                user_who_posted = authenticated_user,
                content = question_content,
                specialty = question_specialty
            )
            return redirect('/igor/')
        else:
            return HttpResponse("ERROR NO USER LOGGED IN")
    else:
        return HttpResponse("ERROR USE POST ROUTE")


def view_question(request, question_id):
    if 'userid' in request.session:
        authenticated_user = User.objects.get(id=request.session['userid'])

        context = {
            'authenticated_user': authenticated_user,
            'selected_question': Question.objects.get(id=question_id)
        }
        return render(request, 'results.html', context)
    else:
        return HttpResponse("ERROR NO USER LOGGED IN")


def answer_question(request, question_id):
    if request.method =="POST":
        if 'userid' in request.session:
            authenticated_user = User.objects.get(id=request.session['userid'])
            question_to_answer = Question.objects.get(id=question_id)
            answer_content =  request.POST['answer_content']
            Answer.objects.create(
                content = answer_content,
                user_who_posted = authenticated_user,
                parent_question = question_to_answer
            )
            return redirect('/igor/questions/'+str(question_id))
