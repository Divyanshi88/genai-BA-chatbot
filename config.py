import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "instance", "business_strategy.db")}'

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "instance", "business_strategy.db")}')

class TestingConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
