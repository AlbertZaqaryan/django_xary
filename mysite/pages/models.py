from django.db import models

# Create your models here.

class HomeCarusel(models.Model):
    name = models.CharField('HomeCarusel name', max_length=40)
    img = models.ImageField('HomeCarusel image', upload_to='media')
    info1 = models.CharField('HomeCarusel info1', max_length=15)
    info2 = models.CharField('HomeCarusel info2', max_length=15, blank=True)
    superuser = models.ImageField('HomeCarusel superuser image', upload_to='media', blank=True)

    def __str__(self):
        return self.name

class HomeCategory(models.Model):
    name = models.CharField('Category name', max_length=30)
    img = models.ImageField('Category image', upload_to='media')
    info = models.CharField('Category info', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HomeCategory'
        verbose_name_plural = 'HomeCategories'


class HomeTopic(models.Model):
    homecategory = models.ForeignKey(HomeCategory, on_delete=models.CASCADE, related_name='garaje')
    name = models.CharField('HomeTopic name', max_length=40)
    img = models.ImageField('HomeTopic image', upload_to='media')
    info = models.CharField('HomeTopic info1', max_length=15)
    history = models.TextField('HomeTopic history')
    slug = models.SlugField('HomeTopic link', unique=True, blank=True)


    def __str__(self):
        return self.name