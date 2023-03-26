# import the functions module and PySimpleGUI library
import functions
import PySimpleGUI as sg

# create a Text object to display a label
label = sg.Text("Type in a To-Do")

# create an InputText object for the user to enter a to-do item
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")

# create a Button object to add the to-do item to the list
add_button = sg.Button("Add")

# create a Listbox object to display the current to-do items
# get the to-do items from the functions module
# enable_events=True to allow the program to respond to the user selecting an item in the list
# size=[45,10] sets the size of the list box
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])

# create a Button object to edit the selected to-do item
edit_button = sg.Button('Edit')

# create a Window object to hold the layout
# layout is a nested list of the elements to be displayed on the window
# font=('Helvetica',17) sets the font of the window
window = sg.Window("My To-Do app", layout=[[label],[input_box,add_button],[list_box,edit_button]], font=('Helvetica',17))

# create a loop to continually read user input from the window
while True:
    # read the user input from the window
    event, values = window.read()

    # print the event and the current values dictionary to the console for debugging
    print(event)
    print(values)

    # check the event variable to determine what action to take
    match event:
        # if the "Add" button was clicked
        case "Add":
            # get the current to-do items from the functions module
            todos = functions.get_todos()

            # create a new to-do item by adding a newline character to the user's input
            new_todo = values['todo'] + "\n"

            # append the new to-do item to the list of current to-do items
            todos.append(new_todo)

            # write the updated to-do items to the functions module
            functions.write_todos(todos)

            # update the values of the Listbox object to display the updated to-do items
            window['todos'].update(values=todos)

        # if the "Edit" button was clicked
        case "Edit":
            # get the to-do item that the user has selected in the Listbox
            todo_to_edit = values['todos'][0]

            # get the new text for the to-do item from the user's input
            new_todo = values['todo']

            # get the current to-do items from the functions module
            todos = functions.get_todos()

            # find the index of the to-do item that the user has selected in the Listbox
            index = todos.index(todo_to_edit)

            # replace the selected to-do item with the new text
            todos[index] =  new_todo

            # write the updated to-do items to the functions module
            functions.write_todos(todos)

            # update the values of the Listbox object to display the updated to-do items
            window['todos'].update(values=todos)

        # if the user selects an item in the Listbox
        case "todos":
            # update the value of the InputText object to match the selected to-do item
            window['todo'].update(value=values['todos'][0])

        # if the user closes the window
        case sg.WIN_CLOSED:
            break



window.close()