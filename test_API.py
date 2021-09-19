from flask.json import jsonify
from main import get_task, get_tasks, add_task, edit_task, dell_task



def test_get():
    res = get_tasks()
    print(res)
    assert res == type(jsonify)