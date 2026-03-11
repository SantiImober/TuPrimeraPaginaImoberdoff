from django.shortcuts import render, redirect
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})


def autor_crear(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AuthorForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Nuevo Autor"})


def categoria_crear(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoryForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Nueva Categoría"})


def post_crear(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/formulario.html", {"form": form, "titulo": "Nuevo Post"})


def buscar(request):
    form = SearchForm(request.GET or None)
    resultados = []
    if form.is_valid():
        query = form.cleaned_data["query"]
        resultados = Post.objects.filter(title__icontains=query)
    return render(request, "blog/buscar.html", {"form": form, "resultados": resultados})

def autor_lista(request):
    autores = Author.objects.all()
    return render(request, "blog/autor_lista.html", {"autores": autores})


def categoria_lista(request):
    categorias = Category.objects.all()
    return render(request, "blog/categoria_lista.html", {"categorias": categorias})


def post_lista(request):
    posts = Post.objects.all()
    return render(request, "blog/post_lista.html", {"posts": posts})