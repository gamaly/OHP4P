from django_countries.fields import CountryField

from django.db import models
from django.urls import reverse


import datetime

yes_or_no = (
    ('yes','YES'),
    ('no', 'NO'),
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    country = CountryField(default="USA")
    date = models.DateField(default=datetime.date.today)
    facilitator_name = models.CharField(max_length=50, default="test")
    nohta_name = models.CharField(max_length=50, default="test")
    rohta_name = models.CharField(max_length=50, default="test")
    participant_number = models.IntegerField(default=1)
    sectors = models.CharField(max_length=50, default="test")
    who_jee = models.CharField(max_length=3, choices=yes_or_no, default='test')
    partners = models.CharField(max_length=3, choices=yes_or_no, default='test')
    workshop = models.CharField(max_length=3, choices=yes_or_no, default='test')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
