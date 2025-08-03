from django.shortcuts import render
from django.http import HttpResponse 


def calculate():
    x = 1
    y = 5
    
    return x
# Create your views here.
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name' : 'Marcus'}) 