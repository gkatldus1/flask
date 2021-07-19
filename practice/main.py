from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from model.user_model import UserModel  
from flask import Flask, request, jsonify, Response
engine = create_engine("sqlite:///main.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# user = UserModel("username", "1234", "jason", "bob@")
# session.add(user)

# session.commit()
# select user by name
# jason = session.query(UserModel).filter(UserModel.name =='jason').one_or_none()
# jason = session.query(UserModel).filter(UserModel.name =='bob').all()

# print(selected_users)
# print(selected_user.user_id,selected_user.username, selected_user.password, selected_user.email)

# jason.password = "new_password"
# session.add(jason)
# # session.delete(bob)
# session.commit()

# app = None
# @app.route("/users")
# def list_user():
#     users = session.query(UserModel).all()
#     return jsonify(users)

# app = Flask(__name__)
# @app.route("/signup", methods=["POST"])
# def signup() :
#     '''회원가입'''
#     #flask request 값 가져오기
#     username = request.form.get("username")
#     password = request.form.get("password")
#     name = request.form.get("name")
#     email = request.form.get("email")

#     #sqlalchemy를 이용하여 db에 사용자 저장하기
#     user = UserModel(username, password, name, email)
#     session.add(user)
#     session.commit()
    
#     return "SUCCESS"

# @app.route("/signin", methods=["POST"])
# def signin():
#     '''로그인'''
#     #flask request에서 값 가져오기
#     username = request.form.get("username")
#     password = request.form.get("password")

#     #값으로 db 조회하여 사용자 찾기
#     user = session.query(UserModel).filter(
#         UserModel.username == username, 
#         UserModel.password == password).one_or_none()
#     if user is None:
#         return "No User"

#     return jsonify(user)
# app.run(debug=True)


# def change_password(user_id):
#     '''비밀번호 변경'''
#     pass

# def delete_user():
#     '''사용자 탈퇴'''
#     pass

app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def signup():
    """회원가입"""
    # flask request 값 가져오기
    username = request.json.get("username")
    password = request.json.get("password")
    name = request.json.get("name")
    email = request.json.get("email")


    user = session.query(UserModel).filter(UserModel.username == username).one_or_none()
    if user is not None:
        return Response("이미 존재하는 username입니다.", status=400)
    




    # sqlalchemy를 이용하여 db에 사용자 저장하기
    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()
    
    return Response("SUCCESS", status=201)


@app.route("/signin", methods=["POST"])
def signin():
    """로그인"""
    # flask request에서 값 가져오기
    username = request.json.get("username")
    password = request.json.get("password")

    # 값으로 db 조회하여 사용자 찾기
    user = session.query(UserModel).filter(
        UserModel.username == username, 
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return Response("No User", status=204)

    return jsonify({
        "user_id" : user.user_id,
        "username": user.username,
        "password": user.password,
        "name": user.name,
        "email": user.email
    })
@app.route('/user/password', methods=['PATCH'])
def change_password():
    '''비밀번호 수정'''
    username = request.json.get('username')
    password = request.json.get("password")

    new_password = request.form.get("new_password")

    if password == new_password:
        return Response("기존 비밀번호와 새로운 비밀번호는 동일할 수 없습니다.", status=400)

    


    
    user = session.query(UserModel).filter(UserModel.username == username, UserModel.password == password).one_or_none()
    if user is None:
        return Response("No User", status=204)

    user.password = new_password
    session.add(user)
    session.commit()

    return Response("SUCCESS", status=200)
@app.route("/user", methods=["DELETE"])
def delete_user():
    """사용자 탈퇴"""
    username = request.form.get('username')
    password = request.form.get("password")

    new_password = request.form.get("new_password")

    user = session.query(UserModel).filter(UserModel.username == username, UserModel.password == password).one_or_none()
    if user is None:
        return Response("No User", status=204)

    session.delete(user)
    session.commit()

    return Response("SUCCESS", status=200)





app.run(debug=True)
