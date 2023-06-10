from django.shortcuts import render
from .models import Student, Faculty, Event

# Create your views here.
def home(request):
    return render(request,'testApp/main.html')

def student(request):
    mydata = Student.objects.all()
    context = {
        'data' : mydata
    }
    return render(request,'testApp/student.html',context)

def faculty(request):
    mydata = Faculty.objects.all()
    context = {
        'data' : mydata
    }
    return render(request,'testApp/faculty.html',context)

def event(request):
    mydata = Event.objects.all()
    context = {
        'data' : mydata
    }
    return render(request,'testApp/event.html',context)