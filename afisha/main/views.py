import datetime

from django.shortcuts import render,redirect

from main.models import Category,Actor,Director,Movie,Review
from main.forms import MovieForm,DirectorForm,RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def news(request):
    dict_={

        'key': 'Cartoons',
        'color': 'red',
        'list_': ["Maikraft", 'Tomy and Jery', 'Alady','Aktan Akylai']
    }
    return render(request,'news.html',context=dict_)
def movie_list_view(request):
    movie=Movie.objects.all()
    context={
     #  'movie_list': movie,
       'movie_list': Movie.objects.all(),
       'category_list': Category.objects.all()
    }
    return render(request, 'movie.html', context=context)


def movie_detail_view(request,id):
    movie = Movie.objects.get(id=id)
    return render(request, 'detail.html', context={'movie_detail': movie,
                                                   'category_list':Category.objects.all(),
                                                   'reviews': Review.objects.filter(movie=movie)})

def category_movie_filter_view(request,category_id):
    context = {
        'movie_list': Movie.objects.filter(category_id=category_id),
        'category_list': Category.objects.all()
    }
    return render(request, 'movie.html', context=context)
def add_news(request):
    print("  ..............           ")
    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    if len(str(day)) == 1:
        day = "0"+str(day)
    if len(str(month)) == 1:
        month = "0"+str(month)
    print(year, month, day)
    print(" .........               ")
def national(request):
    return render(request,'national.html')

def children(request):
    return render(request, 'children.html')

def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movie/')
        return render(request,'add_movie.html',context={
            'form': form,
            'category_list':Category.objects.all()
        })

def add_director_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movie/')
        return render(request, 'add_director.html', context={
            'form': form,
            'category_list': Category.objects.all()
        })


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', context={
        'form': form
    })
def login_view(request):
    form = LoginForm()
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user=user)
        return redirect('/login/')
    return render(request, 'login.html',context={
        'form': form
    })