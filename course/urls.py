from django.urls import path
from .views import Data_science_courseView
from course import views
app_name = 'Course'

urlpatterns = [
    path('Data_science/', Data_science_courseView.as_view(), name='Data_science'),
    path('services/Data_science/<int:id_course>/', views.courseDetail, name='course_detail'),
]


