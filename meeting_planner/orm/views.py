from django.shortcuts import render
from orm.models import Student
# Create your views here.
from django.http import HttpResponse


def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'templates/orm/studetails.html', {'stu': stud})
    # return HttpResponse('egege')
