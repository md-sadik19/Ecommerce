from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone =models.CharField(max_length=11)
    age = models.IntegerField()
    address =models.TextField(max_length=120)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} | {self.age}"

class Spess(models.Model):
    name = models.CharField(max_length=120)
    phone =models.CharField(max_length=11)
    age = models.IntegerField()
    address =models.TextField(max_length=120)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.name} | {self.age}"