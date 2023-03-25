import functions
import PySimpleGUI as sg
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")
# layout expects  a list of object instances
window = sg.Window("My To-Do app",layout=[[label],[input_box,add_button]])
window.read()
window.close()