from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("playground.html", box="<div></div>", num=1, color="aquamarine")


@app.route('/play')
def index_play():
    return render_template("playground.html", box="<div></div>", num=3, color="aquamarine")


@app.route('/play/<int:num>')
def index_play_num(num):
    return render_template("playground.html", box="<div></div>", num=int(num), color="aquamarine")


@app.route('/play/<int:num>/<color>')
def index_play_num_color(num, color):
    return render_template("playground.html", box="<div></div>", num=int(num), color=color)


if __name__ == "__main__":
    app.run(debug=True)
