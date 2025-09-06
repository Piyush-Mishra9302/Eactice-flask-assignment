
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from mysql.connector import Error
from db import get_db_connection

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/users')
def list_users():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, role FROM users ORDER BY id DESC")
        rows = cursor.fetchall()
        return render_template('users.html', users=rows)
    except Error as e:
        app.logger.exception(e)
        abort(500, description="Database error")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, role FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        if not row:
            # Specific not-found page
            return render_template('not_found.html', message=f"User with id {user_id} was not found."), 404
        return render_template('user_detail.html', user=row)
    except Error as e:
        app.logger.exception(e)
        abort(500, description="Database error")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        role = request.form.get('role', '').strip()

        if not name or not email or not role:
            flash('All fields are required.', 'danger')
            return render_template('new_user.html', form={'name': name, 'email': email, 'role': role}), 400

        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                (name, email, role)
            )
            conn.commit()
            flash('User created successfully!', 'success')
            return redirect(url_for('list_users'))
        except Error as e:
            # Handle duplicate email (errno 1062) or other DB errors
            if conn: conn.rollback()
            try:
                errno = getattr(e, 'errno', None)
            except Exception:
                errno = None
            if errno == 1062:
                flash('Email already exists. Please use a different email.', 'warning')
                return render_template('new_user.html', form={'name': name, 'email': email, 'role': role}), 400
            raise
        except Error as e:
            if conn: conn.rollback()
            app.logger.exception(e)
            abort(500, description="Database error")
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
    # GET
    return render_template('new_user.html')

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html', message=str(e)), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('not_found.html', message=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
