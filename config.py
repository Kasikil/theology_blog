import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-Psweet'
    # <DB TYPE>+<DB interface?>://<username>:<password>@<location>/<database>
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/theology_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
