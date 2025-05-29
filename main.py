# def add_new_task(inputUser):

# task_cli = {
#     "task-cli \n "
#                       "Actions: \n "
#                       "- add \n "
#                       "- update \n "
#                       "- delete \n "
#                       "- mark-in-progress \n "
#                       "- mark-done \n "
#                       "-Gets: \n"
#                       "-list \n"
#                       "-list done \n"
#                       "-list todo \n"
#                       "-list in-progress \n"
#                 }

# inputUser = str(input("task-cli \n "
#                       "Actions: \n "
#                       "- add \n "
#                       "- update \n "
#                       "- delete \n "
#                       "- mark-in-progress \n "
#                       "- mark-done \n "
#                       "-Gets: \n"
#                       "-list \n"
#                       "-list done \n"
#                       "-list todo \n"
#                       "-list in-progress \n"))

# task_list = []
task_commands = {
    "add": "Adiciona uma nova tarefa",
    "update": "Atualiza uma tarefa existente",
    "delete": "Remove uma tarefa",
    "mark-in-progress": "Marca a tarefa como em andamento",
    "mark-done": "Marca a tarefa como concluída",
    "list": "Lista todas as tarefas",
    "list done": "Lista tarefas concluídas",
    "list todo": "Lista tarefas pendentes",
    "list in-progress": "Lista tarefas em andamento"
}
task_actions = {
    "add": "Adiciona uma nova tarefa",
    "update": "Atualiza uma tarefa existente",
    "delete": "Remove uma tarefa",
    "mark-in-progress": "Marca a tarefa como em andamento",
    "mark-done": "Marca a tarefa como concluída",
}
task_list = {
    "list": "Lista todas as tarefas",
    "list done": "Lista tarefas concluídas",
    "list todo": "Lista tarefas pendentes",
    "list in-progress": "Lista tarefas em andamento"
}








inputUser = str(input("Welcome to task-cli:"))

def decode_docs(inputUser, task_commands):
    if inputUser == "docs":
        print(task_commands)

def decode_inputUser(inputUser):
    if inputUser == "biro":
        print("helloword")
decode_docs(inputUser, task_commands)
decode_inputUser(inputUser)



