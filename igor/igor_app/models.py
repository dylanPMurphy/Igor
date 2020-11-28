from django.db import models
from login_reg.models import *
from django.forms import ModelForm
import bcrypt
import re
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

class ProfileManager(models.Manager):
    def profile_validator(self, postData):
        errors={}
        if len(postData['first_name'])==0:
            errors['first_name']='First Name Is A Required Field'
        if len(postData['occupation'])==0:
                errors['occupation']= 'Occupation Is A Required Field'
        if len(postData['about'])==0:
                errors['about']= 'About Me Is A Required Field'
        return errors

class Profile(models.Model):
    owner=models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    first_name=models.CharField(max_length=20)
    occupation=models.CharField(max_length=20)
    about=models.TextField()
    img=models.ImageField(upload_to ="img/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ProfileManager()
