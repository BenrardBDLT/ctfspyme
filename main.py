from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('truc.j2')
@app.route('/epreuve1')
def page1():
    return render_template('epreuve1.j2')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 