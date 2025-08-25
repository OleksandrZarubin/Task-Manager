import os 
import json
import random
import datetime

name_of_json = "tasks.json"
tasks = {}


def main():
    while True:
        print("1 - Add a task")
        print("2 - Show all tasks")
        print("3 - Delete a task")
        print("4 - Exit")
        print("\n\n5 - Additional options")
        choice = int(input("Choose an options:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            show_all_task()
        elif choice == 3:
            delet_task()
        elif choice == 4:
            break
        elif choice == 5:
            main2()
        else:
            print("Invalid option. Please try again.")


def main2():
    while True:
        print("1 - Change task status")
        print("2 - Search task by name or id")
        print("3 - Filter tasks by status")
        print("4 - Go back to main menu")
        choice = int(input("Choose an options:"))
        if choice == 1:
            change_status()
        elif choice == 2:
            search_task()
        elif choice == 3:
            filtred_task()
        elif choice == 4:
            return main()
        else:
            print("Invalid option. Please try again.")
            return main2()

def back_to_menu():
    print("1 - Go back to main menu")
    print("2 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        main()
    elif option == "2":
        exit()
    else:
        print("Invalid option. Returning to main menu.")
        return main()

def add_task():
    myuuid = random.randint(1, 10)
    print(f'Okay, your task was created with ID:{myuuid},\nnow please enter tasks details')
    name_of_task = input("Enter task name: ")
    description_of_task = input("Enter task description: ")
    task ={
        "id": str(myuuid),
        "name": name_of_task,
        "description": description_of_task,
        "status": "incomplete",
        "created_at": str(datetime.datetime.now())
    }
    tasks[f"Task with ID: {myuuid}"] = task
    print("Your yask was added with status 'incomplete'")


    a = str(input("Do you change status? (y/n):")).lower()
    if a == "y":
        us_status = str(input("Enter new status (complete/incomplete/inprogress):")).lower()
        if us_status == "complete" or us_status == "incomplete" or us_status == "inprogress":
            task["status"] = us_status
            print(f"Status was changed to {us_status}")
        elif us_status == "n":
            print("Status remains 'incomplete'")
            back_to_menu()
        else:
            print("Invalid status. Status remains 'incomplete'")
    else:
        print("Invalid input. Status remains 'incomplete'")


    if os.path.exists(name_of_json):
        with open(name_of_json, "r") as f:
            data = json.load(f)
            data.update(tasks)
        with open(name_of_json, "w") as f:
            json.dump(data, f, indent = 4)
    else:
        with open(name_of_json, "w") as f:
            json.dump(tasks, f, indent = 4)
    print("Okay, your task was saved in tasks.json")
    print("You can see it, by choosing option 2 in main menu")
    back_to_menu()
    

def show_all_task():
    if os.path.exists(name_of_json):
        data = json.load(open(name_of_json))
        for task in data:
            tasks = data[task]
            print(f"ID: {tasks['id']} | Name: {tasks['name']} | Status: {tasks['status']}")
        back_to_menu()
    else:
        print("No tasks found.")
        back_to_menu()


def delet_task():
    if os.path.exists(name_of_json):
        data = json.load(open(name_of_json))
        task_id = int(input("Enter ypu task ID: "))
        for task in data:
            tasks = data[task]
            if tasks['id'] == str(task_id):
                print(f'Your task with ID: {task_id} was found')
                confirm = int(input("Are you sure to want to delete it? (1 - Yes, 2 - No): "))
                if confirm == 1:
                    del data[task]
                    with open(name_of_json, "w") as f:
                        json.dump(data, f, indent = 4)
                    print("Task was deleted.")
                    return back_to_menu()
                elif confirm == 2:
                    print("Task was not deleted.")
                    back_to_menu()
                else:
                    print("Invalid option. Task was not deleted.")
                    back_to_menu()


def change_status():
    print("Change Task Status")
    task_id = input("Enter task ID to change status: ")
    new_status = input("Enter new status (complete/incomplete/inprogress): ").lower()
    if new_status in ["complete", "incomplete", "inprogress"]:
        if os.path.exists(name_of_json):
            with open(name_of_json, "r") as f:
                data = json.load(open(name_of_json))
                for tasks in data:
                    task = data[tasks]
                    if task['id'] == task_id:
                        task['status'] = new_status
                        with open(name_of_json, "w") as f:
                            json.dump(data, f, indent = 4)
                        print(f"Task ID {task_id} status changed to {new_status}.")
                return back_to_menu()
        else:
            print("No tasks found.")
            return back_to_menu()
                
def search_task():
    print("Search task by name of ID")
    mod = int(input("Choose search mode (1 - by name, 2 - by ID): "))
    if mod == 1:
        name = input("Enter task name: ")
        if os.path.exists(name_of_json):
            with open(name_of_json, "r") as f:
                data = json.load(open(name_of_json))
                for tasks in data:
                    task = data[tasks]
                    if task["name"].lower() == name.lower():
                        print("Your task was found\n Here is it:")
                        print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")
                return back_to_menu()
        else:
            print("No tasks found.")
            return back_to_menu()
        

    elif mod == 2:
        id = input("Enter task ID: ")
        if os.path.exists(name_of_json):
            with open(name_of_json, "r") as f:
                data = json.load(open(name_of_json))
                for tasks in data:
                    task = data[tasks]
                    if task["id"] == id:
                        print("Your task was found\n Here is it:")
                        print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")
                return back_to_menu()
        else:
            print("No tasks found.")
            return back_to_menu()
        



def filtred_task():
    print("Filter tasks by status")
    enter_status = input("Enter status to filter by (complete/incomplete/inprogress): ")
    if enter_status in ["complete", "incomplete", "inprogress"]:
        if os.path.exists(name_of_json):
            with open(name_of_json, "r") as f:
                data = json.load(open(name_of_json))
                for tasks in data:
                    task = data[tasks]
                    if task["status"].lower() == enter_status.lower():
                        print(f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']}")
                return back_to_menu()
        else:
            print("No tasks found.")
            return back_to_menu()

if __name__ == "__main__":
    main()