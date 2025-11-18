# 🕐 15-Minute Flask Backend Challenge (with MongoDB)

Welcome!
This short coding exercise is designed to be completed in **15 minutes** and will test your knowledge of **Flask**, **Python**, and **direct MongoDB interaction**.

Your task is to implement a single endpoint:

```
POST /api/tasks
```

This endpoint will create a new task in a MongoDB database.

---

## ✅ What You Will Build

You will modify logic in **three files**:

1. **app.py** — enable database connection
2. **routes.py** — implement endpoint logic
3. **services.py** — database operations

Look for **`--- TODO ---`** comments to know where to write code.

---

## 🚀 Setup Instructions (2–3 minutes)

### **1. Environment Variables (.env)**

This project includes a `.env.example` file.

1. Create a new file named `.env` in the project root (same directory as `app.py`).
2. Copy the contents of `.env.example` into your `.env`.

> The default `MONGO_URI` works with a local MongoDB server.

---

### **2. Enable MongoDB Connection**

Open:

```
app.py
```

Then:

* **Uncomment** the `load_dotenv()` call.
* **Uncomment** the entire `try: ... except:` block beginning with:

  ```python
  try:
      init_db(app)
  ```

This initializes the MongoDB client.

---

### **3. (Recommended) Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

---

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

# 💻 Your Task (10–12 minutes)

You will complete logic in:

* `routes.py`
* `services.py`

---

## 📌 Part 1 — Implement `POST /api/tasks`

### File: `routes.py`

Implement the `add_new_task` function.

### **Parsing**

Use:

```python
data = request.get_json()
```

### **Validation**

Requirements:

* Must contain `"description"`
  → must be a non-empty string
* `"priority"` is optional

### **Default Priority Value**

If priority is missing or empty:

```
priority = "Medium"
```

### **Database Call**

Use:

```python
create_task(description, priority)
```

### **Response Rules**

| Case                | Response                         |
| ------------------- | -------------------------------- |
| Success             | `jsonify(task)`, status **201**  |
| Invalid description | `jsonify(error)`, status **400** |
| Unexpected error    | `jsonify(error)`, status **500** |

---

## 📌 Part 2 — Implement Database Logic

### File: `services.py`

Modify `create_task(description, priority)`.

### **Create a document:**

```python
{
    "description": description,
    "priority": priority,
    "completed": False,
    "created_at": datetime.utcnow()
}
```

Insert into MongoDB:

```python
tasks_collection.insert_one(document)
```

### **Return the inserted document**

1. Retrieve it using the inserted ID.
2. Convert:

   * `_id` → `str(_id)`
   * `created_at` → `.isoformat()`

Return the final dictionary.

---

## ▶️ Run the Flask App

```bash
python app.py
```

You should see:

```
MongoDB connection successful.
```

---

## 🧪 Testing the Endpoint

URL:

```
http://127.0.0.1:5000/api/tasks
```

---

### **Test 1 — With Priority**

```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
     -H "Content-Type: application/json" \
     -d '{"description": "Finish the Flask challenge", "priority": "High"}'
```

**Expected Response**

```json
{
  "_id": "66a7b8e1f1c2d3a4b5e6f7a8",
  "completed": false,
  "created_at": "2024-07-29T12:45:21.345000",
  "description": "Finish the Flask challenge",
  "priority": "High"
}
```

---

### **Test 2 — Without Priority (Default Value)**

```bash
curl -X POST http://127.0.0.1:5000/api/tasks \
     -H "Content-Type: application/json" \
     -d '{"description": "Test default priority"}'
```

**Expected Response**

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

## 🎉 You're Done!

