from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class school(models.Model):
    Name = models.CharField(max_length=20)
    Roll_no = RichTextField(max_length=20,blank=True,null=True)
    