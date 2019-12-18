from django.contrib import admin

# Register your models here.
from .models import Question, Choice

admin.site.register(Question)   # polls now modifiable admin
admin.site.register(Choice)   # polls now modifiable admin