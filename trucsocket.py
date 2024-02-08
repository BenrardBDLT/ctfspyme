import socket
import sys

# Définition des informations du serveur
server_ip = '172.18.193.60'  # Adresse IP du serveur
server_port = 2000  # Port du serveur
timeout = 10  # Délai maximum d'attente pour la réponse du serveur (en secondes)

# Création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    client_socket.connect((server_ip, server_port))
except ConnectionRefusedError:
    print("Impossible de se connecter au serveur.")
    sys.exit(1)

# Configuration du délai d'attente pour la réception des données
client_socket.settimeout(timeout)

# Boucle de communication avec le serveur
while True:
    # Réception des données du serveur
    try:
        data = client_socket.recv(1024).decode()
    except socket.timeout:
        print("La réponse du serveur a pris trop de temps. Fermeture de la communication.")
        break

    if not data:
        print("La connexion avec le serveur a été interrompue.")
        break

    print("Question du serveur:", data)

    # Saisie de la réponse depuis la console
    response = input("Réponse : ")

    # Envoi de la réponse au serveur
    client_socket.send(response.encode())

    # Réception de la réponse du serveur
    try:
        data = client_socket.recv(1024).decode()
    except socket.timeout:
        print("La réponse du serveur a pris trop de temps. Fermeture de la communication.")
        break

    if not data:
        print("La connexion avec le serveur a été interrompue.")
        break

    if data == "Incorrect":
        print("Réponse incorrecte. Fermeture de la communication.")
        break

    print("Réponse du serveur:", data)

    # Vérification si la communication doit être terminée
    if data == "Fin de la communication.":
        break

# Fermeture de la connexion
client_socket.close()