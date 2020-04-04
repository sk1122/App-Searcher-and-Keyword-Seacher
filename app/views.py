# Importing Important Libraries

# Django Libraries
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Local Modules for Models, Forms and Scraping
from .models import GooglePlayModel, AppleAppModel, Keyword
from .forms import GooglePlayStore, AppleAppStore, KeyWordFinder, CreateUser
from .scrape import GooglePlay, AppleApp, KeywordFinder

from random import randint


@login_required(login_url='app:login')
def index(request):
    """ Home Page / Starting Page """

    return render(request, 'index.html')


# App Searcher

@login_required(login_url='app:login')
def app_searcher(request):
    """
        App Search
        :form - Google Play Store Form
        :form1 - Apple App Store Form
        :data - Data from Google Play Model
        :data1 - Data from Apple App Model
    """

    form = GooglePlayStore()
    form1 = AppleAppStore()
    data = GooglePlayModel.objects.filter(user=request.user)
    print(data)
    data1 = AppleAppModel.objects.filter(user=request.user)
    context = {
        'form': form,
        'form1': form1,
        'data': data.reverse(),
        "data1": data1.reverse()
    }
    return render(request, 'app.html', context)


@login_required(login_url='app:login')
def ajax_app_searcher(request):
    """
        Ajax Function to update App list without reloading
        for Google Play Store
    """

    form = GooglePlayStore()
    if request.is_ajax and request.method == 'POST':
        form = GooglePlayStore(request.POST)
        if form.is_valid():
            ids = form.cleaned_data["app_id"]

            data = GooglePlayModel.objects.filter(user=request.user, name=ids)
            print(data)
            if data:
                form = GooglePlayStore()
                return JsonResponse({"error": "Already Exixts"}, status=400)
            else:
                a = GooglePlay(ids)
                b = a.details()
                new_app = GooglePlayModel(
                    name=ids, app_name=b[0], image=b[1], developer=b[2], description=b[3], downloads=b[4], reviews=b[5], ratings=b[6])
                new_app.save()
                request.user.googleplay.add(new_app)
                ser_app = serializers.serialize('json', [new_app, ])
                return JsonResponse({"app": ser_app}, status=200)

        else:
            form = GooglePlayStore()
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": form.errors}, status=400)


@login_required(login_url='app:login')
def apple_ajax_app_searcher(request):
    """
        Ajax Function to update App list without reloading
        for Apple App Store
    """

    form = AppleAppStore()
    if request.is_ajax and request.method == 'POST':
        form = AppleAppStore(request.POST)
        if form.is_valid():
            app_name = form.cleaned_data["app_name"]
            app_id = form.cleaned_data["app_id"]

            data = AppleAppModel.objects.filter(
                user=request.user, app_name=app_name)

            if data:
                form = AppleApp()
                return JsonResponse({"error": "Hello World"}, status=400)
            else:
                a = AppleApp(app_name, app_id)
                b = a.details()

                new_app = AppleAppModel(
                    app_name=b[0], image=b[1], developer=b[2], description=b[3], reviews=b[4], ratings=b[5])
                new_app.save()
                request.user.appleapp.add(new_app)
                ser_app = serializers.serialize('json', [new_app, ])
                return JsonResponse({"app": ser_app}, status=200)
        else:
            form = AppleApp()
            return JsonResponse({"error": "Hello World"}, status=400)
    return JsonResponse({"error": "Hello World"}, status=400)


# Keyword Finder

@login_required(login_url='app:login')
def keyword_finder(request):
    """
        Searchs for Keywords and Add it to Database
    """

    form = KeyWordFinder()
    data = Keyword.objects.filter(user=request.user)

    context = {
        "form": form,
        'data': data
    }
    return render(request, 'key.html', context)


@login_required(login_url='app:login')
def ajax_keyword_finder(request):
    """

    Ajax Function for Handling REquests to add Keywords and URL's to DB

    """

    form = KeyWordFinder()
    if request.is_ajax and request.method == 'POST':
        form = KeyWordFinder(request.POST)
        if form.is_valid():
            url = form.cleaned_data["site_url"]
            cl = KeywordFinder(url)
            data = cl.keywords()
            if data:

                data3 = data.split(',')
                recommended = []
                for _ in range(3):
                    start = 0
                    end = len(data3) - 1
                    rec_keyword = randint(start, end)
                    recommended.append(data3[rec_keyword])

                new_keyword = Keyword(
                    url=url, keyword=data, rec_keyword=str(', '.join(recommended)))
                new_keyword.save()
                request.user.keywords.add(new_keyword)

                ser_keyword = serializers.serialize("json", [new_keyword, ])
                return JsonResponse({"keyword": ser_keyword}, status=200)
            else:
                return JsonResponse({"error": "data not found"}, status=400)
        else:
            form = KeyWordFinder()
            return JsonResponse({"error": form.error}, status=400)
    return JsonResponse({"error": form.error}, status=400)


# User Authentication for Showing Personlized Data

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username OR password is Invalid")
    context = {}
    return render(request, 'login.html', context)


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data["username"]
                messages.success(
                    request, f"Account Was Created Successfully for {username}")
                return redirect('/login')
            else:
                messages.error(request, "Registration Failed")
    form = CreateUser()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')
