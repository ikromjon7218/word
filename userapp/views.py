from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
import urllib.parse
from django.db import IntegrityError
from mainapp.models import Profil
def register(request):
    # /register/?name=Ibrohimov&gender=male&username=acer&year_of_birth=2007&password=salomsalom
    url = request.get_full_path()  # current URL of the page
    query = urllib.parse.urlparse(url).query
    params = dict(urllib.parse.parse_qsl(query))
    name1 = params.get('name')
    gender1 = params.get('gender')
    username1 = params.get('username')
    password1 = params.get('password')
    year_of_birth1 = params.get('year_of_birth')
    if name1:
        try:
            us = User.objects.create_user(
                username=username1,
                password=password1)
            Profil.objects.create(name=name1,
                                  gender=gender1,
                                  year_of_birth=year_of_birth1,
                                  user=us)
            login(request, us)

            return redirect('/home_page/')
        except IntegrityError:
            return render(request, 'sigin/index.html', {'error': 'Username already exists.'})
    elif username1:
        us = authenticate(request, username=username1, password=password1)
        if us:
            login(request, us)
            return redirect('/home_page/')
    return render(request, 'sigin/index.html')

def logoutview(request):
    logout(request)
    return redirect('/')