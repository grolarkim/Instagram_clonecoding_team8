from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def showIndexPage():
    return render_template('index.html')

@app.route('/profile')
def showProfilePage():
    return render_template('profile.html')

@app.route('/login')
def showLoginPage():
    return render_template('login.html')

@app.route('/register')
def showRegisterPage():
    return render_template('register.html')

@app.route('/posting')
def showPostingPage():
    return render_template('posting.html')






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)