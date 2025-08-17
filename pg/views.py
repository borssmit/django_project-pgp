from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, '/home/bors/django_projects/pgp/pg/templates/pg/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIKLMNOPRSTUWXZY'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+?><'))
    
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, '/home/bors/django_projects/pgp/pg/templates/pg/password.html', {'password':thepassword})

def about(request):
    return render(request, '/home/bors/django_projects/pgp/pg/templates/pg/about.html')


