from django.shortcuts import render
# from django.http import HttpResponse
posts = [
    {
        'author': 'Test Author 1',
        'title': 'Blog Test Post 1',
        'content': 'Test post content 1',
        'date_posted': 'September 4, 2018',
    },
    {
        'author': 'Test Author 2',
        'title': 'Blog Test Post 2',
        'content': 'Test post content 2',
        'date_posted': 'November 14, 2018',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home...</h1>')


def about(request):
    return render(request, 'blog/about.html')


def jinja(request):
    return render(request, 'blog/jinja.html')
