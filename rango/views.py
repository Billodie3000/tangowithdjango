from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    #Construct dictionary to pass to the template engine
    context_dict = {'boldmessage': "I am bold font from the context"}

    #Return a rendered response to the client.
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango'>Home</a>")
