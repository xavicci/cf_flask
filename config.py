from decouple import config

class Config:
    SECRET_KEY = 'B1E$"#Esad#$S'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'tienda'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587 #TLS Transport Layer Security
    MAIL_USE_TLS=True
    MAIL_USERNAME='xavier.flores.gis2@gmail.com'
    MAIL_PASSWORD=config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
