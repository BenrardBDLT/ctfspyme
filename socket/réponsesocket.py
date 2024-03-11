import socket
import sys

server_ip = '35.173.69.207'
server_port = 443
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
    result = eval(data)
   

    # Envoi de la réponse au serveur
    client_socket.send(str(result).encode())
    data = client_socket.recv(1024).decode()
    print("Réponse du serveur:", data)

client_socket.close()