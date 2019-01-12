from django.shortcuts import render
from django.http import HttpResponse
from vennelaapp import forms
from vennelaapp.forms import ContactForm
def index(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('data succesfully inserted')
        else:
            print(forms.errors)
    else:
        form=ContactForm()
        return render(request,'index contact.html',{'form':form})

