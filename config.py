from urllib.parse import quote
class Config:
    DEBUG = True
    MONGOALCHEMY_DATABASE = 'tdb'
    MONGOALCHEMY_SERVER_AUTH = True
    MONGOALCHEMY_SERVER = '192.168.99.1'
    MONGOALCHEMY_PORT = 27017
    MONGOALCHEMY_USER = 'testUser'
    MONGOALCHEMY_PASSWORD = quote('')


