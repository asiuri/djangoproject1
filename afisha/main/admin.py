from django.contrib import admin
#from models import Movie
from django.utils.safestring import mark_safe

from .models import Category, Actor, Movie, Director, Review
# Register your models here.

class ReviewAdminInline(admin.StackedInline):
    model=Review
    extra=0

class MovieAdmin(admin.ModelAdmin):
    model=Movie
    list_display ='get_html_photo', 'tittle',' category ', 'actors_list',
    'directors ','created_at',' updated_at'.split()
    search_fields = 'tittle' ,'description'.split()
    list_editable = 'created_at'.split()
    list_filter = 'created_at','updated_at'.split()
    list_per_page = 4
    fields = 'tittle','category','photo','get_html_photo','created_at'.split()
    readonly_fields = 'created_at','updated_at','get_html_photo'.split()

    def get_html_photo(self,object):
        if object.photo:
           return mark_safe(f"<img scr='{object.photo.url} width 300px>")


admin.site.register(Category),
admin.site.register(Actor),
admin.site.register(Director),
admin.site.register(Movie,MovieAdmin),
admin.site.register(Review)