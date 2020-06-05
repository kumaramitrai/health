from django.shortcuts import render
from django.http import HttpResponse
from .models import patient



# Create your views here.
def home(request):
    patient_list = patient.objects.all()
    context = {'patient_list': patient_list}    
    return render(request, 'index.html', context)
    


def about(request):
    #return HttpResponse("<h1>hello this is the about page</h1>")
    return render(request, 'about.html',)


def services(request):
        return render(request, 'services.html',)


def ContactUs(request):
        return render(request, 'contactus.html',)

    

    