import socket
import threading
import time
import random

def handle_client(client_socket):
    correct_answers = 0
    time_limit = 10
    difficulty_range = (1, 10)

    while correct_answers < 100:
        num1 = random.randint(*difficulty_range)
        num2 = random.randint(*difficulty_range)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            expected_result = num1 + num2
        elif operator == '-':
            expected_result = num1 - num2
        else:
            expected_result = num1 * num2

        client_socket.send(f"Calculez {num1} {operator} {num2} en {time_limit} secondes: ".encode())

        client_socket.settimeout(time_limit)
        try:
            response = client_socket.recv(1024).decode().strip()
            print(response)
        except socket.timeout:
            print("Temps écoulé")
            client_socket.send(f"Temps écoulé. Veuillez répondre dans le temps imparti.".encode())
            correct_answers = 0
            return

        try:
            if int(response) == expected_result:
                correct_answers += 1
                print(correct_answers)
                client_socket.send("Bonne réponse. Calculez le prochain.".encode())
                difficulty_range = (difficulty_range[0] * 2, difficulty_range[1] * 2)
                time_limit = max(1, time_limit // 1.2)
            else:
                client_socket.send("Mauvaise réponse. Connexion fermée.".encode())
                client_socket.close()
                return
        except ValueError:
            client_socket.send("Erreur de calcul. Veuillez répondre avec un nombre valide.".encode())
            print(("Erreur de calcul. Veuillez répondre avec un nombre valide.".encode()))
            
            return

    client_socket.send("FLAG: jaimelescalculs.".encode())
    client_socket.close()

def start_server():
    host = socket.gethostbyname(socket.gethostname())
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur en écoute sur {host}:{port}...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connexion acceptée depuis {address[0]}:{address[1]}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()