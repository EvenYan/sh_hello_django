from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from one.models import *
# Create your views here.


def index1(request):
    resp = HttpResponseRedirect(reverse("one:index2"))
    return resp


def index2(request):
    return HttpResponse("新的接口")



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
    return HttpResponse("保存成功！")