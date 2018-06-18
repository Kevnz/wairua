from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.contrib import messages
from .models import MoodEntry
from .forms import MoodEntryForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def homePage(request):
    if request.method == "POST":
        form = MoodEntryForm(request.POST)
        # form.enteredOn = parse_datetime(request.POST.get('enteredOn'))
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.enteredOn = timezone.now()
            print(entry.enteredOn)
            print(timezone.now())
            entry.save()
        else:
            print(form.errors)
    else:
        form = MoodEntryForm()
    if request.user.is_authenticated:
        past_moods = MoodEntry.objects.filter(user=request.user)
    else:
        past_moods = False

    moods = MoodEntry.MOODS;
    stuff_for_frontend = {"past_moods": past_moods, "all_moods": moods, 'form': form}

    return render(request, 'index.html', stuff_for_frontend)

def register(request):
    if request.method == 'POST':
        print('the things')
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            print('not valid')
            print(f.errors)

    else:
        f = UserCreationForm()

    return render(request, 'register.html', {'form': f })

@login_required
def profile(request):
    print(request.user)
    return render(request, 'profile.html', { "user": request.user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request,'profile_edit.html', 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)

    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        "user": request.user
    })