from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    SHIRT_SIZES = [ 
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),]
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    name = models.CharField(max_length=30)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
from django.db import models

class Runner(models.Model):
    class MedalType(models.TextChoices):
        GOLD = 'GOLD', 'Gold'
        SILVER = 'SILVER', 'Silver'
        BRONZE = 'BRONZE', 'Bronze'

    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, max_length=10, choices=[(tag, tag.value) for tag in MedalType])

    def __str__(self):
        return self.name

class Topping(models.Model):
 # ...
    pass
class Pizza(models.Model):
 # ...
    toppings = models.ManyToManyField(Topping)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")
    def __str__(self):
        return self.name
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
         return "Baby boomer"
        else:
            return "Post-boomer"
    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"



    #page 123