from django.shortcuts import render
from django.views import View
from .models import Course


# Create your views here.
class Data_science_courseView(View):
    def get(self, request):
        course = Course.objects.all()
        return render(request, 'Course/data_science.html', {'course': course})


def courseDetail(request, id_course):
    cD = Course.objects.get(id_course=id_course)
    return render(request, 'Course/course_detail.html', {'cD': cD})
