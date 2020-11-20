from django.db import models
from login_reg.models import *
# Create your models here.


class Specialty(models.Model):
    name = models.CharField(max_length=45)
    users_with_specialty = models.ManyToManyField(User, "specialty")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    content = models.TextField()
    user_who_posted = models.ForiegnKey(User, related_name="posts", on_delete = models.CASCADE)
    specialty = models.ForiegnKey(Specialty, related_name="questions_in_specialty", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    content = models.TextField()
    user_who_answered = models.ForiegnKey(User, related_name="answered_questions", on_delete = models.CASCADE)
    parent_question = models.ForiegnKey(Question, related_name="answers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)