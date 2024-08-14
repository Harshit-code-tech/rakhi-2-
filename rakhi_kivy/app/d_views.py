from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
import logging

# Get the logger for this module
logger = logging.getLogger('myapp')

def my_view(request):
    try:
        # Your view logic here
        logger.debug('Debug message from my_view')
        logger.info('Informational message from my_view')
        return HttpResponse('Check your logs for messages!')
    except Exception as e:
        logger.error(f'An error occurred: {e}', exc_info=True)
        return HttpResponse('An error occurred!')

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'upload.html')


def auth_view(request):
    # Your logic here
    return render(request, 'auth.html')
def home(request):
    return render(request, 'home.html')

def habit_tracker(request):
    return render(request, 'habit_tracker.html')

def mood_tracker(request):
    return render(request, 'mood_tracker.html')

def daily_goals(request):
    logger.info('Accessed mood_entries view')
    # Your logic here
    return render(request, 'daily_goals.html')

def mood_entries(request):
    logger.info('Accessed mood_entries view')
    # Your logic here
    return render(request, 'mood_entries.html')
def historical_data(request):
    return render(request, 'historical_data.html')

def rewards(request):
    return render(request, 'rewards.html')

def settings(request):
    return render(request, 'settings.html')

def reminder(request):
    return render(request, 'reminder.html')
