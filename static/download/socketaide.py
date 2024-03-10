import socket
import sys

server_ip = '192.168.68.55'
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