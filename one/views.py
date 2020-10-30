from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from one.models import *
# Create your views here.


def index1(request):
    resp = redirect(reverse("one:index2"))
    return resp


def index2(request):
    name = request.session.get("name")
    context = {"name":name}
    return render(request, 'one/index.html', context=context)


def static(request):
    good_list = Good.objects.all()
    context = {"good_list":good_list}
    return render(request, 'one/charts.html', context=context)


def detail(request, id):
    good = get_object_or_404(Good, id=id)
    return render(request, 'one/detail.html', context={"good":good})


def home(request):
    return render(request, "one/home.html")


def get_data(request):
    import json
    data = {"name":"Tom", "age":40}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")


def register(request):
    print(request.GET)
    return render(request, "one/register.html")


def save_data(request):
    name = request.POST.get("username")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    email = request.POST.get("email")
    hobby_list = request.POST.getlist("hobby")
    print(hobby_list)
    file = request.FILES.get("file")
    # with open("test.jpg", "wb") as f:
    #     for chunk in file.chunks():
    #         f.write(chunk)

    PeopleInfo.objects.create(name=name, password=password, email=email)
    request.session["name"] = name
    resp = redirect(reverse("one:index1"))
    return resp