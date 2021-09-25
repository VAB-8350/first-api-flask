from flask import jsonify

def read_all(cursor):
    if cursor:
        data = []
        for row in cursor:
            data.append(row)
        return jsonify(data)
    else: 
        return jsonify({'mensage': 'ERROR.'})