import json


def fetch_all_todo():
    try:
        with open("todo.txt","r") as todoList:
            return json.load(todoList)
    except FileNotFoundError:
        return []

def save_to_file_helper(todoList):
    with open("todo.txt","w") as file:
        json.dump(todoList,file)


def list_all_todo(todoList):
    print("\n")
    print("*" *70)
    if todoList:
        for serial, todo in enumerate(todoList, start=1):
            print(serial,".", todo.get("todo")," status ",todo.get("status"))
    print("\n")
    print("*" *70)

def add_todo(todoList):
    add_todo = input("Enter a Todo- ")
    todoList.append({"todo":add_todo, "status":"Created"})
    save_to_file_helper(todoList)

def update_todo(todoList):
    list_all_todo(todoList)
    update_serial = int(input("Enter the todo to be updated "))
    todo_status = input("Enter the status of the todo ")
    todo_name = todoList[update_serial-1].get("todo")
    if(1<=update_serial<=len(todoList)):
        todoList[update_serial -1] = {"todo": todo_name,"status": todo_status}
        save_to_file_helper(todoList)
    else:
        print("invalid todo list number")

def delete_todo(todoList):
    list_all_todo(todoList)
    del_todo = int(input("Enter the number to delete a todo "))
    if(1<=del_todo<=len(todoList)):
        del todoList[del_todo -1]
        save_to_file_helper(todoList)
    else:
        print("invalid todo list number")
    

def main():
    while True:
        print("\n TODO Manager  | Choose an option from down below")
        print("1. List all TODO ")
        print("2. Add a TODO in the list ")
        print("3. Update a TODO in the list ")
        print("4. Delete a TODO ")
        print("5. Exit the application ")
        print("\n")
        input_choice = input("Enter your choice ")
        todoList = fetch_all_todo()
        match input_choice:
            case "1":
                list_all_todo(todoList)
            case "2":
                add_todo(todoList)
            case "3":
                update_todo(todoList)
            case "4":
                delete_todo(todoList)
            case "5":
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()

    
