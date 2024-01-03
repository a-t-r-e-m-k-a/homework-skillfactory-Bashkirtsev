from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("caption", "Author")
    list_filter = ('category', 'caption', "Author")


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
