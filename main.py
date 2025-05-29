# def add_new_task(inputUser):
import json
from errno import ELOOP

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

# task_list_commands = ["add", "update", "delete", "mark-in-progress", "mark-done"]
#
# task_commands = {
#     "add": "Adiciona uma nova tarefa",
#     "update": "Atualiza uma tarefa existente",
#     "delete": "Remove uma tarefa",
#     "mark-in-progress": "Marca a tarefa como em andamento",
#     "mark-done": "Marca a tarefa como concluída",
#     "list": "Lista todas as tarefas",
#     "list done": "Lista tarefas concluídas",
#     "list todo": "Lista tarefas pendentes",
#     "list in-progress": "Lista tarefas em andamento"
# }
# task_actions = {
#     "add": "Adiciona uma nova tarefa",
#     "update": "Atualiza uma tarefa existente",
#     "delete": "Remove uma tarefa",
#     "mark-in-progress": "Marca a tarefa como em andamento",
#     "mark-done": "Marca a tarefa como concluída",
# }
#
#
# # def add_task(task_list_commands):
# #     print()
# def decode_inputUser(inputUser):
#         print(inputUser)
#         print(type(inputUser))
#
#
#
#
# def decode_docs(inputUser, task_commands):
#     if inputUser == "docs":
#         print("\nAvailable commands:")
#         print(json.dumps(task_commands, indent=4, ensure_ascii=False))
#
#
#
# while True:
#     inputUser = input("Welcome to task-cli(type 'exit' to quit):")
#     if inputUser == 'exit':
#         print("exiting")
#         break
#
#     decode_docs(inputUser, task_commands)
#     decode_inputUser(inputUser)
#
#

# while True:
#     inputUser = input("task-cli: ")
#     inputUser.
#     print(inputUser)
#     print(inputUser[0])
#     print(type(inputUser))
#     if inputUser == 'exit':
#         print("exiting")
#         break
#

# import shlex
#
# def decode_input(tokens):
#     if not tokens:
#         return
#
#     command = tokens[0]
#
#     if command == "add":
#         description = tokens[1]
#         print(f"[ADD] Nova tarefa: {description}")
#
#     elif command == "update":
#         if len(tokens) < 3:
#             print("Uso correto: update <id> <nova descrição>")
#             return
#         task_id = tokens[1]
#         new_description = tokens[2]
#         print(f"[UPDATE] ID: {task_id} -> {new_description}")
#
#     elif command == "delete":
#         task_id = tokens[1]
#         print(f"[DELETE] Removendo tarefa ID: {task_id}")
#
#     elif command == "list":
#         if len(tokens) == 1:
#             print("[LIST] Todas as tarefas")
#         else:
#             status = tokens[1]
#             print(f"[LIST] Tarefas com status: {status}")
#
#     else:
#         print(f"Comando não reconhecido: {command}")
#
# # Loop principal
# while True:
#     user_input = input("task-cli > ")
#     if user_input.strip() in ["exit", "quit"]:
#         print("Saindo...")
#         break
#
#     try:
#         tokens = shlex.split(user_input)
#         decode_input(tokens)
#     except Exception as e:
#         print(f"Erro ao processar comando: {e}")
#

# entrada = input ("task-cli >")
#
# if '"' in entrada:
#     comeco = entrada.find('"')
#     fim = entrada.rfind('"')
#     texto = entrada[comeco+1:fim]
# print(texto)
#
# antes = entrada[:comeco].strip().split()
# comando = antes[0]  # Ex: "add"
# resto = antes[1:]   # Ex: []
#
# print(comando)
def parse_input(entrada):
    entrada = entrada.strip()

    # Caso tenha aspas (texto da tarefa com espaços)
    if '"' in entrada:
        aspas_inicio = entrada.find('"')
        aspas_fim = entrada.rfind('"')
        texto = entrada[aspas_inicio + 1:aspas_fim]  # entre aspas
        partes = entrada[:aspas_inicio].strip().split()
    else:
        texto = None
        partes = entrada.split()

    method = partes[0] if len(partes) > 0 else None
    id_ = int(partes[1]) if len(partes) > 1 and partes[1].isdigit() else None

    return {
        "method": method,
        "id": id_,
        "text": texto
    }


while True:
    entrada = input("task-cli > ")

    if entrada.lower() == "exit":
        print("Saindo...")
        break

    comando = parse_input(entrada)

    method = comando["method"]
    id_ = comando["id"]
    text = comando["text"]

    if method == "add":
        print(f"[ADD] Nova tarefa: {text}")
    elif method == "update":
        print(f"[UPDATE] ID: {id_} -> {text}")
    elif method == "delete":
        print(f"[DELETE] Removendo tarefa com ID {id_}")
    elif method == "mark-done":
        print(f"[MARK DONE] Marcando tarefa {id_} como concluída")
    elif method == "list":
        print("[LIST] Listando tarefas...")
    else:
        print("[ERRO] Comando não reconhecido.")
