from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import InscriptionForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', {'form': form})