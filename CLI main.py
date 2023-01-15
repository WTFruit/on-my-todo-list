from functions import *
from time import strftime

"""
"from [file] import [methods]" allows you to treat the imported functions as if they are inline.
If you use "import [file]", you need to use dot notation to access functions, such as "function.file_io().
"""

tasks = file_io(None, readwrite="r")

now = strftime("%b %d, %Y %H:%M:%S")
print("Currently: " + now)

while True:

    print_tasks(tasks)

    user_action = input('Type "add [task]", "show", "edit [n]", "complete [n]", or "exit" (and save): ')
    user_action = user_action.lower()

    # Seems to search for the string within the variable?
    if "add" in user_action[:3]:

        if len(user_action) > 4:
            # This is treating the string as a list, starting from the 4th index character and continuing to the end.
            new_task = user_action[4:] + "\n"
            tasks.append(new_task)

    elif user_action.startswith("edit "):
        number = 0
        try:
            number = int(user_action[5:])
            number -= 1

            if number < 0:
                print(f'\nInvalid input: no task with an index number of "{number + 1}".\n')
                continue

            tasks[number] = tasks[number].strip("\n")
            new = input('What do you want to replace "' + tasks[number] + '" with? ') + "\n"
            tasks[number] = new

        except ValueError:
            print('\nInvalid input: expected a number after "edit".\n')
        except IndexError:
            print(f'\nInvalid input: no task with an index number of "{number+1}".\n')

    elif "complete" in user_action[:8]:
        try:
            complete = int(user_action[9:])
            tasks.pop(complete - 1)

        except IndexError:
            print(f'\nInvalid input: no task with an index number of "{number+1}".\n')

    elif "show" in user_action[:4]:
        continue

    elif "exit" in user_action[:4]:
        file_io(tasks, readwrite="w")
        print("File successfully saved. Bye!")
        break  # Exit current loop

    else:
        print("Beep boop: unable to parse input.\n")