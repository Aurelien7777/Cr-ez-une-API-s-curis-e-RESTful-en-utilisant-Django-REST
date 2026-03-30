# SoftDesk API

API REST sécurisée développée avec Django REST Framework dans le cadre du projet OpenClassrooms.

Cette API permet de gérer :

* les utilisateurs ;
* les projets ;
* les contributeurs ;
* les issues ;
* les commentaires.

L’authentification est sécurisée avec **JSON Web Token (JWT)**.

---

## Objectifs du projet

Ce projet répond aux exigences suivantes :

* mise en place d’une API RESTful avec Django REST Framework ;
* authentification sécurisée avec JWT ;
* gestion des permissions selon le rôle de l’utilisateur ;
* respect des contraintes RGPD ;
* prise en compte d’une logique de green code avec pagination et filtrage des données.

---

## Fonctionnalités principales

### Utilisateurs

* création de compte ;
* authentification avec JWT ;
* accès et modification de son propre profil uniquement ;
* suppression de son compte (droit à l’oubli).

### Projets

* création d’un projet ;
* le créateur devient automatiquement auteur et contributeur ;
* seuls les contributeurs peuvent consulter un projet ;
* seul l’auteur peut modifier ou supprimer un projet.

### Contributeurs

* ajout d’un utilisateur à un projet ;
* seuls les contributeurs peuvent gérer les contributeurs.

### Issues

* création d’issues sur un projet ;
* seuls les contributeurs peuvent créer ou consulter des issues ;
* l’auteur est défini automatiquement ;
* l’assignee doit être contributeur du projet ;
* seul l’auteur peut modifier ou supprimer une issue.

### Commentaires

* création de commentaires sur une issue ;
* seuls les contributeurs du projet peuvent commenter ;
* seul l’auteur peut modifier ou supprimer un commentaire.

---

## Technologies utilisées

* Python 3.12.6
* Django 5.2.12
* Django REST Framework 3.16.1
* SimpleJWT (authentification JWT)
* Poetry
* SQLite3

---

## Structure du projet

```
django_project/
├── config/
├── projects/
├── users/
├── manage.py
├── pyproject.toml
├── poetry.lock
└── db.sqlite3
```

---

## Installation

### 1. Cloner le projet

```bash
git clone <URL_DU_REPO>
cd django_project
```

### 2. Installer les dépendances

```bash
poetry install
```

### 3. Activer l’environnement

```bash
poetry shell
```

### 4. Appliquer les migrations

```bash
python manage.py migrate
```

### 5. Lancer le serveur

```bash
python manage.py runserver
```

---

## Authentification JWT

### Obtenir un token

```http
POST /api/token/
```

```json
{
  "username": "mon_user",
  "password": "mon_mot_de_passe"
}
```

### Réponse

```json
{
  "refresh": "...",
  "access": "..."
}
```

### Utilisation du token

Ajouter dans les headers :

```
Authorization: Bearer <access_token>
```

---

## Endpoints

### Utilisateurs

* `POST /api/users/`
* `GET /api/users/`
* `GET /api/users/{id}/`
* `PATCH /api/users/{id}/`
* `DELETE /api/users/{id}/`

### JWT

* `POST /api/token/`
* `POST /api/token/refresh/`

### Projets

* `GET /api/projects/`
* `POST /api/projects/`
* `GET /api/projects/{id}/`
* `PATCH /api/projects/{id}/`
* `DELETE /api/projects/{id}/`

### Contributeurs

* `GET /api/contributors/`
* `POST /api/contributors/`

### Issues

* `GET /api/issues/`
* `POST /api/issues/`

### Commentaires

* `GET /api/comments/`
* `POST /api/comments/`

---

## Sécurité et permissions

* authentification obligatoire via JWT ;
* accès limité aux contributeurs d’un projet ;
* filtrage des données via `get_queryset()` ;
* modification et suppression réservées à l’auteur (`IsAuthorOrReadOnly`) ;
* sécurisation du modèle utilisateur (accès uniquement à son propre profil).

---

## RGPD

* vérification de l’âge minimum (≥ 15 ans) ;
* consentement utilisateur (`can_be_contacted`, `can_data_be_shared`) ;
* accès et modification du profil utilisateur ;
* suppression complète des données (cascade).

---

## Green Code

L’API est conçue dans une logique de sobriété :

* pagination des résultats pour limiter la charge ;
* filtrage des données selon l’utilisateur ;
* limitation des accès inutiles ;
* réponses API simples et non imbriquées.

---

## Tests

Les tests ont été réalisés avec Postman :

* authentification JWT ;
* création utilisateur ;
* gestion des projets ;
* gestion des contributeurs ;
* gestion des issues ;
* gestion des commentaires ;
* validation des permissions.

---

## Dépendances principales

```
django
djangorestframework
djangorestframework-simplejwt
```

---

## Lancement rapide

```bash
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

---

## Auteur

Aurélien Amorin
