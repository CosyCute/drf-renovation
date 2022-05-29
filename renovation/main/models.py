from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    renovation_type = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name