from django.shortcuts import render
from .models import Profile

def home(request):
    return render(request, 'home.html', {})

def UserProfileView(request):
    user_list = Profile.objects.all()
    return render(request, 'profile_card.html', {'user_list': user_list})