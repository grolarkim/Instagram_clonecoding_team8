from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import hashlib #pw해시함수화 위해 임포트
from datetime import datetime,timedelta #로그인 유지를 위해 필요하니 임포트
import jwt #얘를 임포트하기위해 인터프리터에 PyJwt패키지 설치!

SECRET_KEY = 'sparta'

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

@app.route('/api/login')#로그인
def Login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    #받아온 패스워드를 해시함수화하기
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()
    #DB에서 post로 받아온 id와, pw에 맞는값 불러와서 result에 저장
    result = db.register.find_one({'id': id_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60)  # 로그인 1분 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result':'fail', 'msg' : '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    url_receive = request.form['url_give']
    name_receive = request.form['name_give']
    desc_receive = request.form['desc_give']
    # 저장하기 전 pw를 sha256 방법으로 암호화해서 저장
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'id': id_receive,
        'pw': pw_hash,
        'url': url_receive,
        'name': name_receive,
        'desc': desc_receive
    }
    db.register.insert_one(doc)
    return jsonify({'msg': '가입완료'})

@app.route('/api/posting')
def Posting():
    return

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)