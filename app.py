from flask import Flask, request, redirect, render_template

app = Flask(__name__)
messages = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form.get('message')
    if message:
        messages.append(message)
    return redirect('/')
