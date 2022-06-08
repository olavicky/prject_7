from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    nickname = models.CharField(max_length=500, null=True, blank=True)

    def _str_(self):
        return self.name


class Address(models.Model):
    people = models.OneToOneField(People, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    home_address = models.CharField(max_length=500, null=True, blank=True)
    postalcode = models.CharField(max_length=500, null=True, blank=True)

    def _str_(self):
        return self.state


class Doctor (models.Model):
    patients = models.ManyToManyField(People, through="Doctors")
    people = models.ManyToManyField(People, on_delete=models.CASCADE,  null=True)
    patient_name = models.CharField(max_length=500, null=True, blank=True)
    people_id_number = models.CharField(max_length=500, null=True, blank=True)
    number_of_patient = models.IntegerField(null=True, blank=True)


class Doctors(models.Model):
    patient = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospitals = models.ForeignKey(People, on_delete=models.CASCADE)

    def _str_(self):
        return self.patient


class Product(models.Model):
    name = models.OneToOneField(People, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=500, null=True, blank=True)
    product_category = models.CharField(max_length=500, null=True, blank=True)
    price = models. IntegerField(null=True, blank=True)

    def _str_(self):
        return self.product_name


class Bio (models. Model):
    people = models.OneToOneField(People, on_delete=models.CASCADE, null=True)
    people_id = models.CharField(max_length=500, null=True, blank=True)
    origin = models.CharField(max_length=500, null=True, blank=True)

    def _str_(self):
        return self.people_id
