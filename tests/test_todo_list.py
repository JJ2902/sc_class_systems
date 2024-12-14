from lib.todo_list import *
from lib.todo import *

def test_initialises_correctly():
    todoList_one = TodoList()

def test_add_correctly_todo_instances():
    todoList_one = TodoList()
    todo_one = Todo("Task one", False)
    todo_two = Todo("Task two", False)

    #Add
    todoList_one.add(todo_one)
    todoList_one.add(todo_one)

    assert todoList_one.todo_list == [todo_one, todo_one]

def test_incomplete_returns_incomplete_todo_list():
    todoList_one = TodoList()
    todo_one = Todo("Task one", False)
    todo_two = Todo("Task two", False)
    todo_three = Todo("Task three", True)

    #Add
    todoList_one.add(todo_one)
    todoList_one.add(todo_two)
    todoList_one.add(todo_three)

    incomplete_todos = todoList_one.incomplete()
    assert incomplete_todos == [todo_one, todo_two]  # Compare Todo instances

def test_complete_returns_complete_playlist():
    todoList_one = TodoList()
    todo_one = Todo("Task one", False)
    todo_two = Todo("Task two", False)
    todo_three = Todo("Task three", True)

    #Add
    todoList_one.add(todo_one)
    todoList_one.add(todo_two)
    todoList_one.add(todo_three)

    complete_todos = todoList_one.complete()
    assert complete_todos == [todo_three]

def test_giveup_returns_mark_all_complete():
    todoList_one = TodoList()
    todo_one = Todo("Task one", False)
    todo_two = Todo("Task two", False)
    todo_three = Todo("Task three", True)

    #Add
    todoList_one.add(todo_one)
    todoList_one.add(todo_two)
    todoList_one.add(todo_three)

    #
    giveup = todoList_one.give_up()
    assert giveup == ([todo_one, todo_two, todo_three])







