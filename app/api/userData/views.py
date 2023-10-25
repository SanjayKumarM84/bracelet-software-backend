import hashlib
import traceback

from flask import request
from sqlalchemy import or_

from app.common.connection import (add_item, delete_item, query_list_to_dict,
                                   update_item)
from app.common.response import failure, success
from config import app

from app.api.userData.models import User
from werkzeug.security import generate_password_hash, check_password_hash

# Function to hash a password using SHA-256
def hash_password(password):
    salt = 'random_salt'  # You should use a unique salt per user
    password = password + salt
    return hashlib.sha256(password.encode()).hexdigest()


# Function to verify a password
def verify_password(plain_password, stored_hashed_password):
    salt = 'random_salt'
    input_password = plain_password + salt
    input_hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
    print(input_hashed_password, stored_hashed_password)
    return input_hashed_password == stored_hashed_password


@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        payload = request.get_json()
        name = payload.get('name')
        email = payload.get('email', '')
        phoneNo = payload.get('phoneNo')
        password = payload.get('password')

        if not (email or phoneNo):
            return failure(message="failure", content="Email Or Phone Number Is Not Passed!")
        if not password:
            return failure(message="failure", content="Password Not Passed!")

        userExists = User.query.filter(or_(User.email==email, User.phoneNo==phoneNo)).first()
        if userExists:
            return failure(message="failure", content="User Already Exists")

        userObj = User(
            name=name, email=email if email else None, phoneNo=phoneNo, password = hash_password(password)
        )
        add_item(userObj)

        return success(message="Successfully Signed Up", content={"userId": userObj.id}, status_code=201)
    except Exception as err:
        print(traceback.print_exc())
        return failure(message="failure", content="Something Went Wrong!")
        print(err)


@app.route('/login', methods=['POST'])
def login():
    try:
        payload = request.get_json()
        email = payload.get('email', '')
        phoneNo = payload.get('phoneNo')
        password = payload.get('password')

        if not (email or phoneNo):
            return failure(message="failure", content="Email Or Phone Number Is Not Passed!")
        if not password:
            return failure(message="failure", content="Password Not Passed!")

        userExists = User.query.filter(or_(User.email==email, User.phoneNo==phoneNo)).first()
        if not userExists:
            return failure(message="failure", content="User Not Found!")

        # print(userExists.password)
        if not verify_password(password, userExists.password):
            return failure(message="failure", content="Incorrect Password!")

        return success(message="Successfully Logged In", content={"userId": userExists.id})
    except:
        print(traceback.print_exc())
        return failure(message="failure", content="Something Went Wrong!")


@app.route('/updateUserData', methods=['POST'])
def addUserData():
    try:
        payload = request.get_json()
        id = request.headers.get('id')

        userObj = User.query.filter_by(id=id).first()
        if not userObj:
            return failure(message="failure", content="User Not Found!")
        
        age = payload.get('age')
        emergencyContact = payload.get('emergencyContact')
        
        userObj.emergencyContact = emergencyContact
        userObj.age = age
        update_item(userObj)

        return success(message="success",content="User Data Added Successfully!")
    except:
        print(traceback.print_exc())
        return failure(message="failure", content="Something Went Wrong!")


@app.route('/getUserData', methods=['GET'])
def getUserData():
    try:
        id = request.headers.get('id')
        userObj = User.query.filter_by(id=id).first()
        if userObj:
            return success(message="success", content=query_list_to_dict(userObj))
        return failure(message="failure", content="User Not Found!")
    except:
        print(traceback.print_exc())
        return failure(message="failure", content="Something Went Wrong!")


@app.route('/deleteUserData', methods=['DELETE'])
def deleteUserData():
    try:
        id = request.headers.get('id')
        userObj = User.query.filter_by(id=id).first()
        if userObj:
            delete_item(userObj)
            return success(message="success", content="User Data Deleted Successfully")
        return failure(message="failure", content="User Not Found!")
    except:
        print(traceback.print_exc())
        return failure(message="failure", content="Something Went Wrong!")
