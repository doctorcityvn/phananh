from __future__ import unicode_literals
from django.db import models
from django import forms
from django.conf import settings
import django.utils.safestring as safestring

class Division(models.Model):
    div=models.Manager()
    namediv = models.CharField(max_length=200)
    active = models.BooleanField("Is Active", default=True)
    
    def __str__(self):
        return self.namediv
class Patient(models.Model):
    pat=models.Manager()
    Type_id = models.ForeignKey(Division, on_delete=models.CASCADE)
    namepatient = models.CharField("Patient Name", max_length=200)
    age = models.IntegerField("Age", default=40)
    place = models.CharField("Place", max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/',null=True)
    symptom = models.TextField("symptom", default="")
    diagnosis = models.TextField("diagnosis",default="")
    doctor = models.CharField("Doctor Name", max_length=200,default="")
    prescription = models.TextField("Prescription",default="")
    
    def image_tag(self):
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    def __str__(self):
        return self.namepatient

