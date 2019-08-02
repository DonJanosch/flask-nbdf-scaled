import os

# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_the_unsecure_backup_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplage_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = postgres_local_base

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplage_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = postgres_local_base

def config_by_name(config_name):
    config_dict = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
    )
    return config_dict.get(config_name,DevelopmentConfig)

key = Config.SECRET_KEY
