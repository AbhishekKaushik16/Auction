from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listings(models.Model):
    id_no = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=64)
    description = models.TextField(max_length=64)
    item_price = models.IntegerField()
    listed_by = models.CharField(max_length=64)
    category = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    watchlist = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return f"{self.item_name}"

class Bids(models.Model):
    id_no = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=64)
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE,related_name="bids")
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.person_name} ({self.id_no})"

    class Meta:
        verbose_name_plural = 'Bids'

class Comment(models.Model): 
    post = models.ForeignKey(Listings,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.item_name