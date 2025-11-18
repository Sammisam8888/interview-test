from flask import current_app
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def init_db(app):
    """
    Initializes the MongoDB connection and attaches it to the app context.
    """
    try:
        mongo_uri = app.config['MONGO_URI']
        
        db_name = mongo_uri.split('/')[-1].split('?')[0]
        if not db_name:
            raise ValueError("Could not determine database name from MONGO_URI. Ensure it's in the format '.../db_name'")

        client = MongoClient(mongo_uri)
        client.admin.command('ping')
        
        # Store the database client (specific to our DB) on the app config
        app.config['MONGO_DB_CLIENT'] = client[db_name]
        
    except ConnectionFailure as e:
        print(f"MongoDB ConnectionFailure: {e}")
        raise e
    except Exception as e:
        print(f"An error occurred during DB initialization: {e}")
        raise e