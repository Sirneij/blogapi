from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_created', 'date_updated',)
    search_fields = ('title', 'author',)
    list_filter = ('author', 'date_created', 'date_updated',)
    prepopulated_fields = {'slug': ('title',)}
