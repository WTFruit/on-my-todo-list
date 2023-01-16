import functions as es
import PySimpleGUI as ui

label = ui.Text("Type in a task")
input_box = ui.InputText(tooltip="This is where you can type in your tasks", key="task")
add_button = ui.Button("Add")
exit_button = ui.Button("Exit")


# I created this variable to make the layout easier to see.
# The window layout parameter requires a list containing sub-lists. Each sub-list
# represents a visual row of the interface, lining objects up with each other.
window_layout = [
                [label],
                [input_box, add_button],
                [exit_button]
                ]
window = ui.Window("It's On My Todo List (c) Nate Weil 2023", layout=window_layout, font=("Helvetica", 16))


while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            tasks = es.file_io(None, readwrite="r")

            new_task = values["task"] + "\n"
            tasks.append(new_task)

            es.file_io(tasks, readwrite="w")

        case ui.WIN_CLOSED:
            break

        case "Exit":
            break

window.close()