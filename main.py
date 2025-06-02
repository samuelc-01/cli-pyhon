list_task = {}   # Move outside the loop
list_in_progress = {}
list_done = {}
list_no_done = {}
task_id = 1      # Move outside the loop


# class UserMethods:
#     def methods(userInput):
#         global task_id, list_task, list_in_progress
#         list_arguments = userInput.strip().split()
#         command = list_arguments[0]
#         if command == "docs":
#             print(["add", "update", "list", "list todo", "list done", "mark-in-progress", "delete"])
#
#         elif command == "add":
#             task_description = " ".join(list_arguments[1:])
#             list_task[task_id] = task_description
#             print(f"task added successfully (ID: {task_id}): \"{task_description}\"")
#             task_id += 1
#
#         elif command == "list":
#            if len(list_arguments) == 0:
#                for id, desc in list_task.tems():
#                    print(f"{id}: {desc}")
#         elif list_arguments[0] == "in-progress":
#             for id, desc in list_in_progress.items():
#                 print(f"{id}: {desc}")
#         elif list_arguments[0] == "done":
#             for id, desc in list_done.items():
#                 print(f"{id}: {desc}")
#
#         elif command == "delete":
#             task_to_delete = int(list_arguments[1])
#             if task_to_delete in list_task:
#                 del list_task[task_to_delete]
#                 print(f"Task {task_to_delete} deleted.")
#                 print(list_task)
#             else:
#                 print("Task ID not found.")
#
#         elif command == "update":
#             task_to_update = int(list_arguments[1])
#             if task_to_update in list_task:
#                 new_description = " ".join(list_arguments[2:])
#                 list_task[task_to_update] = new_description
#                 print(f"Task {task_to_update} updated to: \"{new_description}\"")
#
#         elif command == "mark-in-progress":
#             task_to_mark = int(list_arguments[1])
#             if task_to_mark in list_task:
#                 list_in_progress[task_to_mark] = list_task[task_to_mark]
#                 del list_task[task_to_mark]
#                 print(f"Task {task_to_mark} moved to list_progress")
#
#         else:
#             print("invalid Command.")
#
def show_docs():
    print(["add", "update", "list", "list todo", "list in-progress", "list done",
           "delete", "mark-in-progress", "mark-done", "exit"])

def add_task(args):
    global task_id
    description = " ".join(args)
    list_task[task_id] = description
    print(f"Task added (ID: {task_id}): \"{description}\"")
    task_id += 1

def list_tasks():
    print("📝 To-do Tasks:")
    for id, desc in list_task.items():
        print(f"{id}: {desc}")

def list_progress():
    print("🚧 In-Progress Tasks:")
    for id, desc in list_in_progress.items():
        print(f"{id}: {desc}")

def list_done_tasks():
    print("✅ Done Tasks:")
    for id, desc in list_done.items():
        print(f"{id}: {desc}")

def delete_task(args):
    task_id_to_delete = int(args[0])
    if task_id_to_delete in list_task:
        del list_task[task_id_to_delete]
        print(f"Task {task_id_to_delete} deleted from todo.")
    elif task_id_to_delete in list_in_progress:
        del list_in_progress[task_id_to_delete]
        print(f"Task {task_id_to_delete} deleted from in-progress.")
    elif task_id_to_delete in list_done:
        del list_done[task_id_to_delete]
        print(f"Task {task_id_to_delete} deleted from done.")
    else:
        print("❌ Task ID not found.")

def update_task(args):
    task_id_to_update = int(args[0])
    new_desc = " ".join(args[1:])
    for task_list in (list_task, list_in_progress, list_done):
        if task_id_to_update in task_list:
            task_list[task_id_to_update] = new_desc
            print(f"Task {task_id_to_update} updated to: \"{new_desc}\"")
            return
    print("❌ Task ID not found.")

def mark_in_progress(args):
    task_to_mark = int(args[0])
    if task_to_mark in list_task:
        list_in_progress[task_to_mark] = list_task.pop(task_to_mark)
        print(f"Task {task_to_mark} moved to in-progress.")
    else:
        print("❌ Task ID not found in todo.")

def mark_done(args):
    task_to_mark = int(args[0])
    if task_to_mark in list_in_progress:
        list_done[task_to_mark] = list_in_progress.pop(task_to_mark)
        print(f"Task {task_to_mark} marked as done.")
    else:
        print("❌ Task ID not found in in-progress.")

# Mapeamento de comandos
commands = {
    "docs": lambda args: show_docs(),
    "add": add_task,
    "list": lambda args: list_tasks(),
    "list todo": lambda args: list_tasks(),
    "list in-progress": lambda args: list_progress(),
    "list done": lambda args: list_done_tasks(),
    "delete": delete_task,
    "update": update_task,
    "mark-in-progress": mark_in_progress,
    "mark-done": mark_done,
}

# Loop principal
while True:
    user_input = input("task-cli> ").strip()
    if user_input == "exit":
        break

    input_parts = user_input.split()
    if not input_parts:
        continue

    command = input_parts[0]
    args = input_parts[1:]

    if command in commands:
        commands[command](args)
    elif user_input.startswith("list "):  # Para comandos como "list in-progress"
        full_command = " ".join(input_parts[:2])
        if full_command in commands:
            commands[full_command](args[1:])
        else:
            print("❌ Invalid list command.")
    else:
        print("❌ Invalid command. Type 'docs' to see available options.")
