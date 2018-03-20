from django.shortcuts import render,redirect
from .forms import UpdateDocForm

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def updatedoc(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateDocForm(request.POST,request.FILES)
        if form.is_valid():
            new_business = form.save(commit = False)
            new_business.user_id =  current_user
            new_business.save()
            return redirect('welcome') 
    else:
        form = UpdateDocForm()
    return render(request,'doctor/profile.html',{"form":form})
