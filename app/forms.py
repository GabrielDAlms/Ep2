from django.forms import ModelForm
from .models import Post, Comentario, Category


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
            "categoria": "Categoria do post",
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

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name','description')