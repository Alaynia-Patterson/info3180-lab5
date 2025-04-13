# Add any model classes for Flask-SQLAlchemy here
from app import db
from datetime import datetime

# Define the Movie model
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each movie
    title = db.Column(db.String(100), nullable=False)  # Title of the movie
    description = db.Column(db.Text, nullable=False)  # Summary or description
    poster = db.Column(db.String(255), nullable=False)  # Filename of the uploaded poster
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when added
