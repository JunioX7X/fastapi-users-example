# 🚀 FastAPI Users Example | API de Gestión de Usuarios

¡Bienvenido al proyecto **FastAPI Users Example**! Una API sencilla para gestionar usuarios, construida con FastAPI y desplegada con un flujo de trabajo profesional de Git y GitHub. Ideal para aprender buenas prácticas de desarrollo y versionamiento.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)

## 📌 Descripción

Este proyecto demuestra cómo construir dos endpoints REST básicos:
- **POST /users**: Guarda un usuario en memoria (o en una base de datos si escalas el proyecto).
- **GET /users**: Retorna la lista de usuarios guardados.

Además, sigue un flujo de Git con ramas `main`, `staging`, `develop` y ramas de características para un desarrollo colaborativo y ordenado.

---

## 🛠 Requisitos Previos

- Python 3.7+
- Git instalado
- Cuenta en GitHub

---

## 🚀 Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/fastapi-users-example.git
   cd fastapi-users-example

   🌳 Estructura del Repositorio
Rama	Descripción
main	Versión estable y lista para producción.
staging	Entorno de pre-producción para pruebas finales.
develop	Rama de integración para features completados.
feature-*	Ramas temporales para nuevas funcionalidades (ej: feature-get-user).


🔄 Flujo de Trabajo con Git
Crea una rama desde develop:

bash
git checkout develop
git pull origin develop
git checkout -b feature-nueva-funcionalidad
Haz commits descriptivos:

bash
git add .
git commit -m "feat: Agrega endpoint para eliminar usuarios"
Sube tu rama y crea un Pull Request (PR):

bash
git push -u origin feature-nueva-funcionalidad
Ve a GitHub > Pull Requests > New PR (desde feature-* hacia develop).

Después de aprobación, fusiona a develop ✅
Luego, sigue el flujo hacia staging y finalmente a main.
