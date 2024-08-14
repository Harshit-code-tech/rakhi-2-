# app/forms.py
from django import forms
from .models import Mood, Reward, Reminder, Note, Journal, JournalReminder

class MoodForm(forms.ModelForm):
    OTHER_MOOD_VALUE = 'other'

    MOOD_INTENSITY_CHOICES = [
        ('VL', 'Very Low'),
        ('L', 'Low'),
        ('M', 'Moderate'),
        ('H', 'High'),
        ('VH', 'Very High'),
    ]

    mood = forms.ChoiceField(choices=[
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
        (OTHER_MOOD_VALUE, 'Other (please specify)'),
    ], required=True)
    custom_mood = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Custom mood'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}), initial='#ffffff')
    intensity = forms.FloatField(min_value=0, max_value=5, required=True)
    tags = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Tags/Descriptors'}))

    class Meta:
        model = Mood
        fields = ['date', 'intensity', 'mood', 'custom_mood', 'color', 'tags']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'custom_mood': forms.TextInput(attrs={'placeholder': 'Custom mood'}),
            'intensity': forms.NumberInput(attrs={'step': 0.1}),
            'tags': forms.TextInput(attrs={'placeholder': 'Tags/Descriptors'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        mood = cleaned_data.get('mood')
        custom_mood = cleaned_data.get('custom_mood')

        if mood == self.OTHER_MOOD_VALUE and not custom_mood:
            self.add_error('custom_mood', 'Please specify your mood.')
        elif custom_mood:
            cleaned_data['mood'] = custom_mood

        return cleaned_data
class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title', 'maxlength': 100}),
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your journal entry here...'}),
        }

class JournalReminderForm(forms.ModelForm):
    class Meta:
        model = JournalReminder
        fields = ['date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = ['image']

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'No description provided',
                'rows': 3,
            }),
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description == 'No description provided':
            return ''
        return description

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
