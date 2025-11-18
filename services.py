from flask import current_app
from datetime import datetime
from pymongo.errors import PyMongoError

def create_task(description, priority):
    """
    Service function to handle the business logic of creating a new task.
    Now accepts a 'priority' argument.
    """
    
    # Get the MongoDB 'tasks' collection from the Flask app context
    try:
        db = current_app.config['MONGO_DB_CLIENT']
        tasks_collection = db.tasks
    except Exception as e:
        raise PyMongoError(f"Could not access database collection: {e}")

    # --- TODO: Candidate's Task (Approx. 7-8 minutes) ---
    # 1. Create a new task document (as a Python dictionary).
    #    The document should have:
    #    - "description": The description string.
    #    - "completed": A boolean, defaulting to False.
    #    - "created_at": The current UTC datetime (use datetime.utcnow()).
    #    - **NEW**: "priority": The priority string passed to this function.
    # 2. Insert the new task document into the `tasks_collection`.
    # 3. Get the result of the insertion (which includes the `inserted_id`).
    # 4. Find the newly created document in the database using the `inserted_id`.
    # 5. **Crucially**: Convert the `_id` (ObjectId) to a string.
    #    And convert `created_at` (datetime) to a string (`.isoformat()`)
    # 6. Return the complete new task dictionary.
    #
    #    Note: Let potential PyMongoError exceptions propagate up to the route handler.
    # --- End of TODO ---

    # --- START CANDIDATE CODE HERE ---

    # 1. Create the document
    task_document = {
        # ... candidate fills this in ...
    }

    # 2. Insert the document
    
    # 3. & 4. Find the new document
    
    # 5. & 6. Convert _id/datetime and return
    
    # This is a placeholder, the candidate should replace this
    return {"message": "Service not implemented"}

    # --- END CANDIDATE CODE HERE ---