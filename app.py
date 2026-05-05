from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="danielspk",
    database="courier_db"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    tid = request.form['tracking_id']
    query = "SELECT * FROM courier WHERE tracking_id=%s"
    cursor.execute(query, (tid,))
    result = cursor.fetchone()
    return render_template('result.html', data=result)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add', methods=['POST'])
def add():
    tid = request.form['tracking_id']
    sender = request.form['sender']
    receiver = request.form['receiver']
    status = request.form['status']

    query = "INSERT INTO courier (tracking_id, sender, receiver, status) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (tid, sender, receiver, status))
    db.commit()

    return "Added Successfully"

app.run(debug=True)