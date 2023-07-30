from django.db import models

class Certificate(models.Model):
    certificate_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date_of_issue = models.DateField()
    

