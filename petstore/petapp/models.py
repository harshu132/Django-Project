from django.db import models



# Create your models here.
class Pet(models.Model):
    image = models.ImageField(upload_to='images/')
    Petname = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    Breed = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    price = models.FloatField()
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Description = models.CharField(max_length=100)
    # DisplayFields =['id','Petname','species','Breed','Age','price','Gender','Description']
    # SearchableFields =['Petname','Age']


    def __str__(self):
        return self.Petname
    
class Meta:
    db_table = "Pet"    
    

    
       
    
   
    

