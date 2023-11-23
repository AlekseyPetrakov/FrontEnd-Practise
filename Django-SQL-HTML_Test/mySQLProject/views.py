from django.shortcuts import render
from .models import Person  # Adjust the import based on your actual models

def persons_list(request):
    persons_queryset = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons_queryset})
