from django.shortcuts import render


def index(req):
    return render(req, 'reports/index.html')


def mybase(req):
    return render(req, 'account/mybase.html')

