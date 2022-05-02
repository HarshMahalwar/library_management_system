from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class participant(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class book(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

class Issue(models.Model):
    objects = None
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)
    participant = models.ForeignKey(participant, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(book, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.id
