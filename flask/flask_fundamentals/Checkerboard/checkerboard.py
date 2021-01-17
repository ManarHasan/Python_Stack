from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("checker.html", color1="black", color2="red", rows=5, checks=5, open="<tr>", checkbox1="<td class='one'></td>", checkbox2="<td class='two'></td>", close="</tr>")


@app.route('/checkers/<rows>')
def checkers_rows(rows, checks):
    return render_template("checker.html", color1="black", color2="red", rows=int(rows), checks=5, open="<tr>", checkbox1="<td class='one'></td>", checkbox2="<td class='two'></td>", close="</tr>")


@app.route('/checkers/<rows>/<checks>')
def checkers_rows_checks(rows, checks):
    return render_template("checker.html", color1="black", color2="red", rows=int(rows), checks=int(checks), open="<tr>", checkbox1="<td class='one'></td>", checkbox2="<td class='two'></td>", close="</tr>")


@app.route('/checkers/<rows>/<checks>/<color1>/<color2>')
def checkers(rows, checks, color1, color2):
    return render_template("checker.html", color1=color1, color2=color2, rows=int(rows), checks=int(checks), open="<tr>", checkbox1="<td class='one'></td>", checkbox2="<td class='two'></td>", close="</tr>")


if __name__ == "__main__":
    app.run(debug=True)
