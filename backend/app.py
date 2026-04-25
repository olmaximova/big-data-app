from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend", static_url_path="" )

@app.route("/")
def index():
    return send_from_directory("../frontend", "index.html")

@app.route("/upload")
def upload():
    pass

@app.route("/train")
def train_model():
    pass

@app.route("/analyze")
def analyze_data():
    pass

@app.route("/visuals")
def open_visuals():
    pass
