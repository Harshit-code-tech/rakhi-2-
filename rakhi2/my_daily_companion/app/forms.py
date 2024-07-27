from django import forms
from .models import Mood, Habit, Reward

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood']

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'completed']

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['image']
