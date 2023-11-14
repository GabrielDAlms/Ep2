from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = "app"
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path("search/", views.PostSearch, name="search"),
    path("create/", views.PostCreate, name="create"),
    path("<int:post_id>/", views.PostDetail, name="detail"),
    path("update/<int:post_id>/", views.PostUpdate, name="update"),
    path("delete/<int:post_id>/", views.PostDelete, name="delete"),
    path("<int:post_id>/comentario/", views.create_comentario, name="comentario"),
    path("lists/", views.ListListView.as_view(), name="lists"),
    path("lists/create", views.ListCreateView.as_view(), name="create-list"),
    path('', views.home,name='home'),
]