from functions import get_todos,write_todos
import time
now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space characters from it.
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}-{todo}"
            todo = todo.title()
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()

            new_todo = input("Please enter a new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Your command is not valid:")
            continue



    elif user_action.startswith("complete"):
        try:
            completed_number = int(user_action[9:])
            todos = get_todos()

            index_num = completed_number - 1
            todo_to_remove = todos[index_num].strip('\n')
            todos.pop(index_num)
            write_todos(todos)


            message = f"Todo '{todo_to_remove}' removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number:")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("The command is not valid")

print("Bye")


