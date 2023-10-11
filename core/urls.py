from django.urls import path
from .views import HomeView, ServicesView, ProjectsView, AboutView, BlogView, Blog_detailsView, ElementsView, ContactView


urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('services/', ServicesView.as_view(), name='services'),
    path('project/', ProjectsView.as_view(), name='project'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog_details/', Blog_detailsView.as_view(), name='blog_details'),
    path('elements/', ElementsView.as_view(), name='elements'),
    path('contact/', ContactView.as_view(), name='contact')
]
