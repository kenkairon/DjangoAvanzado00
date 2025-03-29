# DjangoAvanzado00
Educativo y de Aprendizaje Personal

---
## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
- [Configuración Base de datos](#configuración-Base-de-datos)
  - [Creación del Modelo ](#creación-del-modelo)
  - [Creamos el superusuario](#creamos-el-superusuario)
  - [Parte 2](#parte-2)
  - [Parte 3](#parte-3)
  - [Parte 4](#parte-4)
---

## Requisitos
- Django 4.0 o superior
---


## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django 
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip

5. Ver la versión que tengo instalada en django 
    ```bash
    python -m django --version
## Guardar las dependencias
6. Instalación dependencias
    ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto

6. Crear el Proyecto
    ```bash
    cd config
    django-admin startproject codigofacilito

7. Ingresar al directorio del Proyecto
    ```bash
    cd codigofacilito

8. Creamos la Aplicación categories
    ```bash
   python manage.py startapp categories


