from django.db import models
from datetime import date
# Create your models here.
#from django.utils.safestring import mark_safe


class Category(models.Model):
    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'

    objects = None
    name=models.CharField(max_length=150,unique=True,verbose_name='Название')

    def __str__(self):
        return self.name



class Actor(models.Model):
    class Meta:
        verbose_name='Астер'
        verbose_name_plural='Акторы'
    name = models.CharField(max_length=100,verbose_name="Название")
    age = models.PositiveIntegerField(default=0,verbose_name="Возраст")
    image = models.ImageField(upload_to='actors',verbose_name="Картинка")

    def __str__(self):
        return self.name



class Director(models.Model):
    class Meta:
        verbose_name='Режиссер'
        verbose_name_plural='Режиссеры'
    name = models.CharField(max_length=100,verbose_name="Название")

    def __str__(self):
        return self.name



class Movie(models.Model):
    class Meta:
        verbose_name='фильм'
        verbose_name_plural='фильмы'
    objects = None
    tittle = models.CharField(max_length=1000,unique=True,verbose_name="Название")
    description = models.TextField(blank=True,verbose_name="Описание фильмы")
    year = models.PositiveSmallIntegerField(default=2000,verbose_name="Год")
    image = models.ImageField(upload_to='image', null=True,verbose_name="Картинка")
    directors = models.ForeignKey(Director, on_delete=models.SET_NULL, blank=True, null=True,
                                  verbose_name="Режиссеры")
    actors = models.ManyToManyField(Actor, max_length=100,verbose_name="Актеры")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата изменения")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,verbose_name="Категория"
    )

    def __str__(self):
        return self.tittle
    @property
    def actors_list(self):
        return ''.join([actors.name for actors in self.actors.all()])



class Review(models.Model):
    class Meta:
        verbose_name='отзыв'
        verbose_name_plural='отзывы'
    objects = None
    text = models.TextField(verbose_name="Текст отзыва")
    author = models.CharField(max_length=100, null=True, blank=True, default='')
    #email = models.EmailField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews',
    verbose_name='Фильм')

    def __str__(self):
        return f"{self.author}-{self.movie}"



