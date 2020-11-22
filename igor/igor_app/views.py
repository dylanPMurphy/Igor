from django.shortcuts import render, HttpResponse

# Create your views here.
def profile(request):
    #profile page
    return render(request, 'pages/profile.html')

def about(request):
    #directs to About Igor
    return render(request, 'pages/about.html')

def questions(request):
    #directs to general Q&A board
    return render(request, 'pages/wanted.html')
