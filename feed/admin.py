from django.contrib import admin

from .forms import PostForm
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')
    form = PostForm

admin.site.register(Post, PostAdmin)