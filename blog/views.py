from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html' , {'blog':blog})
def details(request, blog_id):
    detailsblog = get_object_or_404(Blog, pk= blog_id)
    return render(request, 'blog/details.html', {'blog':detailsblog})
