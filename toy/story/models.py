from django.db import models

# Create your models here.
#To create table in database(sqlite3)

class project(models.Model):
  date=models.CharField(max_length=50)
  bookName=models.CharField(max_length=50)
  name=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  address=models.CharField(max_length=50)
  email=models.EmailField()
  phone=models.IntegerField()
  class Meta:
    db_table="project"  
