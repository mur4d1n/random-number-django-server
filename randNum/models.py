from django.db import models


class RandNum(models.Model):
    randNum = models.IntegerField()

    def __int__(self):
        return self.randNum
