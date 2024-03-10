from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(default=0)
    thumbnailUrl = models.CharField(max_length=256,null=True)
    shortDescription = models.TextField(null=True)
    longDescription = models.TextField(null=True)
    #isbn = models.CharField(max_length=256,null=True)
    #publishedDate = models.DateField()
    #status = models.CharField(max_length=20)
    #authors = models.ManyToManyField('Author')
    #categories = models.ManyToManyField('Category')