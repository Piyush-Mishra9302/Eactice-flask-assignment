
# Flask  Assignment (Starter)

A minimal Flask app.

## ✅ What’s included
- `/hello` → returns **"Hello World!"**
- `/users` → lists users from MySQL in an HTML table
- `/users/<id>` → shows a specific user's details
- `/new_user` → form to create a user (POST inserts into DB)
- Basic error handling for not found and DB errors
- Bootstrap styling (optional per assignment)
- SQL scripts for DB setup (Task 2)

---

## 1) Setup

### Prerequisites
- Python 3.x
- MySQL Server (running locally)

### Create & activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux (bash/zsh):**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## 2) Database (Task 2)
Use the provided SQL file:

```bash
# Replace root with your MySQL username
# You'll be prompted for your password
mysql -u root -p < sql/schema.sql
```

This will:
- Create database **users**
- Create table **users(id, name, email, role)**
- Insert sample data

> **SQL Queries (Task 2, point c):**
>
> - Insert sample data:
>   ```sql
>   INSERT INTO users (name, email, role) VALUES ('Alice Johnson','alice@example.com','Admin');
>   ```
> - Retrieve all users:
>   ```sql
>   SELECT id, name, email, role FROM users;
>   ```
> - Retrieve a specific user by ID:
>   ```sql
>   SELECT id, name, email, role FROM users WHERE id = 1;
>   ```

---

## 3) Configure DB credentials
Edit **config.py** or set environment variables. Defaults assume:
- host: `127.0.0.1`
- port: `3306`
- user: `root`
- password: *(empty)*
- database: `users`

You can also set env vars (example PowerShell):
```powershell
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="your_password"
$env:MYSQL_DATABASE="users"
$env:SECRET_KEY="change_me"
```

---

## 4) Run the app
```bash
python app.py
```
Open:
- http://127.0.0.1:5000/hello
- http://127.0.0.1:5000/users
- http://127.0.0.1:5000/new_user

---

## 5) Git Workflow (Task 3)
```bash
git init
git checkout -b assignment
git add .
git commit -m "Initial Flask app with MySQL and basic routes"

# Create a new repository on GitHub first, then:
git remote add origin <YOUR_REPO_URL>
git push -u origin assignment

# On GitHub, open a Pull Request from 'assignment' to 'main' (or 'master')
```

---

## 6) Notes
- Uses `mysql-connector-python` to avoid OS-specific build issues.
- Basic Bootstrap via CDN for quick styling.
- Error handling returns custom not-found page and 500 error page.
- Feel free to replace with Tailwind or custom CSS if desired.
