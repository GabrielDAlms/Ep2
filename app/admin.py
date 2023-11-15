from django.contrib import admin

from .models import Post, Comentario, List, Category
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(List)
admin.site.register(Category)
