Absolutely! Here’s the **ready-to-copy README** for your Node.js 15-min interview:

````markdown
# 📚 Library Mini API – Node.js 15-min Interview

## Setup
```bash
git clone <repo_url>
cd library-mini-api
npm install
npm start
````

Server will run at: `http://localhost:4000`

---

## **Task 1: GET /books**

**Objective:** Return a static list of books using the sample JSON below.

**Sample JSON to return:**

```json
[
  { "id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "available": true },
  { "id": 2, "title": "Atomic Habits", "author": "James Clear", "available": true }
]
```

**Instructions:**

* Implement `handleBooksRoute` in `src/routes/book.routes.js`.
* Respond with the JSON provided above.
* Set the header `Content-Type: application/json`.

**Expected output:**

```
GET /books
Authorization: Bearer <token>

Response:
[
  { "id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "available": true },
  { "id": 2, "title": "Atomic Habits", "author": "James Clear", "available": true }
]
```

---

## **Task 2: JWT Authentication Middleware**

**Objective:** Protect the `/books` route using a simple JWT check.

**Instructions:**

* Implement `authMiddleware` in `src/middleware/auth.middleware.js`.
* Check for `Authorization` header: `Bearer <token>`.
* If token is valid, allow request.
* If invalid or missing, respond with `401 Unauthorized`.

**Secret Key:**

```
interviewsecret
```

**Hint:**

```js
const jwt = require("jsonwebtoken");
jwt.verify(token, "interviewsecret")
```

---

## **Task 3: SQL Query (Theory)**

**Objective:** Write a SQL query (no need to code) to fetch all **available books** from a `books` table.

**Sample table schema:**

```sql
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  available BOOLEAN
);
```

**Expected answer example:**

```sql
SELECT * FROM books WHERE available = true;
```

---

## **Expected Flow**

1. Candidate writes code for `/books` route returning the sample JSON.
2. Protect `/books` using `authMiddleware`.
3. Explains/writes the SQL query for available books.

---

✅ **Key Points**

* Candidates **do not need to setup Express or DB**—everything is ultra-light.
* Focuses on **JSON handling, JWT, and SQL knowledge** in **15 minutes**.
* Can be tested via **Postman or curl**.

```