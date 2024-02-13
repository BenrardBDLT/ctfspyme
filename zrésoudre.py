import socket
import sys

'''
répondez à 100 calculs pour forcer le serveur

'''




server_ip = '172.18.194.48'  
server_port = 1234  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    client_socket.connect((server_ip, server_port))
except ConnectionRefusedError:
    print("Impossible de se connecter au serveur.")
    sys.exit(1)

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
    data = client_socket.recv(1024).decode()
    print("Réponse du serveur:", data)
client_socket.close()
