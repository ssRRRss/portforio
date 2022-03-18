from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class projectData(models.Model):
    title = models.CharField(max_length=50, null=True)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField()
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(projectData, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class skill(models.Model):
    title = models.CharField(max_length=50, null=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return self.title


class tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return self.name


class Endorsement(models.Model):
    name = models.CharField(max_length=50, null=True)
    body = models.TextField()
    approved = models.BooleanField(default=False, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.body[0:50]
