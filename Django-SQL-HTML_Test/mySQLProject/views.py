from django.shortcuts import render
from .models import Person, Animal,Admin  # Adjust the import based on your actual models
from django.http import HttpResponse


def persons_list(request):
    persons_queryset = Person.objects.all()
    animals_queryset = Animal.objects.all()
    return render(request, 'persons_list.html', {'persons': persons_queryset, 'animals': animals_queryset})



def index(request):
    admin_exists = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if an admin with the given username and password exists
        admin_exists = Admin.objects.filter(name=username, password=password).exists()

    return render(request, 'index.html', {'admin_exists': admin_exists})