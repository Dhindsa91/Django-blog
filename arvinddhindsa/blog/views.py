from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



# posts =[{
#     'author': 'Arvind',
#     'title': 'Blog Post 1',
#     'content': 'First Post Content',
#     'date_posted': 'August 27, 2018'},

# {
#     'author': 'Dhindsa',
#     'title': 'Blog Post 2',
#     'content': 'Second Post Content',
#     'date_posted': 'August 28, 2018'}
# ]


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all(), #Post is a model we created, so we can use pythons ORM to get all the posts
    }
    return render(request,'blog/home.html', context)  #Everything we are sending to the template


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


