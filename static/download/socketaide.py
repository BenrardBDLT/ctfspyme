import socket
import sys

import subprocess

subprocess.Popen(["python", "serveursocket.py"])
host= socket.gethostbyname(socket.gethostname())
server_ip = host
#mettez ci dessus l'adresse que vous voyez affiché à l'ecran, elle vous permet de communiquer avec le serveur 
server_port = 2000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    client_socket.connect((server_ip, server_port))
except ConnectionRefusedError:
    print("Impossible de se connecter au serveur.")
    sys.exit(1)

while True:
    # Réception des données du serveur
    data = client_socket.recv(1024).decode()
    print(data)
   
    response = input("Réponse : ")
    # Envoi de la réponse au serveur
    client_socket.send(response.encode())
    data = client_socket.recv(1024).decode()
    print("Réponse du serveur:", data)

client_socket.close()