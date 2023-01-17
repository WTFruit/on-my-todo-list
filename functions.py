FILEPATH = "todos.txt"

def file_io(data, filepath=FILEPATH, readwrite="r"):
    """ Accesses a file and either reads to it, or writes from it. If reading, returns a list object. """

    if readwrite == "r":
        with open(filepath, readwrite) as file:
            local_tasks = file.readlines()
            return local_tasks

    elif readwrite == "w":
        with open(filepath, readwrite) as file:
            file.writelines(data)


def print_tasks(list_of_tasks=["Empty list"]):
    """ Prints the passed list, numbered and with a starting index of 1. """

    print(" ")
    for i, item in enumerate(list_of_tasks):
        item = item.strip("\n")
        print(f"{i + 1}. {item}")
    print(" ")

# "__main__" doesn't refer to a file called "main", it refers to THIS file.
# __name__ is a predefined variable.
if __name__ == "__main__":
    print("Hello")