from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('index/',views.index, name='index'),
    path('rooms/',views.rooms, name='rooms'),
    path('about/',views.about,name='about'),
    path('blog_details/',views.blog_details, name='blog_details'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact),
    path('room_details/',views.room_details, name='room_details'),
    path('profile/',views.profile),
    path('update_profile/',views.update_profile),
    path('logout/',views.loguot_view, name="logout"),
]