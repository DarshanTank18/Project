from django.contrib import admin
from .models import *

# Register your models here.

class register_tbl_admin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password']

class RoomBooking_tbl_admin(admin.ModelAdmin):
    list_display = ['id', 'check_in', 'check_out', 'guest', 'room']

class latest_admin(admin.ModelAdmin):
    list_display = ['id', 'latest_email']

class Reservation_tbl_admin(admin.ModelAdmin):
    list_display = ['id', 'check_in', 'check_out', 'guest', 'room']

class Leave_A_Comment_tbl_admin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Mail', 'Website', 'Messages']

class Contact_tbl_admin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Email', 'Message']
    
admin.site.register(register_tbl, register_tbl_admin)
admin.site.register(RoomBooking_tbl, RoomBooking_tbl_admin)
admin.site.register(latest,latest_admin)
admin.site.register(Reservation_tbl,Reservation_tbl_admin)
admin.site.register(Leave_A_Comment_tbl,Leave_A_Comment_tbl_admin)
admin.site.register(Contact_tbl,Contact_tbl_admin)
