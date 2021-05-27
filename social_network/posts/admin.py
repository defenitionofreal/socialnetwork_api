from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created')
    list_filter = ('created', 'updated', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)} # поле slug заполняется автоматом
    raw_id_fields = ('author',)
    date_hierarchy = 'created'