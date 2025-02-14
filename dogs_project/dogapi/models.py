from django.db import models

class Dog(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    #breed (внешний ключ к модели Breed)
    gender = models.CharField()
    color = models.CharField()
    favorite_food = models.CharField()
    favorite_toy = models.CharField()




