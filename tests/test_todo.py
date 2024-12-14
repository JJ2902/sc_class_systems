from lib.todo import *
import pytest

def test_diary_initialises_correctly():
    todo_one = Todo("Task one", False)

    assert todo_one.task == "Task one"
    assert todo_one.complete == False

def test_diary_initialises_correctly_two():
    todo_one = Todo("Task one", True)

    assert todo_one.task == "Task one"
    assert todo_one.complete == True

# def test_empty_string_returns_error():
#     todo_one = Todo("Task one", True)
#     with pytest.raises(ValueError) as e:
#         todo_one.task = ""
#     error = e.value
#     assert str(error) == "Task name not given."

def test_mark_complete_updates_complete():
    todo_one = Todo("Task one", False)

    todo_one.mark_complete()
    result = todo_one.complete is True
    assert result is True




