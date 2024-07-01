import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Mail configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'magicwebsite03@gmail.com'  # Hardcoded email
    MAIL_PASSWORD = 'zfpuorxboplmcive'  # Hardcoded app password
    MAIL_DEFAULT_SENDER = 'magicwebsite03@gmail.com'  # Hardcoded default sender

    print("MAIL_USERNAME:", MAIL_USERNAME)
    print("MAIL_PASSWORD:", MAIL_PASSWORD)
    print("MAIL_DEFAULT_SENDER:", MAIL_DEFAULT_SENDER)
