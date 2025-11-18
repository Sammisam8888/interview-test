SERVER_HOST="127.0.0.1"
SERVER_PORT="8000"
BASE_URL="http://$SERVER_HOST:$SERVER_PORT"
PID_FILE="django_server.pid"
TEST_SCRIPT="interview_scorer.py"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=================================================${NC}"
echo -e "${BLUE}    Django Backend Interview Evaluator    ${NC}"
echo -e "${BLUE}=================================================${NC}"

# 1. Check for Environment
if [ ! -f "manage.py" ]; then
    echo -e "${RED}Error: manage.py not found. Please run this script from the project root.${NC}"
    exit 1
fi

if [ ! -f ".env" ]; then
    echo -e "${RED}Error: .env file not found. Candidate has not completed Setup Task 1.${NC}"
    echo "Score: 0/100"
    exit 1
fi

# 2. Start the Server
echo -e "Starting Django server..."
python manage.py runserver $SERVER_HOST:$SERVER_PORT > /dev/null 2>&1 &
SERVER_PID=$!
echo $SERVER_PID > $PID_FILE

# Function to cleanup on exit
cleanup() {
    echo -e "\n${BLUE}Stopping server (PID: $SERVER_PID)...${NC}"
    kill $SERVER_PID 2>/dev/null
    rm -f $PID_FILE $TEST_SCRIPT
}
trap cleanup EXIT

# 3. Wait for Server to be ready
echo -n "Waiting for server to initialize..."
MAX_RETRIES=10
count=0
server_ready=false

while [ $count -lt $MAX_RETRIES ]; do
    if python -c "import socket; s = socket.socket(); s.connect(('$SERVER_HOST', int('$SERVER_PORT')))" 2>/dev/null; then
        server_ready=true
        break
    fi
    echo -n "."
    sleep 1
    count=$((count+1))
done
echo ""

if [ "$server_ready" = false ]; then
    echo -e "${RED}Server failed to start within 10 seconds.${NC}"
    echo -e "Check if the candidate has completed the database setup in settings.py."
    echo "Score: 0/100"
    exit 1
fi

echo -e "${GREEN}Server is up! Running tests...${NC}\n"

# 4. Create the Python Test Script
# We create this on the fly to avoid dependency issues (uses standard urllib)
cat << 'EOF' > $TEST_SCRIPT
import urllib.request
import urllib.error
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/tasks"
SCORE = 10 # 10 points for server starting

def print_result(name, success, points):
    global SCORE
    if success:
        SCORE += points
        print(f"[\033[92mPASS\033[0m] {name} (+{points} pts)")
    else:
        print(f"[\033[91mFAIL\033[0m] {name} (+0 pts)")

def run_tests():
    global SCORE
    
    # --- Test 1: Validation (Missing Description) ---
    try:
        req = urllib.request.Request(
            BASE_URL, 
            data=json.dumps({"wrong_key": "test"}).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            # Should verify it failed, but if it opens successfully (200/201), that's a fail for validation
            print_result("Validation: Rejects missing description", False, 20)
    except urllib.error.HTTPError as e:
        if e.code == 400:
            print_result("Validation: Rejects missing description", True, 20)
        else:
            print(f"      Expected 400, got {e.code}")
            print_result("Validation: Rejects missing description", False, 20)
    except Exception as e:
        print(f"      Connection error: {e}")
        print_result("Validation: Rejects missing description", False, 20)

    # --- Test 2: Create Task with Priority ---
    try:
        payload = {"description": "Test Task 1", "priority": "High"}
        req = urllib.request.Request(
            BASE_URL, 
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                data = json.loads(response.read().decode())
                if data.get("description") == "Test Task 1" and data.get("priority") == "High":
                    print_result("Functional: Creates task with Priority", True, 30)
                else:
                    print(f"      Response data mismatch: {data}")
                    print_result("Functional: Creates task with Priority", False, 30)
            else:
                print(f"      Expected 201, got {response.status}")
                print_result("Functional: Creates task with Priority", False, 30)
    except Exception as e:
        print(f"      Error: {e}")
        print_result("Functional: Creates task with Priority", False, 30)

    # --- Test 3: Default Logic (No Priority) ---
    try:
        payload = {"description": "Test Task 2"} # No priority sent
        req = urllib.request.Request(
            BASE_URL, 
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                data = json.loads(response.read().decode())
                if data.get("priority") == "Medium":
                    print_result("Logic: Defaults priority to 'Medium'", True, 20)
                else:
                    print(f"      Expected 'Medium', got '{data.get('priority')}'")
                    print_result("Logic: Defaults priority to 'Medium'", False, 20)
            else:
                print_result("Logic: Defaults priority to 'Medium'", False, 20)
    except Exception as e:
        print_result("Logic: Defaults priority to 'Medium'", False, 20)

    # --- Test 4: Data Formatting (_id and dates) ---
    # We use the data from the previous successful request if possible, or try a new one
    try:
        payload = {"description": "Formatting Test"}
        req = urllib.request.Request(
            BASE_URL, 
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            _id = data.get("_id")
            created_at = data.get("created_at")
            
            if isinstance(_id, str) and isinstance(created_at, str) and len(_id) > 0:
                print_result("Data: Handles ObjectId and Datetime serialization", True, 20)
            else:
                print(f"      Invalid types. _id type: {type(_id)}, created_at type: {type(created_at)}")
                print_result("Data: Handles ObjectId and Datetime serialization", False, 20)
    except Exception:
        print_result("Data: Handles ObjectId and Datetime serialization", False, 20)

    print("-" * 30)
    print(f"FINAL_SCORE={SCORE}")

if __name__ == "__main__":
    run_tests()
EOF

# 5. Execute Tests and Parse Output
python $TEST_SCRIPT > test_output.txt
cat test_output.txt

# Extract score
FINAL_SCORE=$(grep "FINAL_SCORE" test_output.txt | cut -d'=' -f2)
rm test_output.txt

echo -e "\n${BLUE}=================================================${NC}"
if [ "$FINAL_SCORE" -eq 100 ]; then
    echo -e "   ${GREEN}PERFECT SCORE: $FINAL_SCORE / 100${NC}"
elif [ "$FINAL_SCORE" -ge 70 ]; then
    echo -e "   ${GREEN}PASSING SCORE: $FINAL_SCORE / 100${NC}"
else
    echo -e "   ${RED}FAILING SCORE: $FINAL_SCORE / 100${NC}"
fi
echo -e "${BLUE}=================================================${NC}"