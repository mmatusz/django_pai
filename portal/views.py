from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import json
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'portal/home.html' ##zmiana
    context_object_name = 'posts'
    ordering = ['-post_date']

class PostDetailedView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False


def about(request):
    return render(request, 'portal/about.html', {'title': 'About'})

##def testVue(request):
  ##  return render(request, 'portal/test_vue.html')

