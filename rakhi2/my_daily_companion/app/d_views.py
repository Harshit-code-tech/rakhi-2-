from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def habit_tracker(request):
    return render(request, 'habit_tracker.html')

def mood_tracker(request):
    return render(request, 'mood_tracker.html')

def historical_data(request):
    return render(request, 'historical_data.html')

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')

def reminder(request):
    return render(request, 'reminder.html')
