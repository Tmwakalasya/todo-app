import functions
import PySimpleGUI as sg
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a to-do",key="todo")
add_button = sg.Button("Add")
# layout expects  a list of object instances
window = sg.Window("My To-Do app",
                   layout=[[label],[input_box,add_button]],
                   font=('Helvetica',17))
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break




window.close()