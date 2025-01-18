from django.shortcuts import render
from .models import Blog, BlogImage, Category, Comment
# Create your views here.

def blog_page(request):
    bloglar = Blog.objects.all()
    kategoriyalar = Category.objects.all()

    context = {
        'bloglar': bloglar,
        'kategoriyalar': kategoriyalar
    }
    return render(request, template_name='index.html', context=context)
