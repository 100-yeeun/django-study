from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=30)

 # 이름알려주는 함수라고 생각하기
    def __str__(self):
        return self.email