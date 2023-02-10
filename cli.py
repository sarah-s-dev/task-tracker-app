import functions

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:]

        tasks = functions.get_tasks()
        tasks.append(task + '\n')

        functions.update_tasks(tasks)

    elif user_action.startswith('show'):
        
        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}:{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5])
            print(number)
            number = number - 1

            tasks = functions.get_tasks()

            new_task = input ("Enter new task: ")
            tasks[number] = new_task + '\n'

            functions.update_tasks(tasks)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            tasks = functions.get_tasks()
            index = number - 1
            task_to_remove = tasks[index].strip('\n')
            tasks.pop(index)

            functions.update_tasks(tasks)

            message = f"Task: {task_to_remove}, was removed from the list." 
            print(message)   
        except IndexError:
            print("There is no item with that number")    
            continue
        
    elif 'exit' in user_action:
        break

    else: 
        print("The command entered is not valid")

print("Goodbye!")

