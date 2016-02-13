import os


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://vishnu:vishnu@localhost/test"
    SECRET_KEY = 'hard to guess string'