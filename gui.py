import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task", key="task")
add_task_button = sg.Button("Add")
edit_task_button = sg.Button("Edit")
complete_task_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_tasks(), key='tasks', 
                      enable_events=True, size=[45, 10]), 

window = sg.Window('Task tracker app', 
                    layout=[[label], 
                    [input_box, add_task_button], 
                    [list_box, edit_task_button, complete_task_button],
                    [exit_button]],
                    font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.update_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.update_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Complete":
            task_to_complete = values['tasks'][0]    
            tasks = functions.get_tasks()
            tasks.remove(task_to_complete)
            functions.update_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")

        case "Exit":
            break    

        case 'tasks':
               window['task'].update(value=values['tasks'][0])     
               
        case sg.WIN_CLOSED:
            break

window.close()
 




