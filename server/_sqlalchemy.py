from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, inspect, create_engine


DB_URI = '{db_type}://{user}:{password}@{host}:{port}/{db_name}'
