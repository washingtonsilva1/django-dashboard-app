from django.db import models


class Member(models.Model):
    full_name = models.CharField(max_length=155, blank=False)
    birth_date = models.DateField()
    sex = models.BooleanField()
    is_married = models.BooleanField()
