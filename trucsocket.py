import socket

# Définition des informations du serveur
server_ip = '172.18.192.78'  # Adresse IP du serveur
server_port = 2000  # Port du serveur

# Création d'un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((server_ip, server_port))

# Envoi de données au serveur
while True: 
    message = "coucou robin ;)"
    client_socket.send(message.encode())

    # Réception des données du serveur
    data = client_socket.recv(1024).decode()
    print("Réponse du serveur:", data)

    # Fermeture de la connexion
client_socket.close()