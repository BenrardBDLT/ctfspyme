from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

@app.route('/main')
def index():
    return render_template('main.j2')

@app.route('/epreuve1')
def page1():
    return render_template('epreuve1.j2')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

