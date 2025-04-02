from django import forms
from .models import *

class register_form(forms.ModelForm):
    class Meta:
        model = register_tbl
        fields = '__all__'

class roomcheck_form(forms.ModelForm):
    class Meta:
        model = RoomBooking_tbl
        fields = ['guest', 'room', 'check_in', 'check_out']
        

class latest_form(forms.ModelForm):
    class Meta:
        model = latest
        fields = ['latest_email']

class Reservation_form(forms.ModelForm):
    class Meta:
        model = Reservation_tbl
        fields = ['guest', 'room', 'check_in', 'check_out']

class Leave_A_Comment_form(forms.ModelForm):
    class Meta:
        model = Leave_A_Comment_tbl
        fields = '__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_tbl
        fields = '__all__'
        
class update_form(forms.ModelForm):
    class Meta:
        model = register_tbl
        fields = ['username', 'email', 'password']