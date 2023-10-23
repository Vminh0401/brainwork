from django.shortcuts import render
from django.views import View
from .models import Course


# Create your views here.
class Data_science_courseView(View):
    def get(self, request):
        course_1 = Course.objects.filter(id_course=1)
        course_2 = Course.objects.filter(id_course=2)
        course_3 = Course.objects.filter(id_course=3)
        course_4 = Course.objects.filter(id_course=4)
        course_5 = Course.objects.filter(id_course=5)
        course_6 = Course.objects.filter(id_course=6)
        course_7 = Course.objects.filter(id_course=7)
        course_8 = Course.objects.filter(id_course=8)
        course_9 = Course.objects.filter(id_course=9)
        course_10 = Course.objects.filter(id_course=10)
        course_11 = Course.objects.filter(id_course=11)
        course_12 = Course.objects.filter(id_course=12)
        course_13 = Course.objects.filter(id_course=13)
        return render(request, 'Course/data_science.html',
                      {'course_1': course_1,
                              'course_2': course_2,
                              'course_3': course_3,
                              'course_4': course_4,
                              'course_5': course_5,
                              'course_6': course_6,
                              'course_7': course_7,
                              'course_8': course_8,
                              'course_9': course_9,
                              'course_10': course_10,
                              'course_11': course_11,
                              'course_12': course_12,
                              'course_13': course_13, })


def courseDetail(request, id_course):
    cD = Course.objects.get(id_course=id_course)
    return render(request, 'Course/course_detail.html', {'cD': cD})
