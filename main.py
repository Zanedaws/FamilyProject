import flask
import sqlite3
import hashlib
# import time


app = flask.Flask(__name__, static_folder="./static")


@app.route("/genUsers/awdsfh1235dsfidofaj12k35diaso2134214dsjkahfl!")
def genUsers_get():

    user = "Kara"
    pswd = "password"

    userHash = hashlib.sha256((user + pswd).encode('utf-8')).hexdigest()

    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", (user, pswd, userHash))

    user = "Patrick"
    pswd = "password"

    userHash = hashlib.sha256((user + pswd).encode('utf-8')).hexdigest()

    c.execute("INSERT INTO users VALUES (?,?,?)", (user, pswd, userHash))
    conn.commit()
    conn.close()
    return flask.redirect(flask.url_for("login_get"))


@app.route('/', methods=["GET"])
def home_get():
    return flask.redirect(flask.url_for("login_get"))


@app.route('/login', methods=["POST"])
def login_post():

    userName = flask.request.form['user']
    password = flask.request.form['pass']

    userHash = hashlib.sha256((userName + password).encode('utf-8')).hexdigest()

    conn = sqlite3.connect('data/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE userHash=?", (userHash,))
    user = c.fetchall()
    data = flask.jsonify({"data": user, "hash": userHash}, 204)
    return data


@app.route('/login', methods=["GET"])
def login_get():
    return flask.render_template("home.html")


@app.route("/feed/<userHash>", methods=["GET"])
def feed_get(userHash):
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM inputs")
    return flask.render_template("feed.html", data=[userHash])


@app.route("/profile/<userHash>", methods=["GET"])
def profile_get(userHash):
    conn = sqlite3.connect("data/database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM inputs WHERE userHash=?", (userHash,))
    inputs = c.fetchall()
    inputs.insert(0, userHash)
    return flask.render_template("profile.html", data=inputs)


@app.route("/input/<userHash>", methods=["GET"])
def input_get(userHash):
    return flask.render_template("input.html", data=[userHash])


@app.route("/input/<userHash>", methods=["POST"])
def input_post(userHash):

    # implement input creation in database

    return flask.redirect(flask.url_for("feed_get", userHash=userHash))


if __name__ == "__main__":
    app.run(port="5001", host="127.0.0.1", debug=True, use_evalex=False)
