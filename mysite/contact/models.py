from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField('Full name', max_length=60)
    email = models.EmailField('Email')
    company = models.CharField('Company', max_length=50)
    describe = models.TextField('Describe')

    def __str__(self):
        return self.email