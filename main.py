while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:]

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        tasks.append(task + '\n')

        with open('tasks.txt', 'w') as file:
            tasks = file.writelines(tasks)

    elif user_action.startswith('show'):
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}:{item}"
            print(row)

    elif user_action.startswith('edit'):
        number = int(user_action[5])
        print(number)
        number = number - 1

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        new_task = input ("Enter new task: ")
        tasks[number] = new_task + '\n'

        with open('tasks.txt', 'w') as file:
            tasks = file.writelines(tasks)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()

        index = number - 1
        task_to_remove = tasks[index].strip('\n')
        tasks.pop(index)

        with open('tasks.txt', 'w') as file:
            tasks = file.writelines(tasks)

        message = f"Task: {task_to_remove}, was removed from the list." 
        print(message)   

    elif 'exit' in user_action:
        break

    else: 
        print("The command entered is not valid")

print("Goodbye!")

