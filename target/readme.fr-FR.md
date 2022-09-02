[![Licence GitHub](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)

## Approche

1. Environnement virtuel

   Chaque développeur a ses préférences en choisissant des outils pour définir un environnement virtuel, pour cette implémentation I a choisi d'utiliser pipenv qui utilise Pipfile au lieu use Cependant, un fichier requirements.txt sera fourni pour faciliter d'autres développeurs à utiliser cette implémentation.

## Prérequis

1. Bibliothèques

   Comme décrit dans les fichiers Pipfile et requirements.txt les bibliothèques nécessaires pour exécuter cette implémentation sont :

   * django==3.2.8
   * djangorestframework==3.12.4
   * drf-yasg==1.20.0
   * psycopg2-binary==2.9.1

## Comment utiliser

1. Construisez les images en exécutant
   ```
   $ docker-compose up -d --build
   ```
2. Faire les migrations L'implémentation vient avec la migration api app effectuée, le dev a juste besoin de "migrer"
   ```
   $ docker-compose exec eye_web python manage.py migrate
   ```
3. Créer un super utilisateur
   ```
   $ docker-compose exec eye_web python manage.py createsuperuser
   ```


### Points de terminaison

Tous les points de terminaison disponibles avec la documentation générée automatiquement peut être consulté via le lien

* http://localhost:8000/swagger/ : 8000/swagger/

L'accès dans l'api a le préfixe suivant : http://localhost:8000/api/... : 8000/api/...

Inhabituellement pour cette implémentation, j'ai créé une dynamique unique point de fin qui gère tous les cas d'utilisation attendus.

Exemplo: :

* http://localhost:8000/api/ : 8000/api/

Tipo de dados :

L'api autorise uniquement l'insertion de données sur le point de terminaison http://localhost:8000/api/ : 8000/api/ en suivant l'exemple suivant :

    { "session_id" : "e2085be5-9137-4e4e-80b5-f1ffddc25423", "category" : "page interaction", "nom" : "pageview", "data" : [ { "host" : "www.consumeraffairs.com", "path" : "/" } ], "timestamp" : "2021-01-01T09:15:27.243860Z" } ou { "session_id" : "e2085be5-9137-4e4e-80b5-f1ffddc25423", "category" : "page interaction", "nom" : "pageview", "data" : [ { "host" : "www.consumeraffairs.com", "path" : "/", "element" : "chat bulle" } ], "timestamp" : "2021-01-01T09:15:27.243860Z" } ou { "session_id" : "d0ee6b24-e21c-46e5-882a-a48ff51da189", "catégorie" : "interaction de forme", "nom" : "soumettre", "data" : [ { "host" : "www.consumeraffairs.com", "path" : "/", "forme" : [ { "first_name" : "John", "last_name" : "Doe" } ] } ], "timestamp" : "2021-10-13T04:16:44Z" }
NB : Pour toutes les listes, l'analyseur s'attend à un dictionnaire à l'intérieur de celui-ci (assurez-vous de suivre le modèle pour les variables "données" et "formulaire").

## Auteur de l'auteur de l'Éducation

* **Andy Kiaka** - *Job Completo* - [detona115](https://github.com/detona115)

---
de ❤️ por [detona115](https://github.com/detona115) 😊