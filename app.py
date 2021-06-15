from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('3.35.210.207', 27017, username="test", password="test")
db = client.dbsparta_plus_week3


@app.route('/')
def main():
    return render_template("index.html")

@app.route("/matjip", methods=["GET"])
# GET 방식으로 요청이 왔을 때 맛집 리스트를 돌려주면 된다는게 이 api의 역할
def get_matjip():
    #1. 데이터베이스에서 맛집 목록을 꺼내와야 한다.
    matjip_list = list(db.matjips.find({},{'_id': False}))
    #2. 그걸 클라이언트에게 돌려준다
    return jsonify({'result': 'success', 'matjip_list': matjip_list})
    #3. 서버 작성 완료. 이렇게 api를 만들었으면 클라이언트 단에서 가져와야 함 (html 파일로 가기)

@app.route('/like_matjip', methods=['POST'])
def like_matjip():
    title_receive = request.form["title_give"]
    address_receive = request.form["address_give"]
    action_receive = request.form["action_give"]
    print (title_receive, address_receive, action_receive)

    if action_receive == "like":
        db.matjips.update_one({"title": title_receive, "address": address_receive}, {"$set": {"liked": True}})
    else:
        db.matjips.update_one({"title": title_receive, "address": address_receive}, {"$unset": {"liked": False}})

    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

