from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300) 

    def __str__(self):
        return self.name

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    # without null=True, if you have blank=True, for some fields (like CharField) default empty values (e.g. empty string) would be stored, others would cause an error
    participants = models.ManyToManyField(Participant, blank=True, null=True)
