from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=100)
    type = [
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('WB', 'WEB'),
    ]
    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_label = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_label



class Articl(models.Model):

    titel= models.CharField(max_length=100)
    link =models.URLField(max_length=200)
    date =models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.titel


class User(models.Model):
    name = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class commant(models.Model):
    date = models.DateTimeField()
    commant = models.CharField(max_length=300)
    articl = models.ForeignKey(Articl, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)