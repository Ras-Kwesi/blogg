import os

class Config:
    '''
    Configuration of our app features
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/pitcher'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True



class ProdConfig(Config):
    '''
    Class that sets app to run of production mode
    '''
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    """
    Class this sets app to run on development mode
    """
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/blogg'

    DEBUG = True

class TestConfig(Config):
    '''
    Class that sets app to run on test mode
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kwesi:OnnenOfori14@localhost/blog'


config_options = {
'development':DevConfig,
    'test':TestConfig,
'production':ProdConfig}
