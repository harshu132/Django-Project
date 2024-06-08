from typing import Any
from django.http import Http404 
from django.views.generic import ListView,DetailView
from django.shortcuts import render


from.models import Pet

# Create your views here.
def pet_list_view(request):
    pets = Pet.objects.all()
    return render(request, 'Pet/Pet_list.html', {'pets': pets})

   
#class PetDetailView(DetailView):
   # model = Pet

   # def get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)
   #     return context

#class PetDetailView(DetailView):
  #  model = Pet
  #  slug_field = 'Petname'  # Assuming 'name' is the field in your Pet model that stores the pet's name
  #  slug_url_kwarg = 'Petname'  # Same as above
class PetDetailView(DetailView):
    model = Pet

    def get_object(self, queryset=None):
        # Get the pet's name from the URL
        pet_name = self.kwargs.get('Petname')
        # Query the pet by name
        queryset = Pet.objects.filter(Petname=pet_name)
        # If pet is found, return it, else raise a 404 error
        try:
            return queryset.get()
        except Pet.DoesNotExist:
            raise Http404("Pet does not exist")