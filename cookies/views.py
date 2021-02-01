from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.contrib.auth.hashers import make_password

def index(req):
    if req.method == 'GET' :
        print('###########')
        res = render(req, "signup.html")
        res.delete_cookie('pw')
        return res

    if req.COOKIES.get('pw') is not None:
        en_pw = req.COOKIES.get('pw')
        print(en_pw)

    if req.method == 'POST' :
        pw = req.POST.get('password','')
        print(pw)
        res = render(req, "signup.html")
        res.set_cookie('pw', make_password(pw))
        return res

    return render(req ,"signup.html")
