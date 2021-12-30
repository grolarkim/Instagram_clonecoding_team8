from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import hashlib #pw해시함수화 위해 임포트
import datetime #로그인 유지를 위해 필요하니 임포트
import jwt #얘를 임포트하기위해 인터프리터에 PyJwt패키지 설치!

SECRET_KEY = 'SPARTA'


@app.route('/')
def showIndexPage():
    token_receive = request.cookies.get('mytoken')
    try:
	    # 암호화되어있는 token의 값을 우리가 사용할 수 있도록 디코딩(암호화 풀기)해줍니다!
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})
        return render_template('index.html', user_id=user_info["id"])
		# 만약 해당 token의 로그인 시간이 만료되었다면, 아래와 같은 코드를 실행합니다.
    except jwt.ExpiredSignatureError:
        return redirect(url_for("showLoginPage", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
		# 만약 해당 token이 올바르게 디코딩되지 않는다면, 아래와 같은 코드를 실행합니다.
        return redirect(url_for("showLoginPage", msg="로그인 정보가 존재하지 않습니다."))
    

@app.route('/profile')
def showProfilePage():
    token_receive = request.cookies.get('mytoken')
    try:
	    # 암호화되어있는 token의 값을 우리가 사용할 수 있도록 디코딩(암호화 풀기)해줍니다!
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})
        return render_template('main.html', user_id=user_info["id"])
		# 만약 해당 token의 로그인 시간이 만료되었다면, 아래와 같은 코드를 실행합니다.
    except jwt.ExpiredSignatureError:
        return redirect(url_for("showLoginPage", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
		# 만약 해당 token이 올바르게 디코딩되지 않는다면, 아래와 같은 코드를 실행합니다.
        return redirect(url_for("showLoginPage", msg="로그인 정보가 존재하지 않습니다."))
    



@app.route('/login')
def showLoginPage():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)

@app.route('/register')
def showRegisterPage():
    return render_template('join.html')

@app.route('/posting')
def showPostingPage():
    token_receive = request.cookies.get('mytoken')
    try:
	    # 암호화되어있는 token의 값을 우리가 사용할 수 있도록 디코딩(암호화 풀기)해줍니다!
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.register.find_one({"id": payload['id']})
        return render_template('posting.html', user_id=user_info["id"])
		# 만약 해당 token의 로그인 시간이 만료되었다면, 아래와 같은 코드를 실행합니다.
    except jwt.ExpiredSignatureError:
        return redirect(url_for("showLoginPage", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
		# 만약 해당 token이 올바르게 디코딩되지 않는다면, 아래와 같은 코드를 실행합니다.
        return redirect(url_for("showLoginPage", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/api/timeline')
def showTimeLine():
    return

@app.route('/api/my_post')
def showMyPost():
    return

@app.route('/api/login', methods=['POST'])
def Login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
    result = db.register.find_one({'id': id_receive, 'pw': pw_hash})

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=암호화 풀기)해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

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

@app.route('/api/posting', methods=['POST'])
def Posting():
    id_receive = request.form['id_give']
    url_receive = request.form['url_give']
    desc_receive = request.form['desc_give']
    doc = {
        'id': id_receive,
        'url': url_receive,
        'desc': desc_receive
    }
    db.post.insert_one(doc)
    return jsonify({'msg': '게시물 생성 완료!'}) 

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)