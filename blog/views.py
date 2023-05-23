from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Leon',
    'title': 'Blog post 1',
    'content': 'First Post Content',
    'date_posted': 'June 27, 2023 '
},
{
    'author': 'Corey',
    'title': 'Blog post 2',
    'content': 'second Post Content',
    'date_posted': 'August 27, 2023 '
},

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})