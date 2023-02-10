FILEPATH = "tasks.txt"

def get_tasks(filepath=FILEPATH):
    """ Read a text file and return the list of task items."""
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    return tasks

def update_tasks(tasks, filepath=FILEPATH):
    """ Write task items into a text file."""
    with open(filepath, 'w') as file:
        tasks = file.writelines(tasks)

if __name__ == "__main__":
    print("Hello")
    print(get_tasks())