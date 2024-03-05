from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route pour la page de connexion
@app.route('/', methods=['GET', 'POST'])
def con():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Axel' and password == 'start':
            return redirect('/main')
        else:
            return redirect('/')
    return render_template('connexion.j2')

# Route pour la page principale
@app.route('/main')
def index():
    return render_template('main.j2')

# Route pour la validation du flag
@app.route('/validate_flag')
def validate():
    return "hello world !"


# Routes pour les pages d'épreuves
@app.route('/epreuve1')
def page1():
    return render_template('epreuve1.j2')

@app.route('/epreuve2')
def page2():
    return render_template('epreuve2.j2')

@app.route('/epreuve3')
def page3():
    return render_template('epreuve3.j2')

@app.route('/epreuve4')
def page4():
    return render_template('epreuve4.j2')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
