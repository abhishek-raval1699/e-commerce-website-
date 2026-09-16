from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hellow():
    return render_template('index.html')