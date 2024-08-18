from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import studentreg
from .models import user

# Create your views here.

# this function is for add and show new item
def add_show(request):
    if request.method == "POST":
        fm = studentreg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = user(name = nm,email = em, password = pwd)
            reg.save()
        else:
            # Handle form errors here
            print("Form errors:", fm.errors)
        fm = studentreg()
    else:
        fm = studentreg()
    
    stud = user.objects.all()
    
    return render(request,'enroll/addandshow.html',{'form':fm, 'student':stud })


def update_data(request,id):
    if request.method == "POST":
        pi = user.objects.get(pk = id)
        fm = studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk = id)
        fm = studentreg(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})


def deletedata(request,id):
    if request.method == "POST":
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')