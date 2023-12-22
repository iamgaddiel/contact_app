from django.db import models
from django.contrib.auth.models import User



class Group(models.Model):
    group_title = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.group_title


class Job(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title


class Relationship(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
    
# Create your models here.
class Contact(models.Model):

    # group_choices = [
    #     ('NA', 'Not Assigned'),
    #     ('EC', 'Emmer Assigned'),
    #     ('NA', 'Not Assigned'),
    #     ('NA', 'Not Assigned'),
    # ]

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='contact_images/%Y/%m/%d', blank=True) # %Y %m %d
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    website = models.URLField(blank=True)
    ringtone = models.FileField(upload_to='ringtones/%Y/%m', blank=True)
    groups = models.ForeignKey(to=Group, on_delete=models.CASCADE, blank=True)
    jobs = models.ForeignKey(to=Job, on_delete=models.CASCADE, blank=True)
    relationships = models.ForeignKey(to=Relationship, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def get_first_name_initials(self):
        return self.first_name[0].capitalize()
