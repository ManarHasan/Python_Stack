from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
@app.route("/")
def index():
    bookStore = connectToMySQL('books')
    bookData = bookStore.query_db('SELECT book_name, author_name FROM book;')
    print("--"*30)
    print(bookData)
    print("--"*30)
    return render_template("index.html", bookData = bookData)

@app.route("/addBook")
def add_book():
    return render_template("add_book.html")

@app.route("/display", methods=["POST"])
def display():
    bookStore = connectToMySQL('books')
    
    query = "INSERT INTO book (book_name, author_name) VALUE (%(bookName)s, %(authorName)s)"
    data = {
        "bookName":request.form['bookName'],
        "authorName":request.form['authorName']
    }
    inserted = bookStore.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
