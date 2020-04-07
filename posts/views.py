from django.shortcuts import render

# Create your views here.


def home(requests):
    return render(requests, "posts/home.html")


def passView(requests):
    data = {"message":"장고를 잘하자"}
    data.update({"important_message":"코로나 조심하세요"})
    return render(requests, "posts/pass.html", data)
