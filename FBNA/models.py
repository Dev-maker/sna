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


class Article(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    date = models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    def __str__(self):
        return self.title


class Profile(models.Model):
    name = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12,blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class comment(models.Model):

    comment = models.TextField(max_length=300)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField()

