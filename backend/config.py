import os

UPLOAD_FOLDER = 'static/files'
ALLOWED_EXTENSIONS = {'csv'}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")