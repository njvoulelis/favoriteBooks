from __future__ import unicode_literals
from django.db import models
from datetime import date
from apps.logRegApp.models import User


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        if len(postData['title']) == 0:
            errors['titleLength'] = "Title is required"
        if len(postData['desc']) < 5:
            errors['descLength'] = "Description must be greater than 5 characters"
        return errors

class Book(models.Model):
    uploadedBy = models.ForeignKey(User, related_name="booksUploaded")
    usersWhoLike = models.ManyToManyField(User, related_name="likedBooks")
    title = models.CharField(max_length=255)
    desc = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = BookManager()


