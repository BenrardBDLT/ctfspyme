from flask import Flask, render_template, request, redirect, url_for
import threading
import subprocess

app = Flask(__name__)


def start_server():
    # Code pour lancer l'épreuve
    subprocess.run(["python", "socket\serveursocket.py"]) 

# Route pour la page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('connexion.j2')

# Route pour la page principale
@app.route('/main', methods=['POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Axel' and password == 'start':
            return render_template('main.j2')
    if request.method == 'POST' and 'home-form' in request.form:
        return render_template('main.j2')
    else:
        return redirect('/')

    flag = request.form.get("flag")
    if flag == 'flag':
        return render_template('main.j2')
    else:
        return render_template('main.j2', flagpblm=True)

# Routes pour les pages d'épreuves
@app.route('/epreuve1')
def page1():
    return render_template('epreuve1.j2')

@app.route('/epreuve2')
def page2():
    return render_template('main.j2')

@app.route('/start_server')
def start_server_route():
    # Exécuter le script start_server() dans un thread séparé
    epreuve_thread = threading.Thread(target=start_server)
    epreuve_thread.start()
    return "Script d'épreuve lancé avec succès!"

@app.route('/epreuve3')
def page3():
    return render_template('epreuve3.j2')

@app.route('/epreuve4')
def page4():
    return render_template('epreuve4.j2')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)