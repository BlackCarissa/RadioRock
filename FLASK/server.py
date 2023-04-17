from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/sign_up')
def sign_up():
    return render_template('frame1.html')
if __name__=='__main__':
    app.run(debug=True)