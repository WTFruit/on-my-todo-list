import functions as es
import PySimpleGUI as ui
import time as t
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

ui.theme("LightGrey1")

clock = ui.Text("", key="clock")

input_box = ui.InputText(tooltip="This is where you can type in your tasks", key="task")

add_button = ui.Button("Add", button_color=("blue",""), size=(11,1))
# add_button = ui.Button(image_source="add.png", key="Add", tooltip="Add task")
replace_button = ui.Button("Replace", button_color=("blue","white"))

insert_button = ui.Button("Insert after")
complete_button = ui.Button("Complete", button_color=("red",""), size=(13,1))

task_list = ui.Listbox(values=es.file_io(None, readwrite="r"), key="tasklist", enable_events=True, size=(44, 10))

exit_button = ui.Button("Exit")
message_label = ui.Text("Nothing to report",key="message")

# I created this variable to make the layout easier to see.
# The window layout parameter requires a list containing sub-lists. Each sub-list
# represents a visual row of the interface, lining objects up with each other.
window_layout = [
                [clock],
                [input_box],
                [add_button, replace_button, insert_button, complete_button],
                [task_list],
                [exit_button, message_label]
                ]
ui.theme("LightGrey1")
window = ui.Window("It's On My Todo List (c) Nate Weil 2023", layout=window_layout, font=("Helvetica", 16))


while True:

    # Loop pauses at the read() line until an event is received. Timeout allows the loop to proceed (100ms?)
    event, values = window.read(timeout=1000)

    window["clock"].update(value=t.strftime("%b %d, %Y %H:%M:%S"))

    if event != "__TIMEOUT__":
        print(f"Trigger: {event}")
        print(f"Values: {values}")

    match event:
        case "Add":
            if values["task"] != "":
                tasks = es.file_io(None, readwrite="r")

                new_task = values["task"] + "\n"
                tasks.append(new_task)

                es.file_io(tasks, readwrite="w")
                window["tasklist"].update(values=es.file_io(None, readwrite="r"))
            else:
                window["message"].update(value="Can't add a blank task!")

        case "Replace":
            try:
                if values["task"] != "":
                    tasks = es.file_io(None, readwrite="r")

                    task_to_edit = values["tasklist"][0]
                    replacement = values["task"] + "\n"

                    # You can get the index of an item in a list if you know its value
                    index = tasks.index(task_to_edit)
                    tasks[index] = replacement

                    es.file_io(tasks, readwrite="w")
                    window["tasklist"].update(values=es.file_io(None, readwrite="r"))
                else:
                    window["message"].update(value="Can't replace with a blank task!")

            except IndexError:
                ui.Popup("Please select a task first", font=("Helvetica", 16))

        case "Complete":
            try:
                tasks = es.file_io(None, readwrite="r")

                task_to_remove = values["tasklist"][0]
                index = tasks.index(task_to_remove)
                tasks.pop(index)

                es.file_io(tasks, readwrite="w")
                window["tasklist"].update(values=es.file_io(None, readwrite="r"))

            except IndexError:
                ui.Popup("Please select a task first", font=("Helvetica", 16))

        case "Insert after":
            try:
                tasks = es.file_io(None, readwrite="r")
                task_to_insert = values["task"] + "\n"
                previous_task = values["tasklist"][0]
                index = tasks.index(previous_task) + 1
                tasks.insert(index, task_to_insert)

                es.file_io(tasks, readwrite="w")
                window["tasklist"].update(values=es.file_io(None, readwrite="r"))

            except IndexError:
                ui.Popup("Please select a task first", font=("Helvetica", 16))

        case "tasklist":
            selected = values["tasklist"][0].strip("\n")
            window["task"].update(value=selected)

        case ui.WIN_CLOSED:
            break

        case "Exit":
            break

window.close()