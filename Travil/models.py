from django.db import models

# Create your models here.


class Index(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    photos = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.age}, {self.photos}'
