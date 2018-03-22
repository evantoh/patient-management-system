from django.shortcuts import render,redirect
from .forms import UpdateDocForm,addPatientForm,TreatmentForm,NewNextOfKinForm,NewMedicineForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Doctor,Medicine,NextOfKin
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
    doctor = Doctor.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        nform = NewNextOfKinForm(request.POST, request.FILES)
        form = addPatientForm(request.POST, request.FILES)
        mform = NewMedicineForm(request.POST, request.FILES)
        if mform.is_valid() and nform.is_valid() and form.is_valid():
            next_of_kin = nform.save()
            next_of_kin.save()
        elif mform.is_valid():
            medicine = mform.save()
            medicine.doctor =doctor
            medicine.save()

        elif form.is_valid():
            patient = form.save()
            patient.doctor = doctor
            patient.save()

        elif adform.is_valid():
            allergies = adform.save()
            allergies.save()
        return redirect('newPatient')
        current_user = request.user
    doctor = Doctor.objects.get(user_id=current_user.id)
    if request.method == 'POST':
        nform = NewNextOfKinForm(request.POST, request.FILES)
        form = NewPatientForm(request.POST, request.FILES)
        mform = NewMedicineForm(request.POST, request.FILES)
        adform = AllergiesAndDirectivesForm(request.POST, request.FILES)
        if mform.is_valid() and nform.is_valid() and form.is_valid():
            next_of_kin = nform.save()
            next_of_kin.save()
        elif mform.is_valid():
            medicine = mform.save()
            medicine.doctor =doctor
            medicine.save()

        elif form.is_valid():
            patient = form.save()
            patient.doctor = doctor
            patient.save()

        elif adform.is_valid():
            allergies = adform.save()
            allergies.save()
        return redirect('newPatient')
        
    return render(request,'patient/profile.html',{"form":form})

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



