class Config:
    SECRET_KEY = 'B!1234567dasdCAS*S'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
