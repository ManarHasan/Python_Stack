from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    petsDatabase = connectToMySQL("c+r")
    allPets = petsDatabase.query_db("SELECT * FROM pets;")
    return render_template("pets.html", allPets=allPets)


@app.route("/addPet", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    petsDatabase = connectToMySQL("c+r")

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        "name": request.form["name"],
        "type": request.form["type"]
    }
    petsDatabase.query_db(query, data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
