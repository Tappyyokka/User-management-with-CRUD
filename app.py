from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secure-secret-key"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn



def init_db():
    db = get_db()

    # Auth users
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # User management table
    db.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    db.commit()


@app.route('/')
def home():
    return redirect('/login')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            db.commit()
            return redirect('/login')
        except sqlite3.IntegrityError:
            return "⚠️ Username already exists!"

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            return redirect('/dashboard')
        else:
            return "❌ Invalid username or password"

    return render_template('login.html')



@app.route('/dashboard')
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect('/login')

    db = get_db()

    # Add user
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        db.execute(
            "INSERT INTO contacts (name, email) VALUES (?, ?)",
            (name, email)
        )
        db.commit()

    # Fetch users
    users = db.execute("SELECT * FROM contacts").fetchall()

    return render_template('dashboard.html', user=session['user'], users=users)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')



if __name__ == '__main__':
    init_db()
    app.run(debug=True)