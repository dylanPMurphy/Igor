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
            return reditect('/igor/questions/'+str(question_id))
