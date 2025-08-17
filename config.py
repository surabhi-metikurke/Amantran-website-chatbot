class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Use a strong secret key
