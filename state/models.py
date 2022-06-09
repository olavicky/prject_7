from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=500, blank=True)
    nickname = models.CharField(max_length=500, blank=True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)

    def _str_(self):
        return self.name


class Address(models.Model):
    state = models.CharField(max_length=500, blank=True)
    home_address = models.CharField(max_length=500, blank=True)
    postalcode = models.CharField(max_length=500, blank=True)

    def _str_(self):
        return self.state


class Doctor (models.Model):
    patient_name = models.CharField(max_length=500, blank=True)
    people_id_number = models.CharField(max_length=500, blank=True)
    number_of_patient = models.IntegerField(blank=True)

    def _str_(self):
        return self.patient_name


class Product(models.Model):
    product_name = models.CharField(max_length=500, blank=True)
    product_category = models.CharField(max_length=500, blank=True)
    price = models. IntegerField(null=True, blank=True)

    def _str_(self):
        return self.product_name


class Bio (models. Model):
    people_id = models.CharField(max_length=500, blank=True)
    origin = models.CharField(max_length=500, blank=True)
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.origin
