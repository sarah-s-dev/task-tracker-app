import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task", key="task")
add_task_button = sg.Button("Add")

window = sg.Window('Task tracker app', 
                    layout=[[label], [input_box, add_task_button]], 
                    font=('Helvetica', 15))

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

        case sg.WIN_CLOSED:
            break

window.close()
 




