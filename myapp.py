from flask import Flask

app= Flask(__name__)

@app.route("/info")
def lwinfo():
        return"i m lw from india"

@app.route("/phone")
def lwphone():
        return"7016722814"

app.run(host="0.0.0.0")