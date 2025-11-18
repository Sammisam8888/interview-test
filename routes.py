from flask import Blueprint, request, jsonify
from services import create_task
from pymongo.errors import PyMongoError
import logging

tasks_bp = Blueprint('tasks_bp', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def add_new_task():
    """
    API endpoint to create a new task.
    
    # --- TODO: Candidate's Task (Approx. 7-8 minutes) ---
    # 1. Get the JSON data from the incoming request.
    #    Hint: `data = request.get_json()`
    # 2. Validate the data:
    #    - Check if it's valid JSON (Flask handles this, but check if `data` is None).
    #    - Check if 'description' exists and is a non-empty string.
    #    - If validation fails, return a 400 Bad Request error.
    #      Example: `return jsonify({"error": "..."}), 400`
    # 3. **NEW**: Check for an *optional* 'priority' field.
    #    - If it's not provided or is empty, set a default value of "Medium".
    # 4. If validation is successful, call the `create_task` function 
    #    from the `services` module, passing BOTH the description and priority.
    # 5. Handle any potential PyMongoError that the service layer might raise.
    #    - If an error occurs, return a 500 Internal Server Error.
    # 6. If successful, return the newly created task (as a dictionary) 
    #    with a 201 Created status code.
    #    Example: `return jsonify(new_task), 201`
    # --- End of TODO ---
    """
    
    try:
        # --- START CANDIDATE CODE HERE ---
        
        # 1. Get JSON data
        
        # 2. Validate description
        
        # 3. Handle priority (with default)
        
        # 4. Call service layer
        
        # 6. Return success response
        
        
        # --- END CANDIDATE CODE HERE ---
        
        # This is a placeholder, the candidate should replace this
        return jsonify({"message": "Endpoint not implemented"}), 501

    except PyMongoError as e:
        # 5. Handle database errors
        logging.error(f"Database error on task creation: {e}")
        return jsonify({"error": "A database error occurred."}), 500
    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"Unexpected error on task creation: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500