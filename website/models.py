from django.db import models


class Record(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=25)
     
    def __str__(self):
	    return (f"{self.first_name} {self.last_name}")
    
