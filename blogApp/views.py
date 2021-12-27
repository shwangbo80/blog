from django.shortcuts import render
from blogApp.models import Topic, Blog
from html import unescape
# Create your views here.

def index(request):
    blog_list = Blog.objects.order_by()[::-1]
    blog_list = unescape(blog_list)
    my_posts = {"posts" : blog_list}
    return render(request, "blogApp/index.html", context=my_posts)

def blog(request):
    my_dict={"insert_me": "Hello from blog page"}
    return render(request, "blogApp/blog.html", context=my_dict)


