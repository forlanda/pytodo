def read_todos(filepath):
    try:
        with open(filepath,"r") as file:
            todos = file.readlines()
            return todos
    except FileNotFoundError:
        with open(filepath,"w") as file:
            return []


def write_todos(filepath, todos):
    try:
        with open(filepath,"w") as file:
            file.writelines(todos)
        return
    except:
        return