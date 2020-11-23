from django.db import models
from login_reg.models import *
# Create your models here.


SPECIALTY_CHOICES =[
    ('Food', "Food"),
    ("Cars","Cars"),
    ("Clothes", "Clothes"),
    ("Computer", "Computer"),
    ("Health", "Health")
]
class Question(models.Model):
    content = models.TextField()
    user_who_posted = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    specialty = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    content = models.TextField()
    user_who_answered = models.ForeignKey(User, related_name="answered_questions", on_delete = models.CASCADE)
    parent_question = models.ForeignKey(Question, related_name="answers", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)