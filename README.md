# 🕐 15-Minute Django Backend Challenge (with MongoDB)

Welcome!
This short coding exercise is designed to be completed in **15 minutes** and will test your familiarity with **Django**, **Python**, and **direct MongoDB interaction**.

Your goal:
Implement a single endpoint:

```
POST /api/tasks
```

This endpoint will create a new task and store it in MongoDB.

---

## ✅ What You Will Build

You will implement logic across **three primary areas**:

1. **Database Setup**
   Enable MongoDB connection in `django_mongo_interview/settings.py`.

2. **Schema Modification**
   Add a new field:

   ```
   priority: string
   ```

3. **Endpoint Logic**
   Implement POST `/api/tasks` using:

   - `tasks/views.py`
   - `tasks/services.py`

Look for `--- TODO ---` inside those files.

---

## 🚀 Setup Instructions (2–3 minutes)

### **1. Create Environment Variables (.env)**

The project includes `.env.example`.

1. Create a new `.env` file in the project root (same directory as `manage.py`).
2. Copy ALL contents from `.env.example` into `.env`.

> The default `MONGO_URI` works for a local MongoDB instance.

---

### **2. Enable MongoDB in Django Settings**

Open:

```
django_mongo_interview/settings.py
```

Do the following:

- **Uncomment** the line that calls:

  ```python
  load_dotenv(...)
  ```

- **Uncomment** the entire `try: ... except:` MongoDB initialization block that begins with:

  ```python
  try:
      MONGO_URI = ...
  ```

---

### **3. (Recommended) Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

---

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 💻 Your Task (10–12 minutes)

You will write code in:

- `tasks/views.py`
- `tasks/services.py`

---

# 📌 Part 1 — Implement `POST /api/tasks`

### File: `tasks/views.py`

Implement `add_new_task`.

#### Requirements:

### **Parsing**

- Parse JSON body from `request.body`.

### **Validation**

- Must contain `"description"`

  - must be a **non-empty string**

- Optional `"priority"`

### **Default Logic**

If `"priority"` is missing or empty:

```
priority = "Medium"
```

### **Database Logic**

Call:

```python
create_task(description, priority)
```

### **Response Rules**

| Case                        | Response                             |
| --------------------------- | ------------------------------------ |
| Success                     | JSON of created task, status **201** |
| Missing/invalid description | JSON error, status **400**           |
| Unexpected failure          | JSON error, status **500**           |

---

# 📌 Part 2 — Implement Database Write Logic

### File: `tasks/services.py`

Modify `create_task(description, priority)`.

### **Document Structure**

Create a dictionary like:

```python
{
    "description": description,
    "priority": priority,
    "completed": False,
    "created_at": datetime.utcnow(),
}
```

Insert into `tasks_collection`.

### **Return Value**

After inserting:

1. Retrieve the document you inserted.
2. Convert:

   - `_id` → `str(_id)`
   - `created_at` → `created_at.isoformat()`

3. Return the updated dictionary.

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Watch for:

```
MongoDB connection successful.
```

---

## 🧪 Testing Your Endpoint

### **Test 1 — With Priority**

```bash
curl -X POST http://127.0.0.1:8000/api/tasks \
     -H "Content-Type: application/json" \
     -d '{"description": "Finish the Django challenge", "priority": "High"}'
```

**Expected Response:**

```json
{
  "_id": "66a7b8e1f1c2d3a4b5e6f7a8",
  "completed": false,
  "created_at": "2024-07-29T12:45:21.345000",
  "description": "Finish the Django challenge",
  "priority": "High"
}
```

---

### **Test 2 — Without Priority**

```bash
curl -X POST http://127.0.0.1:8000/api/tasks \
     -H "Content-Type: application/json" \
     -d '{"description": "Test default priority"}'
```

**Expected Response:**

```json
{
  "_id": "66a7b8e2f1c2d3a4b5e6f7a9",
  "completed": false,
  "created_at": "2024-07-29T12:45:22.123000",
  "description": "Test default priority",
  "priority": "Medium"
}
```

---

## 