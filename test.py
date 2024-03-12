import os

# Chemin vers le fichier à protéger
chemin_fichier = "static\download\serveursocket.py"

# Modifier les permissions pour rendre le fichier non lisible
os.chmod(chemin_fichier, 0o644)