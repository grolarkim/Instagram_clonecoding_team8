from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbinsta

app = Flask(__name__)

@app.route('/')
def showIndexPage():
    return render_template('index.html')

@app.route('/profile')
def showProfilePage():
    return render_template('main.html')

@app.route('/login')
def showLoginPage():
    return render_template('login.html')

@app.route('/register')
def showRegisterPage():
    return render_template('join.html')

@app.route('/posting')
def showPostingPage():
    return render_template('posting.html')

@app.route('/api/timeline')
def showTimeLine():
    return 

@app.route('/api/my_post')
def showMyPost():
    return 

@app.route('/api/login')
def Login():
    return 

@app.route('/api/register')
def Register():
    return 

@app.route('/api/posting')
def Posting():
    return 






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)