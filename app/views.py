from django.shortcuts import render
# import requests
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Postagem, Comentario, List
from .forms import PostForm, ComentarioForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

###############################################

# # Apenas views funcionais
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post
# from django.http import HttpResponse

# # Listar todos os posts
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# # Detalhes de um post
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'blog/post_detail.html', {'post': post})

# # Criar um novo post
# def post_create(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         content = request.POST['content']
#         Post.objects.create(title=title, content=content)
#         return redirect('post_list')
#     return render(request, 'blog/post_form.html')

# # Atualizar um post
# def post_update(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         post.title = request.POST['title']
#         post.content = request.POST['content']
#         post.save()
#         return redirect('post_list')
#     return render(request, 'blog/post_form.html', {'post': post})

# # Excluir um post
# def post_delete(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_confirm_delete.html', {'post': post})

####################################################

# # Apenas views funcionais com uma django form
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post
# from .forms import PostForm

# # Listar todos os posts
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# # Detalhes de um post
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'blog/post_detail.html', {'post': post})

# # Criar um novo post
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_form.html', {'form': form})

# # Atualizar um post
# def post_update(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_form.html', {'form': form})

# # Excluir um post
# def post_delete(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request, 'blog/post_confirm_delete.html', {'post': post})

############################################################

# Com classes comuns
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Post

# # Listar todos os posts
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'

# # Detalhes de um post
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'

# # Criar um novo post
# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/post_form.html'
#     success_url = reverse_lazy('post_list')

# # Atualizar um post
# class PostUpdateView(UpdateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'blog/post_form.html'
#     context_object_name = 'post'
#     success_url = reverse_lazy('post_list')

# # Excluir um post
# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'blog/post_confirm_delete.html'
#     context_object_name = 'post'
#     success_url = reverse_lazy('post_list')

############################################################

# Usada
def PostDetail(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)
    if 'last_viewed' not in request.session:
        request.session['last_viewed'] = []
    request.session['last_viewed'] = [post_id
                                      ] + request.session['last_viewed']
    if len(request.session['last_viewed']) > 5:
        request.session['last_viewed'] = request.session['last_viewed'][:-1]
    context = {'post': post}
    return render(request, 'app/detail.html', context)

class PostListView(generic.ListView):
    model = Postagem
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'last_viewed' in self.request.session:
            context['last_posts'] = []
            for post_id in self.request.session['last_viewed']:
                context['last_posts'].append(
                    get_object_or_404(Postagem, pk=post_id))
        return context


def PostSearch(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET["query"].lower()
        post_list = Postagem.objects.filter(name__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, "app/search.html", context)


@login_required
@permission_required('app.add_post')
def PostCreate(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = Postagem(**post_form.cleaned_data)
            post.save()
            return HttpResponseRedirect(
                reverse('app:detail', args=(post.pk, )))

    else:
        post_form = PostForm()
    context = {"post_form": post_form}
    return render(request, "app/create.html", context)

@login_required
@permission_required('app.update_post')
def PostUpdate(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.name = form.cleaned_data["name"]
            post.categoria = form.cleaned_data["categoria"]
            post.image_url = form.cleaned_data["image_url"]
            post.texto = form.cleaned_data["texto"]
            post.save()
            return HttpResponseRedirect(reverse('app:detail', args=(post.id,)))
    else:
        form = PostForm(
            initial={
                "name": post.name,
                "categoria": post.categoria,
                "image_url": post.image_url,
                "texto": post.texto,
            }
        )
    context = {"post": post, "form": form}
    return render(request, "app/update.html", context)

@login_required
@permission_required('app.delete_post')
def PostDelete(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('app:index'))

    context = {"post": post}
    return render(request, "app/delete.html", context)

@login_required
def create_comentario(request, post_id):
    post = get_object_or_404(Postagem, pk=post_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario_author = request.user
            comentario_text = form.cleaned_data["text"]
            comentario = Comentario(author=comentario_author, text=comentario_text, post=post)
            comentario.save()
            return HttpResponseRedirect(reverse('app:detail', args=(post_id,)))
    else:
        form = ComentarioForm()
    context = {"form": form, "post": post}
    return render(request, "post/comentario.html", context)


class ListListView(generic.ListView):
    model = List
    template_name = "app/lists.html"


class ListCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     generic.CreateView):
    model = List
    template_name = 'app/create_list.html'
    fields = ['name', 'author', 'app']
    success_url = reverse_lazy('app:lists')
    permission_required = 'app.add_list'

def home(request):
    return render(request,'home.html')
