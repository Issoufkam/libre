# Utilisation de l'image Python 3.10 officielle en tant qu'image de base
FROM python:3.10

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie de tous les fichiers du répertoire de construction dans le répertoire de travail du conteneur
COPY . /app

# Installation des dépendances depuis requirements.txt
RUN pip install -r requirements.txt \
    && echo "Requirements installed successfully."

# Exposition du port 8000 pour accéder à l'application
EXPOSE 8000

# Commande pour exécuter le serveur Django, accessible depuis l'extérieur du conteneur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
