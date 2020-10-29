from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    views = models.PositiveIntegerField(default=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Good(models.Model):
    name = models.CharField(max_length=100)
    b_price = models.PositiveIntegerField(default=100)
    s_price = models.PositiveIntegerField(default=110)


class PeopleInfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=512)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name