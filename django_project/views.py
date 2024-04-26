# views.py
import requests
import random
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def facts(request):
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']
  
    return render(request, 'random_facts.html', {'fact': fact})

def students(request):
    response2 = requests.get('https://freetestapi.com/api/v1/students?sort=name&order=dec')
    data2 = response2.json()
    random.shuffle(data2) 
    name = data2[0]['name']
    return render(request, 'random_students.html', {'name': name})

def dog(request):
    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']
    return render(request, 'random_image.html', {'dog': dog})