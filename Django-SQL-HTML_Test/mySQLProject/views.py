from django.shortcuts import render
from .models import Person, Animal  # Adjust the import based on your actual models
from django.http import HttpResponse


def persons_list(request):
    persons_queryset = Person.objects.all()
    animals_queryset = Animal.objects.all()
    return render(request, 'persons_list.html', {'persons': persons_queryset, 'animals': animals_queryset})



def index(request):
    person_exists = None

    if request.method == 'POST':
        fname = request.POST.get('fname')
        person_exists = Person.objects.filter(name=fname).exists()

    return render(request, 'index.html', {'person_exists': person_exists})