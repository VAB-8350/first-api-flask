from flask import Flask, jsonify, request
import mysql.connector

from data import conect

app = Flask(__name__)

mydb = mysql.connector.connect(
  host= conect['host'],
  user= conect['user'],
  password= conect['password'],
  database= conect['database']
)
cursor = mydb.cursor()

#get
@app.route('/')
def get_tasks():
    cursor.execute("SELECT * FROM task.tareas")
    data = []
    for row in cursor:
        data.append(row)
    return jsonify(data)

#get for id
@app.route('/task/<int:id>')
def get_task(id):
    cursor.execute("SELECT * FROM task.tareas WHERE id = %s"% id)
    validate = cursor.fetchall()
    if len(validate) > 0:
        return jsonify(validate)
    return jsonify(False)

#add new task
@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = (
        request.json['titulo'],
        request.json['descripcion'],
        request.json['nombre_usuario'],
        request.json['estado']
    )

    sql = "INSERT INTO task.tareas (titulo, descripcion, nombre_usuario, estado) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, new_task)
    mydb.commit()

    return jsonify({'mensage': 'add with exit!!'})

#edit task, search for id
@app.route('/edit_task/<int:id>', methods=['PUT'])
def edit_task(id):

    sql = "SELECT id FROM task.tareas WHERE id = %s"% id
    cursor.execute(sql)
    validate = cursor.fetchall()

    if len(validate) > 0:
        titulo = "titulo = '"+request.json['titulo']+"'"
        descripcion = "descripcion = '"+request.json['descripcion']+"'"
        nombre = "nombre_usuario = '"+request.json['nombre_usuario']+"'"
        estado = "estado = "+str(request.json['estado'])+""

        sql = "UPDATE task.tareas SET %s, %s, %s, %s WHERE id = %s"%  (titulo, descripcion, nombre, estado, id)
        cursor.execute(sql)
        mydb.commit()

        return jsonify({'mensage': 'edit with exit!!'})
    return jsonify(False)

#dell task, search for id 
@app.route('/dell_task/<int:id>', methods=['DELETE'])
def dell_task(id):

    sql = "SELECT id FROM task.tareas WHERE id = %s"% id
    cursor.execute(sql)
    validate = cursor.fetchall()

    if len(validate) > 0:

        sql = "DELETE FROM task.tareas WHERE id = %s"% id
        cursor.execute(sql)
        mydb.commit()
        
        return jsonify({'mensage': 'task deel!!'})

    return jsonify(False)

if __name__ == '__main__':
    app.run(debug=True, port=4000)