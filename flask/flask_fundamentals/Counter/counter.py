from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Manar"


@app.route('/')
def coutner():
    return render_template("counter.html", counter=session['counter'])


@app.route('/cool', methods=['POST'])
def counter():
    session['counter'] = 0
    x = request.form['submit_button']
    if x == '1':
        session['counter'] += 1
    if x == '1':
        session['counter'] = 0
    # if 'counter' in session:
    #     print('key exists!')
    # else:
    #     print("key 'counter' does NOT exist")
    return redirect('/')


@app.route('/destroy_session')
def clear():
    session.clear()
    return render_template("coutner.html")


if __name__ == "__main__":
    app.run(debug=True)
