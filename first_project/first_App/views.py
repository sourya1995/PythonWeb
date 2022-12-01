from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm

def index(request):
    return HttpResponse("Hello World!")

def home(request):
    return HttpResponse("Welcome to the home page")

def educative(request):
    return HttpResponse("Welcome to the educative page")

def show_age(request, age):
    return HttpResponse("I am %s years old", age)

def even_or_odd(request, num):
    if(num%2 == 0):
        output="%s is an even number"% num
    else:
        output="%s is an odd number"% num
    return HttpResponse(output)

def forms(request):
    initial_dict = {
        "text": "some initial data",
        "integer": 123
    }
    form = TestForm(request.POST or None, initial=initial_dict)
    data = "None"
    text = "None"
    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
    return render(request, 'first_App/forms.html', {'form':form, 'data':data, 'text':text})

# Create your views here.
