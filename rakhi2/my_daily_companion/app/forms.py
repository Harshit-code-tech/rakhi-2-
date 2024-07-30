from django import forms
from .models import Mood, Reward, Reminder, Note, Journal


class MoodForm(forms.ModelForm):
    OTHER_MOOD_VALUE = 'other'

    mood = forms.ChoiceField(choices=[
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        (OTHER_MOOD_VALUE, 'Other (please specify)'),
    ], required=True)
    custom_mood = forms.CharField(required=False, max_length=255)

    class Meta:
        model = Mood
        fields = ['date', 'level', 'mood', 'custom_mood']
        widgets = {
            'level': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'date': forms.DateInput(attrs={'type': 'date'}),
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