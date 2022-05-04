from django.db import models

# Create your models here.
class Funfact(models.Model):
    idm = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    photo = models.ImageField(
        upload_to='media/photo_funfacts',
        default='media/default/default.jpg',
        blank=True)

class Scale(models.Model):
    idm = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='media/photo_scale',
        default='media/default/default.jpg',
        blank=True)
    typesb = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    cause = models.CharField(max_length=100)

class Tip(models.Model):
    idm = models.CharField(max_length=100)
    t_title = models.CharField(max_length=100)
    t_text = models.CharField(max_length=100)
    t_icon = models.CharField(max_length=100)

class Post(models.Model):
    idm = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='media/photo_posts',
        default='media/default/default.jpg',
        blank=True)

class Link(models.Model):
    idm = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)



class Photo(models.Model):
    idm = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    photo = models.ImageField(
        upload_to='media/photo_gallery',
        default='media/default/default.jpg',
        blank=True)











