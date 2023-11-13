from django.contrib import admin

from .models import Postagem, Comentario, List
admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(List)
