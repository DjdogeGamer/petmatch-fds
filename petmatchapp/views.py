from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from petmatchapp.models import PetProfile

from .forms import PetProfileForm
from .models import PetProfile


class HomePageView(ListView):
    model = PetProfile
    template_name = "home.html"


class PetDetailView(DetailView):
    model = PetProfile
    template_name = "pet_details.html"
    context_object_name = 'PetProfile'
    
class AddPetView(CreateView):
    model = PetProfile
    form_class = PetProfileForm
    template_name = "add_pet.html"

#Ainda não foi implementada, a ser implementada

'''
class UpdatePet(UpdateView):
    model = PetProfile
    template_name = "update_pet.html"
    fields = ['name', 'age', 'bio']
    
class DeletePetView(DeleteView):
    model = PetProfile
    template_name = "delete_pet.html"
'''
