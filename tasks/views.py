from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from pymongo.errors import PyMongoError
from .services import create_task
import json
import logging

@csrf_exempt
@require_http_methods(["POST"])
def add_new_task(request: HttpRequest) -> JsonResponse:
    """
    
    # --- TODO: Candidate's Task (Approx. 7-8 minutes) ---
    # 1. Parse the JSON data from the request body.
    #    Hint: `data = json.loads(request.body)`
    # 2. Validate the data:
    #    - Check if 'description' exists and is a non-empty string.
    #    - If validation fails, return a JsonResponse with a 400 status.
    #      Example: `return JsonResponse({"error": "..."}, status=400)`
    # 3. **NEW**: Check for an *optional* 'priority' field.
    #    - If it's not provided or is empty, set a default value of "Medium".
    # 4. If validation is successful, call the `create_task` function 
    #    from the `services` module, passing BOTH the description and priority.
    # 5. Handle any potential PyMongoError that the service layer might raise.
    #    - If an error occurs, return a JsonResponse with a 500 status.
    # 6. If successful, return the newly created task (as a dictionary) 
    #    in a JsonResponse with a 201 Created status code.
    #    Example: `return JsonResponse(new_task, status=201)`
    # --- End of TODO ---
    """
    
    try:
        # --- START CANDIDATE CODE HERE ---
        
        # 1. Parse JSON (Hint: use try/except for json.JSONDecodeError)
        
        # 2. Validate description
        
        # 3. Handle priority (with default)
        
        # 4. Call service layer
        
        # 6. Return success response
        
        
        # --- END CANDIDATE CODE HERE ---
        
        # This is a placeholder, the candidate should replace this
        return JsonResponse({"message": "Endpoint not implemented"}, status=501)


    except PyMongoError as e:
        # 5. Handle database errors
        logging.error(f"Database error on task creation: {e}")
        return JsonResponse({"error": "A database error occurred."}, status=500)
    except Exception as e:
        # Handle other unexpected errors
        logging.error(f"Unexpected error on task creation: {e}")
        return JsonResponse({"error": "An internal server error occurred."}, status=500)