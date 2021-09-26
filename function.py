from flask import jsonify

def read_all(cursor):
    if cursor:
        data = []
        for row in cursor:
            data.append(row)
        return data
    else: 
        return {'mensage': 'ERROR.'}

def validate(data):
    if len(data) > 0:
        return data
    return False
    