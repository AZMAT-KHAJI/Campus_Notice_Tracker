# notices/models.py
"""
Entities:
1. User (Primary Key: id)
2. Category (Primary Key: id)
3. Notice (Primary Key: id)

Relationships:
User (1) ---- (Many) Notice
Category (1) ---- (Many) Notice
"""

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
