from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("autores/", views.autor_lista, name="autor_lista"),
    path("autores/nuevo/", views.autor_crear, name="autor_crear"),
    path("categorias/", views.categoria_lista, name="categoria_lista"),
    path("categorias/nueva/", views.categoria_crear, name="categoria_crear"),
    path("posts/", views.post_lista, name="post_lista"),
    path("posts/nuevo/", views.post_crear, name="post_crear"),
    path("buscar/", views.buscar, name="buscar"),
]