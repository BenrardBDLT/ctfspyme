from flask import Flask, render_template, request, redirect, session, url_for
import threading
import subprocess
import socket

app = Flask(__name__)
app.secret_key = "votre_clé_secrète" 
  # Remplacez "your_secret_key" par votre clé secrète réelle

def start_epreuve():
    # Code pour lancer l'épreuve
    subprocess.run(["python", "socket/serveursocket.py"])

# Route pour la page de connexion
@app.route('/', methods=['GET', 'POST'])
def login():
    session['logged_in'] = False
    loginpblm = request.args.get('loginfault') == 'true'
    return render_template('connexion.j2', loginfault = loginpblm)

@app.route('/post-login', methods=['POST'])
def post_login():
    """Fonction exécutée lorsque l'utilisateur soumet le formulaire de connexion.
    Elle effectue la vérification des identifiants et redirige en conséquence.
    """
    name = request.form['username']
    password = request.form['password']

    if name == 'Axel' and password == 'start':
        session['logged_in'] = True
        return redirect(url_for('index'))  # Rediriger vers la page principale
    else:
        return redirect("/?loginfault=true")  # Rediriger vers la page de connexion

# Route pour la page principale
@app.route('/main', methods=['GET', 'POST'])
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    flagpblm = request.args.get('flagpblm') == 'true'

    return render_template('main.j2', flagpblm=flagpblm)
        

    return render_template('main.j2')
@app.route('/flag-post', methods= ['POST'])
def postflag():
    if request.method == 'POST':
        flag = request.form.get("flag")

        if flag == 'FLAG{Louis_le_hacker}':
            return redirect('/main')
        else:
            return redirect('/main?flagpblm=true')
            
# Routes pour les pages d'épreuves
@app.route('/epreuve1')
def page1():
    return render_template('epreuve1.j2')

@app.route('/epreuve2')
def page2():
    return render_template('main.j2')

@app.route('/start_server')
def start_server_route():
    # Exécuter le script start_epreuve() dans un thread séparé
    epreuve_thread = threading.Thread(target=start_epreuve)
    epreuve_thread.start()
    return "Script d'épreuve lancé avec succès!"

@app.route('/epreuve3')
def page3():
    ip = request.remote_addr  # Récupère l'adresse IP du client
    return render_template('epreuve3.j2', ip=socket.gethostbyname(socket.gethostname()))

@app.route('/epreuve4')
def page4():
    reponse = request.args.get('reponse') == 'true'
    return render_template('epreuve4.j2', reponse = False)

@app.route('/post-reponse', methods= ['POST'])
def page_reponse():
    reponse = request.form.get('reponse')
    if reponse == 'pl. du chateau, jumilhac-le-grand':
        session['flag_correct'] = True
    else:
        session['flag_correct'] = False
    return redirect('/epreuve5')
@app.route('/epreuve5')
def page5():
    return render_template('epreuve5.j2')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)