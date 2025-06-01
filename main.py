list_task = {}   # Move outside the loop
list_in_progress = {}
task_id = 1      # Move outside the loop

def methods(userInput):
    global task_id, list_task, list_in_progress
    list_arguments = userInput.strip().split()
    command = list_arguments[0]
    if command == "docs":
        print(["add", "update", "list", "list todo", "list done", "mark-in-progress"])

    elif command == "add":
        task_description = " ".join(list_arguments[1:])
        list_task[task_id] = task_description
        print(f"task added successfully (ID: {task_id}): \"{task_description}\"")
        task_id += 1

    elif command == "list":
        for id, desc in list_task.items():
            print(f"{id}: {desc}")

    elif command == "list in-progress":
        for id, desc in list_in_progress.items():
            print(f"{id}: {desc}")

    elif command == "delete":
        task_to_delete = int(list_arguments[1])
        if task_to_delete in list_task:
            del list_task[task_to_delete]
            print(f"Task {task_to_delete} deleted.")
        else:
            print("Task ID not found.")

    elif command == "update":
        task_to_update = int(list_arguments[1])
        if task_to_update in list_task:
            new_description = " ".join(list_arguments[2:])
            list_task[task_to_update] = new_description
            print(f"Task {task_to_update} updated to: \"{new_description}\"")

    elif command == "mark-in-progress":
        task_to_mark = int(list_arguments[1])
        if task_to_mark in list_task:
            list_in_progress[task_to_mark] = list_task[task_to_mark]
            del list_task[task_to_mark]
            print(f"Task {task_to_mark} moved to list_progress")

    else:
        print("invalid Command.")


while True:
    userInput = input("task-cli:")
    if userInput == "exit":
        break
    methods(userInput)
