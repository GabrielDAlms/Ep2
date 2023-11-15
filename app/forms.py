from django.forms import ModelForm
from .models import Post, Comentario


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "name",
            "categoria",
            "image_url",
            "texto",
        ]
        labels = {
            "name": "Título",
            "categoria": "Categoria de Investimento",
            "image_url": "URL da Imagem",
            "texto": "Texto"
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = [
            "text",
        ]
        labels = {
            "text": "Comentário",
        }
