from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    species = models.IntegerField() # 개 = 1, 고양이 = 2, 기타 = 3
    age = models.CharField(max_length=10) #개월수, 나이

    def __str__(self):
        return self.name