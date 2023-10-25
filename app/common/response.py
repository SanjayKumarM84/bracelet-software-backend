from flask import jsonify


def success(message, content, status_code=200):
    data = {'message': message, 
            'content': content}
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp


def failure(message, content, status_code=400):
    data = {'message': message, 
            'content': content}
    resp = jsonify(data)
    resp.status_code = status_code
    resp.content_type = "application/json"
    return resp

