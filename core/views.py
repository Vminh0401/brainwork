from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'assets/index.html')


class ServicesView(View):
    def get(self, request):
        return render(request, 'assets/services.html')


class ProjectsView(View):
    def get(self, request):
        return render(request, 'assets/project.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'assets/about.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'assets/blog.html')


class Blog_detailsView(View):
    def get(self, request):
        return render(request, 'assets/blog_details.html')


class ElementsView(View):
    def get(self, request):
        return render(request, 'assets/elements.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'assets/contact.html')
