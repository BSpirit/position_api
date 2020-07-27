"""Classes used to configure FlaskApp and ConnexionApp"""

import os
from connexion.problem import problem
from connexion import decorators
from jsonschema import ValidationError

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Parent configuration class."""
    SECRET = 's3cr3t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

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
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}


class RequestBodyValidator(decorators.validation.RequestBodyValidator):
    """
    This class overrides the default connexion RequestBodyValidator
    so that it returns the complete string representation of the
    error, rather than just returning the error message.

    For more information:
        - https://github.com/zalando/connexion/issues/558
        - https://connexion.readthedocs.io/en/latest/request.html
    """
    def validate_schema(self, data, url):
        if self.is_null_value_valid and is_null(data):
            return None

        try:
            self.validator.validate(data)
        except ValidationError as exception:
            return problem(400, "Bad Request", str(exception))

        return None
