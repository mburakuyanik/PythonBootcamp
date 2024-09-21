from django.db import models

# Create your models here.

class Tweets(models.Model):
    nickname = models.CharField(max_length=50)
    tweet = models.CharField(max_length=100)

    def __str__(self):
        return f'nickname: {self.nickname}, tweet: {self.tweet}'

