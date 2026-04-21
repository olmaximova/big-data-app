import os

class Config:
    SECRET_KEY = 'big-data-secret'
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    PROCESSED_FOLDER = os.path.join('static', 'processed')
    PLOT_FOLDER = os.path.join('static', 'plots')
    SPARK_APP_NAME = 'ImageBigData'
    SPARK_MASTER = 'local[*]' 
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  
    
    @staticmethod
    def init_dirs():
        for folder in [Config.UPLOAD_FOLDER, Config.PROCESSED_FOLDER, Config.PLOT_FOLDER]:
            os.makedirs(folder, exist_ok=True)
