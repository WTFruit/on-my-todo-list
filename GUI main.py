import functions as es
import PySimpleGUI as ui


label = ui.Text("Type in a task")
input_box = ui.InputText(tooltip="This is where you can type in your tasks")
add_button = ui.Button("Add")

window = ui.Window("It's On My Todo List (c) Nate Weil 2023", layout=[[label], [input_box, add_button]])


window.read()
window.close()