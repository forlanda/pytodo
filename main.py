import functions
import FreeSimpleGUI as sg
import time

TODO_FILEPATH = "output/todo.txt"
todos = []
buttons = ["Add", "Edit", "Complete", "Exit"]
labels = ["Todo", "Todos", "Feedback"]
button = {}
label = {}
todo_input = sg.InputText(key="todo_input")
todo_list = sg.Listbox(enable_events=True, size=(50,10), key="todo_list",values="")

for b in buttons:
    button[b] = sg.Button(b, key=b)
for l in labels:
    label[l] = sg.Text(l, key=l)

layout = [[label["Todo"]],
          [todo_input,button["Add"]],
          [label["Todos"]],
          [todo_list,button["Edit"],button["Complete"]],
          [label["Feedback"]],
          [button["Exit"]]]

window = sg.Window("TODO App", layout=layout)
list_index = -1
if __name__ == '__main__':
    todos = functions.read_todos(TODO_FILEPATH)
    while True:
        event, value = window.read(timeout=500)
        window["todo_list"].update(todos)
        clock = time.strftime("%m/%d/%Y %H:%M:%S")
        window["Feedback"].update(clock)
        #print(f"event:  {event} | value:  {value}")
        match event:
            case "Exit":
                exit()
            case "Add":
                if value != "":
                    #print(value)
                    todo = value["todo_input"]+"\n"
                    todos.append(todo)
                    functions.write_todos(TODO_FILEPATH,todos)
                    window["todo_list"].update(todos)
                    window["todo_input"].update("")
            case "todo_list":
                window["todo_input"].update(value['todo_list'][0])
                list_index = todos.index(todo_input.get())
            case "Edit":
                if list_index < 0:
                    pass
                else:
                    todos[list_index] = f"{todo_input.get()}\n"
                    functions.write_todos(TODO_FILEPATH, todos)
                    window["todo_input"].update("")
            case "Complete":
                if list_index < 0:
                    pass
                else:
                    todos.pop(list_index)
                    functions.write_todos(TODO_FILEPATH, todos)
                    window["todo_input"].update("")

