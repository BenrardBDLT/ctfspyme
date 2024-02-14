import socket
import sys

server_ip = '172.0.0.1'
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
    data = client_socket.recv(1024).decode()

    if not data:
        print("La connexion avec le serveur a été interrompue.")
        break

    print("Question du serveur:", data)

    # Extraction des opérandes et de l'opérateur de la question
    try:
        parts = data.split()
        operand1 = int(parts[1])
        operator = parts[2]
        operand2 = int(parts[3])
    except (IndexError, ValueError):
        print("Question du serveur invalide.")
        break

    # Calcul de la réponse
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    else:
        print("Opérateur invalide dans la question du serveur.")
        break

    # Envoi de la réponse au serveur
    client_socket.send(str(result).encode())
    data = client_socket.recv(1024).decode()
    print("Réponse du serveur:", data)

client_socket.close()