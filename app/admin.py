from django.contrib import admin

from .models import Postagem, Comentario, List, Category
admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(List)
admin.site.register(Category)
