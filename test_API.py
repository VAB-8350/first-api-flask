from function import read_all
from flask.json import jsonify
from main import get_task, get_tasks, add_task, edit_task, dell_task



def get():
    cursor = {[
            1,
            "caminar",
            "correr",
            null,
            null,
            "maria",
            3
        ],}
    
    res = read_all(cursor)
    print(res)
    assert res == res