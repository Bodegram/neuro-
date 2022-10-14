from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from matplotlib.pyplot import title
from sqlalchemy import null

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=300, null=True, default="Unknown")
    content = models.CharField(max_length=400, null=True, default="Unknown")
    date = models.DateField()
    category = models.CharField(max_length=300, null=True, default="Unknown")

    def __str__(self):
        return self.title

