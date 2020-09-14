"""Classes used to configure FlaskApp and ConnexionApp"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Parent configuration class."""
    SECRET = 's3cr3t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_PATH = 'db/position_api.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, SQLALCHEMY_DATABASE_PATH)
    

class DevelopmentConfig(Config):
    """Configuration for Development."""
    DEBUG = True
    SQLALCHEMY_DATABASE_PATH = 'db/position_api_dev.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, SQLALCHEMY_DATABASE_PATH)
    

class TestingConfig(Config):
    """Configuration for Development."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_PATH = 'db/testing.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, SQLALCHEMY_DATABASE_PATH)


class ProductionConfig(Config):
    """Configuration for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'default': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
