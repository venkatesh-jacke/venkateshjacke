from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Contact


def welcome(request):
    return render(request, 'demoapp/welcome.html')


def about(request):
    return render(request, 'demoapp/about.html')


def projects(request):
    return render(request, 'demoapp/projects.html')


def cp(request):
    return render(request, 'demoapp/competitiveprogramming.html')


def contact(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        # print(name,email,phone,msg)
        ins = Contact(name=name, email=email, phone=phone, msg=msg)
        ins.save()
        print("The data has been written to the DB")
    return render(request, 'demoapp/contact.html')
