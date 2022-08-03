from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=600)
    title_tag = models.CharField(max_length=600) #,default="DEYS RAVEZ!"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))
        # return reverse('home')
