from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author' : 'Miki',
        'title' : 'Post numer 1',
        'content' : 'Zawartosc posta 1',
        'date': '10.05.2020'
    },
    {
        'author' : 'GK',
        'title' : '',
        'content' : 'Zawartosc posta 2',
        'date': '20.04.2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'portal/home.html', context)

def about(request):
    return render(request, 'portal/about.html', {'title': 'About'})
