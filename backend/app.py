from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend")

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/upload")
def upload():
    pass

@app.route("/train")
def train_model():
    pass

@app.route("/visuals")
def open_visuals():
    pass
