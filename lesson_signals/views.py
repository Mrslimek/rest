from django.shortcuts import render
from .models import Sun
from .forms import SunForm

# Create your views here.


def get_page(request):

    form = SunForm()

    if request.method == 'POST':
        form_with_data = SunForm(data=request.POST)
        if form_with_data.is_valid():
            form_with_data.save()

    return render(request, 'index.html', {'form': form})