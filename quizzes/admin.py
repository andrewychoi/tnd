from django.contrib import admin
from quizzes.models import Quiz, Question, Answer

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)