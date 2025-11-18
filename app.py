import os
from flask import Flask
from dotenv import load_dotenv
from config import Config
from models import init_db
from routes import tasks_bp

def create_app():
    """Application factory to create and configure the Flask app."""
    
    # --- TODO: Candidate Setup Task 1 ---
    # 1. Uncomment the following line to load environment variables from .env
    # load_dotenv()
    # --- End of TODO ---

    app = Flask(__name__)
    app.config.from_object(Config)

    # --- TODO: Candidate Setup Task 2 ---
    # 1. Uncomment the entire `try...except` block below
    #    to initialize the MongoDB connection.
    # --- End of TODO ---
    # try:
    #     init_db(app)
    #     print("MongoDB connection successful.")
    # except Exception as e:
    #     print(f"Error connecting to MongoDB: {e}")
    # --- End of TODO ---

    # Register the blueprint for our routes
    app.register_blueprint(tasks_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return "Interview API is running. Please use the /api/tasks endpoint.", 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)