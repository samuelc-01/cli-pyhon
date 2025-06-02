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
