
class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    RESTPLUS_MASK_SWAGGER=False

MONGODB_SETTINGS = {
        'db': 'local',
        'host': 'localhost',
        'port': 27017
}
    
