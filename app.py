from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL credentials (use environment vars on Render)
conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
)

@app.route("/", methods=["GET", "POST"])
def index():
    cur = conn.cursor()
    if request.method == "POST":
        message = request.form["message"]
        cur.execute("INSERT INTO messages (text) VALUES (%s)", (message,))
        conn.commit()
    
    cur.execute("SELECT text FROM messages ORDER BY id DESC")
    rows = cur.fetchall()
    return render_template("index.html", messages=rows)
