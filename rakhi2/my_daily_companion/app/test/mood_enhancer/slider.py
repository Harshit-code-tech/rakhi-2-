# forms.py
from django import forms

class MoodForm(forms.Form):
    MOOD_CHOICES = [
        ('very_low', 'Very Low'),
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ]

    intensity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'value': '3', 'id': 'intensity-slider'})
    )
    mood = forms.ChoiceField(choices=MOOD_CHOICES)
