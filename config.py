class Config:
    SECRET_KEY = 'B!1234567dasdCAS*S'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'tienda'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
