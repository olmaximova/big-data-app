import os
from flask import Flask, redirect, request, send_from_directory
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, FRONTEND_DIR, ALLOWED_EXTENSIONS


app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return 

@app.route("/train")
def train_model():
    pass

@app.route("/analyze")
def analyze_data():
    pass

@app.route("/visuals")
def open_visuals():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7861, debug=True)