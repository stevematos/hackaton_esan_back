"""
 Configuracion de los objectos de flask
"""

POSTGRES_DEVELOPMENT = {
        'user': 'hackaton',
        'pw': 'hackaton',
        'db': 'hackaton',
        'host': 'localhost',
        'port': '5432'
}

POSTGRES_PRODUCTION = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'hackaton',
        'host': '34.95.237.199',
        'port': '5432'
}
#
# POSTGRES_DATAMART_PRODUCTION = {
#         'user': 'datamart',
#         'pw': 'datamart',
#         'db': 'datamart',
#         'host': '34.95.237.199',
#         'port': '5432'
# }

class Config(object):   
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class __DevelopmentConfig__(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES_DEVELOPMENT

# class __DatamartTestingConfig__(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES_DATAMART_TESTING

class __ProductionConfig__(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES_PRODUCTION


DATABASES_CONFIG = {
    'production_config': __ProductionConfig__,
    # 'datamart_testing': __DatamartTestingConfig__,
    'development_config': __DevelopmentConfig__
}


# class TestingConfig(TestingDBConfig):
#     DEBUG = False

# class TestingConfig(Config):
#     TESTING = True