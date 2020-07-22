from django.shortcuts import render

def index(request):
    my_dict = {"insert_me": "I am from views.py"}
    return render(request,'first_app/index.html',context=my_dict)