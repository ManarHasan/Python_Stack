from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Manar"


@app.route('/')
def game():
    session['wins'] = 0
    session['losses'] = 0
    session['ties'] = 0
    return render_template("group.html", end="")


@app.route('/game', methods=['POST'])
def go():
    scen = {
        '1': {'2': 'lose', '3': 'win', '1': 'tie'},
        '2': {'2': 'tie', '3': 'lose', '1': 'win'},
        '3': {'2': 'win', '3': 'tie', '1': 'lose'}
    }
    session['computer'] = str(random.randint(1, 3))
    session['user'] = request.form['game']
    session['result'] = scen[session['user']][session['computer']]
    if session['result'] == 'win':
        session['wins'] += 1
    if session['result'] == 'lose':
        session['losses'] += 1
    if session['result'] == 'tie':
        session['ties'] += 1
    return redirect('/page2')


@app.route('/page2')
def page():
    return render_template("group.html", end=session['result'], user=session['user'], computer=session['computer'], wins=session['wins'], losses=session['losses'], ties=session['ties'])


if __name__ == "__main__":
    app.run(debug=True)
