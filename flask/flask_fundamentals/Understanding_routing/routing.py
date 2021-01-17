from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/<word>')
def word(word):
    return "Hi " + word


@app.route('/<int:num>/<word>')
def num_word(num, word):
    x = ""
    for i in range(int(num)):
        x += word + " "
    return x


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again!"


if __name__ == "__main__":
    app.run(debug=True)
