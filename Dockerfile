# Utilise une image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer les ports pour Flask (5001) et Streamlit (8501)
EXPOSE 5001
EXPOSE 8501

# Démarrer Flask ou Streamlit via docker-compose
CMD ["echo", "Use docker-compose to run Flask or Streamlit"]
