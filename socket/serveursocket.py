
import socket
import random
import threading
communication_count = 0
def calcul(com):
    a = random.randint(1, 4)
    calcul = ''
    nb=a + com
    for i in range(nb):
        op = random.choice(['*', '+', '-'])
        valeur = str(random.randint(1, 9))
        calcul = calcul + valeur + op
    valeur = str(random.randint(1, 9))
    calcul = calcul + valeur

    resultat_calcul = eval(calcul)
    print('le calcul envoyé est : ', calcul)
    print('le résultat attendu est : ',resultat_calcul)
    return (calcul, resultat_calcul)

def handle_client(client_socket, addr):
    fin =False
    print("Connexion établie avec", addr)

    client_socket.settimeout(10)  # Définir un délai de 10 secondes pour recevoir les réponses du client

    communication_count = 0  # Compteur de communications avec le client
    calcul_str, resultat_calcul = calcul(communication_count)
   
    #client_socket.send(("\n \nRépondez à ces 100 calculs pour tenter de récupérer le flag. Répondez en moins de 10s pour chaque calcul\n************************************************************\n"+calcul_str).encode())
    client_socket.send(calcul_str.encode())
    response = client_socket.recv(1024).decode()
    if not response:
       
        fin=True
    print("Réponse reçue du client:", response)

    if response.lower() == "exit":
        client_socket.close()
        fin=True
    if response == str(resultat_calcul):
        communication_count += 1
        client_socket.send("Correct!".encode())
    else:
        client_socket.send("Incorrect!".encode())
        client_socket.close()
        fin =True    
   
    while True:
        if fin==True:
            break
        try:
            calcul_str, resultat_calcul = calcul(communication_count)
            client_socket.send(calcul_str.encode())
           
            response = client_socket.recv(1024).decode()
            if not response:
               
                break
            print("Réponse reçue du client:", response)

            if response.lower() == "exit":
                client_socket.close()
                break  # Sortir de la boucle et fermer la communication avec le client

            if response == str(resultat_calcul):
                communication_count += 1  # Incrémenter le compteur de communications
                client_socket.send("Correct!".encode())
            else:
                client_socket.send("Incorrect!".encode())
                break  # Sortir de la boucle et fermer la communication avec le client
            print("Nombre de communications avec le client", addr, ":", communication_count)
            if communication_count == 100:
                client_socket.send("Flag: {Weuve_le_malefique} ".encode())
                client_socket.close()
               
        except socket.timeout:
            print("Le client ne répond pas dans les 10 secondes.")
            client_socket.send("Trop lent !".encode())
            break  # Sortir de la boucle et fermer la communication avec le client

    client_socket.send("Déconnexion...".encode())
    return

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host= socket.gethostbyname(socket.gethostname())
    
    server_socket.bind((host, 443))
    print(host)
    server_socket.listen(5)
    print("Serveur en attente de connexions...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

start_server()
