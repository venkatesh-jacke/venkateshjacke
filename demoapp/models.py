from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,default='',blank=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=10,default='',blank=True)
    msg = models.TextField(max_length=500,default='',blank=True)

    def __str__(self):
        return self.name+"-"+self.email+"-"+self.phone

