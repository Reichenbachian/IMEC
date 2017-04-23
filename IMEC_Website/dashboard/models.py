from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timezone import localtime, now

# wrapper class for User
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

# Create your models here.
class Entry(models.Model):
    productID = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expirationDate = models.DateField(blank=True, null=True)
    lotBatchNum = models.CharField(max_length=70, blank=True, null=True)
    unitsPerCase = models.CharField(max_length=70, blank=True, null=True)
    totalUnits = models.TextField(blank=True, null=True)
    scannedBy = models.CharField(max_length=20, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def toDict(self):
    	return {"productID": self.productID, \
    			"description": self.description, \
    			"expirationDate": self.expirationDate, \
    			"lotBatchNum": self.lotBatchNum, \
    			"unitsPerCase": self.unitsPerCase, \
    			"totalUnits": self.totalUnits}

class VolunteerID(models.Model):
    idString = models.CharField(max_length=20, null=True)
    issuedBy = models.CharField(max_length=60, null=True)
    valid = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def isValid(self):
        return self.valid
