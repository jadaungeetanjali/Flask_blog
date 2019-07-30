import os


class Config:
    SECRET_KEY = '9b7dc40f250d437f9e3e11e80ca0cbc8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jadaungeetanjali24@gmail.com'
    MAIL_PASSWORD = 'geetanjali-24'