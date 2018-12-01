"""config file"""

#pylint: disable=too-few-public-methods
class Config(object):
    """
    Common configurations
    """
    DEBUG = False
    CSRF_ENABLED = True

class TestingConfig(Config):
    """
    The configuration for testing
    """
    DEBUG = True
    TESTING = True

#pylint: disable=too-few-public-methods
class DevelopmentConfig(Config):
    """
    Development configurations
    """
    TESTING = True
    DEBUG = True

#pylint: disable=too-few-public-methods
class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

class StagingConfig(Config):
    """
    The configuration for staging
    """
    DEBUG = True

APP_CONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'staging': StagingConfig
}
