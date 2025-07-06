from django.shortcuts import render
from .forms import SurveyForm
from datetime import datetime

def home(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            color = form.cleaned_data['favorite_color']
            hobby = form.cleaned_data['hobby']
            age = form.cleaned_data['age']

            # Calculate birth year
            current_year = datetime.now().year
            birth_year = current_year - age

            # Pass data to the success page
            context = {
                'name': name,
                'color': color,
                'hobby': hobby,
                'birth_year': birth_year,
            }
            return render(request, 'success.html', context)
    else:
        form = SurveyForm()

    return render(request, 'home.html', {'form': form})
