FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH): #set  with default parameter
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
       todos_local = file_local.readlines()
    return todos_local

def write_todos(datadet_arg,filepath = FILEPATH):
    """ Write to-do item list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(datadet_arg)

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())