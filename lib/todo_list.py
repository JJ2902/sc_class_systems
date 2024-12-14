class TodoList:
    def __init__(self):
        self.todo_list = []
        self.incomplete_todo_list = []
        self.complete_todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        for task in self.todo_list:
            if task.complete is False:
                self.incomplete_todo_list.append(task)
        return self.incomplete_todo_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        for task in self.todo_list:
            if task.complete is True:
                self.complete_todo_list.append(task)
        return self.complete_todo_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todo_list:
            self.complete_todo_list.append(task)
        for task in self.incomplete_todo_list:
            self.complete_todo_list.append(task)
        return self.complete_todo_list

