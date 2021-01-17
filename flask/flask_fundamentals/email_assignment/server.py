from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = "Thunderbirds"


@app.route('/success')
def success():
    emailData = connectToMySQL("email")
    flash(
        f"The email you have entered {session['email']} is a VALID email address! Thank you!")
    emails = emailData.query_db("SELECT email, created_at FROM user;")
    return render_template("success.html", allEmails=emails)


@app.route("/")
def addEmail():
    return render_template("index.html")


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/add", methods=["POST"])
def addEmailToDatabase():
    emailData = connectToMySQL("email")
    query = "INSERT INTO user (email) VALUES (%(email)s);"
    data = {
        "email": request.form["email"]
    }
    emailExists = True
    if emailExists == True:
        print("8"*80)
        emails = emailData.query_db("SELECT email, created_at FROM user;")
        for i in range(len(emails)):
            print("8"*80)
            if request.form['email'] == emails[i]['email']:
                print("8"*80)
                flash("Email already exists!")
                emailExists = False
                return render_template("index.html")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address!")
        return redirect("/")
    session['email'] = request.form['email']
    emailData.query_db(query, data)
    return redirect("/success")


if __name__ == "__main__":
    app.run(debug=True)
