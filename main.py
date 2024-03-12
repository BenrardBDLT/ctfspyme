from flask import Flask, render_template, request, redirect, session, url_for
import threading
import subprocess
import socket
import smtplib
app = Flask(__name__)
app.secret_key = "votre_clé_secrète" 
score = 0
validated_flags = []
  # Remplacez "your_secret_key" par votre clé secrète réelle


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
    flagagain = request.args.get('flagdejatrouvé') == 'true'
    return render_template('main.j2', flagpblm=flagpblm, flagagain=flagagain)
        

    return render_template('main.j2')
@app.route('/flag-post', methods= ['POST'])
def postflag():
    if request.method == 'POST':
        flag = request.form.get("flag")
        if flag in validated_flags:
            return redirect('/main?flagdejatrouvé=true')
        global score
        if flag == 'admin' :
            
            score +=5
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        #verif flag 1

        if flag == 'flag{Louis_le_hacker}' :
            
            score +=1
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        #verif flag 2
        if flag == 'admin':
            score+=5
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        if flag == 'flag{Weuve_le_malefique}' :
            score +=1
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        #verif flag 3
        if flag == 'flag{Ax€l_n0us_0b5erv€}' :
            score +=1
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        #verif flag 4
        if flag == 'flag{NSI_hacking_corp.}' :
            score +=1
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
            return redirect('/main')
        #verif flag 5
        if flag == 'flag{perigord_jumilhac-le-grand}' :
            score +=1
            validated_flags.append(flag)
            if score >= 5:
                return render_template('found_all_flags.j2')
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


@app.route('/epreuve4')
def page4():
    return render_template('epreuve4bis.j2')


@app.route('/epreuve5')
def page5():
    return render_template('epreuve5.j2')
@app.route('/contact')
def contact():
    return render_template('contact.j2')
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)