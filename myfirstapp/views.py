from django.shortcuts import render

# Create your views here.
users_list = []


def hello(request):
    return render(request, 'hello.html')


def users(request, name):
    users_list.append(name)
    return render(request, 'users.html', {'name': name, 'users': users_list})
