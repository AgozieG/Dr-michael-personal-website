from django.shortcuts import render


def index(request):
    return render(request, 'app1/index.html')

def base(request):
    return render(request, 'app1/base.html')

def about(request):
    return render(request, 'app1/about.html')

def books(request):
    return render(request, 'app1/books.html')

def journals(request):
    return render(request, 'app1/journals.html')

def news(request):
    return render(request, 'app1/news.html')

def presentations(request):
    return render(request, 'app1/presentations.html')

def pics(request):
    return render(request, 'app1/pics.html')

def training(request):
    return render(request, 'app1/training.html')

def education(request):
    return render(request, 'app1/education.html')

def policy(request):
    return render(request, 'app1/policy.html')

def security(request):
    return render(request, 'app1/security.html')

def mentor(request):
    return render(request, 'app1/mentor.html')

def research(request):
    return render(request, 'app1/research.html')

def rec(request):
    return render(request, 'app1/rec.html')

def test(request):
    return render(request, 'app1/test.html')

def fliers(request):
    return render(request, 'app1/fliers.html')

def advid(request):
    return render(request, 'app1/advid.html')