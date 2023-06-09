import functions
import PySimpleGUI as sg
import time
import os
if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
sg.theme("LightBlue")
time_label = sg.Text('',key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
# list of values to be displayed,Values = List of values to display. Can be any type including mixed types
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
layout=[[time_label],[label], [input_box, add_button], [list_box, edit_button,complete_button],[exit_button]]
window = sg.Window("My To-Do app",
                   layout=layout,
                   font=('Helvetica', 17))

while True:
    # Values is a dictionary with the keys todo and todos:
    # event is a string that identifies an action that has occurred in the GUI(such as clicking a button):
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                # from the values dict get the todo from the todos key and we use [0] to get the string only:
                todo_to_edit = values['todos'][0]
                # new_todo is from the values dict and has the todo key
                new_todo = values['todo']
                # if not new_todo.endswith("\n"):
                #     new_todo += "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select something first")

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                completed_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except:
                sg.popup("Please select something to complete first")
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
window.close()
