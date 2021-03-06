DEBUG = True
LOGGING_CONFIG = "config/logging/local.conf"
PORT = 5000
APP_NAME = "penny-lane"
SQLALCHEMY_DATABASE_URI = 'sqlite:///data/tracks.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False  # If true, SQL for queries made will be printed
MAX_ROWS_SHOW = 100