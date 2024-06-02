from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    contact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_flagged = models.BooleanField(default=False)


class Licence(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    license_key = models.CharField(max_length=100)
    expiration_date = models.DateField()
