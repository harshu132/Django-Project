
from django.urls import path
from petapp.views  import PetListView
from petapp.views  import PetDetailView



urlpatterns = [path('', PetListView.as_view()),
                path('/<str:Petname>/', PetDetailView.as_view(), name='pet_detail'),
    
]
