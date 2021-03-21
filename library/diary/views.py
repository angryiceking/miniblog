from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse
from django.views.generic import View

from .models import BlogPost
# Create your views here.

class About(View):

    def get(self, request):
        return render(request, 'about.html', status=200)


class DiaryHome(View):

    def get(self, request):
        blogs = BlogPost.objects.all()
        return render(request, 'diary.html', context={'blogs': blogs})


class DiaryLogEntryView(View):

    def get(self, request, blog_id):
        blogs = BlogPost.objects.get(pk=blog_id)
        print(blogs)
        return render(request, 'diary-entry.html', context={'blogs': blogs})


class Contact(View):

    def get(self, request):
        return render(request, 'contact.html', status=200)


class Minigame(View):

    def get(self, request):
        return render(request, 'game-demo.html', status=200)