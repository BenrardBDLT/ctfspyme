import socket
import threading
import time

def handle_client(client_socket):
    correct_answers = 0

    while correct_answers < 3:
        # Générer un calcul aléatoire
        num1 = 5
        num2 = 3
        operator = '+'
        expected_result = num1 + num2

        # Envoyer le calcul au client
        client_socket.send(f"Calculez {num1} {operator} {num2}: ".encode())

        # Attendre la réponse du client dans les 5 secondes
        client_socket.settimeout(2)
        try:
            response = client_socket.recv(1024).decode().strip()
        except socket.timeout:
            client_socket.send("Temps écoulé. Veuillez répondre dans les 5 secondes.".encode())
            client_socket.close()
            return
        # Vérifier la réponse du client
        if int(response) == expected_result:
            correct_answers += 1
            client_socket.send("Bonne réponse. Calculez le prochain.".encode())
        else:
            client_socket.send("Mauvaise réponse. Connexion fermée.".encode())
            client_socket.close()
            return
        

    # Après 3 bonnes réponses
    client_socket.send("Trois bonnes réponses ont été données.".encode())
    print("Trois bonnes réponses ont été données.")

    client_socket.close()

def start_server():
    # Configurer le serveur
    host = '172.18.194.48'
    port = 1234

    # Créer une socket du serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur en écoute sur {host}:{port}...")

    while True:
        # Accepter une nouvelle connexion client
        client_socket, address = server_socket.accept()
        print(f"Connexion acceptée depuis {address[0]}:{address[1]}")

        # Lancer un thread pour gérer la connexion client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()