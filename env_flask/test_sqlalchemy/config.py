class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    ENV = "development"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"


