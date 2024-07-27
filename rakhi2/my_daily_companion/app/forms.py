from django import forms
from .models import Mood, Note, Reward

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['date', 'level', 'mood']
        widgets = {
            'level': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['image']
