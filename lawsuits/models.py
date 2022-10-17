from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Customer(models.Model):
    """A model that represents a single costumer that can have more than on lawsuit"""
    # TODO - You might want to update these variables with the user information you want to keep track of. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=14)

class Lawsuit(models.Model):
    """A model to represent a single lawsuit that can belong to more than one customer"""
    customer = models.ManyToManyField(User)
    number = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.number} - {self.description}"
    
class Movement(models.Model):
    """A model where the lawyer can describe in simple terms whats happening in the process.
    Its in a separete model so that the history of the process can be mantained"""
    lawsuit = models.ForeignKey(Lawsuit, on_delete=models.CASCADE)
    description = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lawsuit.description} - {self.date_added}"
