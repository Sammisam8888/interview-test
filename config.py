import os

class Config:
    """
    Flask configuration object.
    Loads configuration from environment variables.
    """
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/interview_db")