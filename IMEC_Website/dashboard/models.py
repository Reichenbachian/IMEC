from django.db import models

# Create your models here.
class Entry(models.Model):
    productID = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expirationDate = models.DateField(blank=True, null=True)
    lotBatchNum = models.CharField(max_length=70, blank=True, null=True)
    unitsPerCase = models.CharField(max_length=70, blank=True, null=True)
    totalUnits = models.TextField(blank=True, null=True)
    def toDict(self):
    	return {"catNumber": self.productID, \
    			"siteNumber": self.description, \
    			"locality": self.expirationDate, \
    			"site": self.lotBatchNum, \
    			"name": self.unitsPerCase, \
    			"situation": self.totalUnits}