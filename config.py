import os


class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_USER = os.environ.get('POSTGRES_USER')
    SQLALCHEMY_DATABASE_NAME = os.environ.get('POSTGRES_NAME')
    SQLALCHEMY_DATABASE_PASS = os.environ.get('POSTGRES_PASS')
    SQLALCHEMY_DATABASE_HOST = os.environ.get('POSTGRES_HOST')
    SQLALCHEMY_DATABASE_PORT = os.environ.get('POSTGRES_PORT')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
            SQLALCHEMY_DATABASE_USER,
            SQLALCHEMY_DATABASE_PASS,
            SQLALCHEMY_DATABASE_HOST,
            SQLALCHEMY_DATABASE_PORT,
            SQLALCHEMY_DATABASE_NAME
        )


config = {
    'dev': DevConfig
}
