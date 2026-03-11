# TuPrimeraPaginaImoberdoff

Blog desarrollado con Django usando el patrón MVT.

## Instalación
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Orden para probar las funcionalidades

1. Entrar al admin en /admin y crear al menos un Autor y una Categoría
2. Crear un Post desde /posts/nuevo/
3. Ver la lista de posts en /posts/
4. Buscar posts en /buscar/

## URLs disponibles

| URL | Descripción |
|-----|-------------|
| / | Inicio |
| /posts/ | Lista de posts |
| /posts/nuevo/ | Formulario nuevo post |
| /autores/ | Lista de autores |
| /autores/nuevo/ | Formulario nuevo autor |
| /categorias/ | Lista de categorías |
| /categorias/nueva/ | Formulario nueva categoría |
| /buscar/ | Buscador de posts |
| /admin/ | Panel de administración |