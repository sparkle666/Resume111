from django.db import models

# Create your models here.
class Skills(models.Model):
  name = models.CharField(max_length = 200)
  level = models.IntegerField()
  
  def __str__(self):
    return self.name
  

class Bio(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  stack = models.CharField(max_length = 200)
  age = models.IntegerField()
  degree = models.CharField(max_length= 4)
  location = models.CharField(max_length = 100)
  #profile_picture = models.InageField(upload_to = "pic/")
  skills = models.ForeignKey(Skills, on_delete = models.CASCADE)
  email = models.EmailField(max_length = 200)
  url = models.URLField(max_length = 200)
  
  def __str__(self):
    return self.first_name + " " + self.stack
    
