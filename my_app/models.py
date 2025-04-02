from django.db import models

# Create your models here.


class register_tbl(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class RoomBooking_tbl(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

class latest(models.Model):
    latest_email = models.EmailField()

class Reservation_tbl(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

class Leave_A_Comment_tbl(models.Model):
    Name = models.CharField(max_length=50)
    Mail = models.EmailField()
    Website = models.CharField(max_length=100)
    Messages = models.TextField(max_length=100)

class Contact_tbl(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()