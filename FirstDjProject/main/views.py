from django.http import HttpResponse
from .models import Question
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    questions = Question.objects.all()  # Получаем все вопросы
    return render(request, 'home.html', {'questions': questions})