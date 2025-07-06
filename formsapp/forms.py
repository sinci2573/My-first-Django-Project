from django import forms

class SurveyForm(forms.Form):
    name = forms.CharField(label="What's your name?", max_length=100)
    age = forms.IntegerField(label="How old are you?")
    favorite_color = forms.CharField(label="What's your favorite color?", max_length=50)
    hobby = forms.CharField(label="What's your hobby?", max_length=100)
    feedback = forms.CharField(label="Any feedback for us?", widget=forms.Textarea, required=False)
