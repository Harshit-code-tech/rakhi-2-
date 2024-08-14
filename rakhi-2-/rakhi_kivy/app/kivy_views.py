import logging
from kivy.uix.screenmanager import ScreenManager, Screen


# kivy_views.py
class HomeScreen(Screen):
    def on_pre_enter(self):
        logging.info("Entering Home Screen")


class MoodTrackerScreen(Screen):
    def on_pre_enter(self):
        logging.info("Entering Mood Tracker Screen")


class HabitTrackerScreen(Screen):
    def on_pre_enter(self):
        logging.info("Entering Habit Tracker Screen")


class RewardScreen(Screen):
    def on_pre_enter(self):
        logging.info("Entering Reward Screen")


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        logging.info("Initializing MyScreenManager")
        self.add_widget(HomeScreen(name='home'))
        self.add_widget(MoodTrackerScreen(name='mood_tracker'))
        self.add_widget(HabitTrackerScreen(name='habit_tracker'))
        self.add_widget(RewardScreen(name='reward'))

    def on_current(self, *args):
        logging.info(f"Screen changed to: {self.current}")


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


from django.shortcuts import render
from .kivy_models import Habit


def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habit_list.html', {'habits': habits})


from rest_framework import viewsets
from .kivy_models import Habit
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
