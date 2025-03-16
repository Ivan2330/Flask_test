---


# 🚀 Flask User API

A **Flask-based REST API** for managing users with CRUD operations.  
Built with **Flask, FastAPI, SQLAlchemy, and Docker**.

---

## 🛠️ Tech Stack

- **🐍 Python & Flask** - Backend framework
- **🐘 PostgreSQL** - Database
- **🐳 Docker & Docker Compose** - Containerization
- **🧪 Pytest** - Automated testing
- **📜 Swagger UI** - API documentation

---

## 📂 Project Structure

```
Flask_test/
│-- app/
│   ├── models.py         # Database models
│   ├── routes.py         # API endpoints
    ├── schemas/          # Pydantic schemas for validation
│-- static/               # Swagger documentation files
│-- tests/                # Test cases for API
│-- Dockerfile            # Docker setup for the app
│-- docker-compose.yml    # Docker Compose configuration
│-- .gitignore            # Files ignored by Git
│-- requirements.txt      # Dependencies
│-- main.py               # Application entry point
│-- README.md             # Project documentation (this file)
```

---

## 🏗️ How to Run the Project (Docker Only)

### 1️⃣ **Navigate to the Project Directory**
```sh
cd Flask_test
```

### 2️⃣ **Build and Start the Containers**
```sh
docker-compose up --build
```

✅ **Tests will run automatically on startup!**  
📌 Screenshot of Tests Running:  
![image](https://github.com/user-attachments/assets/17bdf5f9-3f00-4614-b4fe-dcd8602dbabc)


---

## 🔗 Access API Documentation

After starting the project, open:  
📌 **[Swagger UI](http://localhost:5000/api/docs/)**

📌 **Example Screenshot of Swagger UI:**  
![image](https://github.com/user-attachments/assets/56232fd1-45d4-4a41-af79-1f0d073eb7ed)


---

## 📖 API Documentation

### 🔹 User Endpoints
| Method  | Endpoint         | Description                    |
|---------|-----------------|--------------------------------|
| **GET**    | `/users`       | Retrieve all users          |
| **POST**   | `/users`       | Create a new user           |
| **GET**    | `/users/{id}`  | Retrieve a user by ID       |
| **PUT**    | `/users/{id}`  | Update user details         |
| **DELETE** | `/users/{id}`  | Delete a user               |

### 📜 Example Request (Create User)
```json
POST /users
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### ✅ Example Response
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-03-16T00:05:04.118236"
}
```

---

## 📜 License

This project is licensed under the **MIT License**.

---
