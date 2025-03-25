# Aplicación de ejemplo con Docker

Esta es una aplicación simple de Flask para demostrar el uso de Docker.

## Instrucciones

1. Construir la imagen de Docker:
```bash
docker build -t mi-app-flask .
```

2. Ejecutar el contenedor:
```bash
docker run -p 5000:5000 mi-app-flask
```

3. Visitar la aplicación en el navegador:
http://localhost:5000

## Subir a GitHub

1. Crear un nuevo repositorio en GitHub
2. Inicializar el repositorio local y subir los cambios:
```bash
git init
git add .
git commit -m "Primera versión de la aplicación Docker"
git branch -M main
git remote add origin <URL_DE_TU_REPOSITORIO>
git push -u origin main
```
