import functions as es
import PySimpleGUI as ui

label = ui.Text("Type in a task")

input_box = ui.InputText(tooltip="This is where you can type in your tasks", key="task")

edit_button = ui.Button("Edit")
add_button = ui.Button("Add")
insert_button = ui.Button("Insert")
delete_button = ui.Button("Remove")

task_list = ui.Listbox(values=es.file_io(None, readwrite="r"), key="tasklist", enable_events=True, size=[44, 10])

exit_button = ui.Button("Exit")

# I created this variable to make the layout easier to see.
# The window layout parameter requires a list containing sub-lists. Each sub-list
# represents a visual row of the interface, lining objects up with each other.
window_layout = [
                [label],
                [input_box],
                [edit_button, add_button, insert_button, delete_button],
                [task_list],
                [exit_button]
                ]
window = ui.Window("It's On My Todo List (c) Nate Weil 2023", layout=window_layout, font=("Helvetica", 16))


while True:

    # Loop pauses at the read() line until an event is received
    event, values = window.read()
    print(f"Trigger: {event}")
    print(f"Values: {values}")

    match event:
        case "Add":
            tasks = es.file_io(None, readwrite="r")

            new_task = values["task"] + "\n"
            tasks.append(new_task)

            es.file_io(tasks, readwrite="w")
            window["tasklist"].update(values=es.file_io(None, readwrite="r"))

        case "Edit":
            tasks = es.file_io(None, readwrite="r")

            task_to_edit = values["tasklist"][0]
            replacement = values["task"] + "\n"

            # You can get the index of an item in a list if you know its value
            index = tasks.index(task_to_edit)
            tasks[index] = replacement

            es.file_io(tasks, readwrite="w")
            window["tasklist"].update(values=es.file_io(None, readwrite="r"))

        case "Remove":
            tasks = es.file_io(None, readwrite="r")

            task_to_remove = values["tasklist"][0]
            index = tasks.index(task_to_remove)
            tasks.pop(index)

            es.file_io(tasks, readwrite="w")
            window["tasklist"].update(values=es.file_io(None, readwrite="r"))

        case "tasklist":
            selected = values["tasklist"][0].strip("\n")
            window["task"].update(value=selected)

        case ui.WIN_CLOSED:
            break

        case "Exit":
            break

window.close()