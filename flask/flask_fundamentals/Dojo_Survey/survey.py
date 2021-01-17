from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Manar"


@app.route('/')
def form():
    return render_template("survey.html")


@app.route('/result', methods=['POST'])
def submit():
    username = request.form["username"]
    location = request.form["loc"]
    favorite = request.form["fav"]
    comment = request.form["comment"]
    NnT = request.form.getlist("NnT")
    if NnT == ['NnT']:
        NnT = 'Yes'
    else:
        NnT = 'No'
    BnH = request.form.getlist("BnH")
    if BnH == ['BnH']:
        BnH = 'Yes'
    else:
        BnH = 'No'
    Naruto = request.form.getlist("Naruto")
    if Naruto == ['Naruto']:
        Naruto = 'Yes'
    else:
        Naruto = 'No'
    yes = request.form.getlist("yes")
    if yes == ['on']:
        yes = 'Yes'
    else:
        yes = 'No'
    return render_template('survey1.html', username=username, location=location, favorite=favorite, NnT=NnT, BnH=BnH, Naruto=Naruto, yes=yes, comment=comment)


if __name__ == "__main__":
    app.run(debug=True)
