from django.contrib import admin
from test_tree.models import Genre

# Register your models here.
#admin.site.register(Genre)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk','name','parent')


admin.site.register(Genre, GenreAdmin)