from django import forms
from .models import Mood, Note, Reward

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ['mood', 'level']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['image']
