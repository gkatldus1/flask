from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from model.user_model import UserModel  
from flask import Flask, request, jsonify
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
    username = request.form.get("username")
    password = request.form.get("password")
    name = request.form.get("name")
    email = request.form.get("email")

    # sqlalchemy를 이용하여 db에 사용자 저장하기
    user = UserModel(username, password, name, email)
    session.add(user)
    session.commit()
    
    return "SUCCESS"


@app.route("/signin", methods=["POST"])
def signin():
    """로그인"""
    # flask request에서 값 가져오기
    username = request.form.get("username")
    password = request.form.get("password")

    # 값으로 db 조회하여 사용자 찾기
    user = session.query(UserModel).filter(
        UserModel.username == username, 
        UserModel.password == password
    ).one_or_none()
    if user is None:
        return "No User"

    return jsonify({
        "user_id" : user.user_id,
        "username": user.username,
        "password": user.password,
        "name": user.name,
        "email": user.email
    })

app.run(debug=True)
# def change_password(user_id):
#     """비밀번호 변경"""
    
#     pass


# def delete_user():
#     """사용자 탈퇴"""
#     pass