from django.contrib import admin
from django.urls import path
from testApp import views

urlpatterns = [
    path('',views.home, name = "Home"),
    path('StudentNews/',views.student, name="Page1"),
    path('FacultyNews/',views.faculty,name="Page2"),
    path('EventNews/',views.event,name="Page2"),
]
