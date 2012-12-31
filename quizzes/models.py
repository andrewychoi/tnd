from django.db import models

from courses.models import Clip

class Quiz(models.Model):
    clip = models.ForeignKey(Clip)
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    text = models.TextField()
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    is_correct_answer = models.BooleanField()
    
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)