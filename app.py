from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def showIndex():
    return render_template('index.html')

@app.route('/profile')
def showProfile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)