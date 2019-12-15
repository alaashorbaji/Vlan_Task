from django.db import models



class Vlan_T(models.Model):
    Vlan_id=models.CharField(max_length=100,primary_key=True,serialize=True)
    Name= models.CharField(max_length=100)
    Description= models.CharField(max_length=100)
    def __str__(self):
        return self.Name

