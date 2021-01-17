from flask import Flask, render_template, request, redirect
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    friendsDatabase = connectToMySQL("users")
    friends = friendsDatabase.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("all_users.html", allFriends=friends)


@app.route("/addUser")
def addFriendPage():
    return render_template("add_user.html")


@app.route("/add", methods=["POST"])
def addFriendToDb():
    friendsDatabase = connectToMySQL("users")
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (%(firstName)s, %(lastName)s, %(email)s, NOW(), NOW());"
    data = {
        "firstName": request.form["fName"],
        "lastName": request.form["lName"],
        "email": request.form["email"]
    }
    friendsDatabase.query_db(query, data)
    return redirect("/profile/<i>")


if __name__ == "__main__":
    app.run(debug=True)
