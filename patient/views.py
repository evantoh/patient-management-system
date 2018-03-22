from django.shortcuts import render,redirect
from .forms import UpdateDocForm,addPatientForm,TreatmentForm,NewNextOfKinForm,NewMedicineForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Doctor,Medicine,NextOfKin,Patient
# Create your views here.
@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    doctor = Doctor.objects.get(id='1')
    return render(request, 'profile.html', {'doctor':doctor,'current_user':current_user})

@login_required(login_url='/accounts/login')    
def welcome(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login')
def update_profile(request, username):
    current_user = request.user
    username = current_user.username
    doctor = Doctor.objects.get(id='1')
    if request.method == 'POST':
        form = UpdateDocForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save()
        return redirect('updatedoc')
    else:
        form = UpdateDocForm()
    return render(request, 'doctor/profile.html', {'form':form, 'doctor':doctor})

@login_required(login_url='/accounts/login')
def addpatient(request):
    current_user = request.user
    # doctor = Patient.objects.get(id='1')
    if request.method == 'POST':
        nextkinform = NewNextOfKinForm(request.POST, request.FILES)
        addpatform = addPatientForm(request.POST, request.FILES)
        newmedform = NewMedicineForm(request.POST, request.FILES)
        if nextkinform.is_valid() and addpatform.is_valid() and newmedform.is_valid():
            next_of_kin = nextkinform.save()
            next_of_kin.save()
            return redirect('/')
        elif newmedform.is_valid():
            medicine = newmedform.save()
            medicine.save()
            return redirect('/')

        elif addpatform.is_valid():
            patient = addpatform.save()
            patient.save()
            return redirect('/')

    else:
        addpatform = addPatientForm()
        nextkinform = NewNextOfKinForm()
        newmedform = NewMedicineForm()
    return render(request, 'patient/profile.html', { 'addpatform':addpatform,'nextkinform':nextkinform,'newmedform':newmedform})

@login_required(login_url='/accounts/login')
def treatment(request):
    # current_user =request.user
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.save()
            # return redirect('') 
    else:
        form = TreatmentForm()
    return render(request, 'treatment/treatment.html', { 'form':form})



