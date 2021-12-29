from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('일부러비워뒀습니다')
db = client.dbsparta #dbsparta에 넣을게

import hashlib

@app.route('/register')
def showIndex():
    return render_template('join.html')

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

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)