from django.db import models

# Create your models here.


#models is nothing tables in sql

class topic(models.Model):
    topic_name=models.CharField(max_length=100, primary_key=True) 

    def __str__(self):
        return self.topic_name

class webpage(models.Model):

    name=models.CharField(max_length=100,primary_key=True) 
    url=models.URLField()
    email=models.EmailField()
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class accessrecord(models.Model):

    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author