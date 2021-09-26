from mysql.connector import cursor
from function import read_all, validate
from flask import jsonify



def test_get():    
    cursor = {('pepe', 3, 'formosa'), ('maria', 5, 'cordoba')}
    assert read_all(cursor) == [('pepe', 3, 'formosa'), ('maria', 5, 'cordoba')]

def test_validate_true():
    aux = '123'
    assert validate(aux) == '123' 

def test_validate_false():
    aux = ''
    assert validate(aux) == False 