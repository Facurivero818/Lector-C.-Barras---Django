from django.db import models

class Codigos(models.Model):
    codigo= models.CharField(max_length=70)
    producto= models.CharField(max_length=70)

