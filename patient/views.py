from django.shortcuts import render,redirect
from .forms import UpdateDocForm,addPatientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Doctor

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login/')    
def updatedoc(request):
    # current_user = request.user
    # username = current_user.username
    if request.method == 'POST':
        form = UpdateDocForm(request.POST,request.FILES)
        if form.is_valid():
            new_doc = form.save(commit = False)
            # new_doc.user_id = current_user
            new_doc.save()
            return redirect('welcome') 
    else:
        form = UpdateDocForm()
    return render(request,'doctor/profile.html',{"form":form})

@login_required(login_url='/accounts/login/')    
def addpatient(request):
    # current_user = request.user
    # username = current_user.username
    if request.method == 'POST':
        form = addPatientForm(request.POST,request.FILES)
        if form.is_valid():
            new_doc = form.save(commit = False)
            # new_doc.user_id = current_user
            new_doc.save()
            return redirect('index') 
    else:
        form = UpdateDocForm()
    return render(request,'patient/profile.html',{"form":form})

