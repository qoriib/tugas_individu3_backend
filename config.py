import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/product_reviews')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'xh3aTAJJejHswX638h7R'
