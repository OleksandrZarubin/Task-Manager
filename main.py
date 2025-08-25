import json
import random
import os
import sys




name_file = "notes.json"
json_notes = {
    "notes": []
}


def main():
    while True:
        print("1 - Add a note")
        print("2 - Show all notes")
        print("3 - Delete a note")
        print("4 - Exit")
        choice = int(input("Choose any options: "))
        if choice == 1:
            add_note()
            print("5 - To continue")
            print("6 - To exit")
            choice2 = int(input("Choose any options: "))
            if choice2 == 5:
                continue
            elif choice2 == 6:
                break
            else:
                print("Invalid choice, please try again.")
                continue

        elif choice == 2:
            show_notes()
            print("5 - To continue")
            print("6 - To exit")
            choice2 = int(input("Choose any options: "))
            if choice2 == 5:
                continue
            elif choice2 == 6:
                break
            else:
                print("Invalid choice, please try again.")
                continue

        elif choice == 3:
            delete_note()
            print("5 - To continue")
            print("6 - To exit")
            choice2 = int(input("Choose any options: "))
            if choice2 == 5:
                continue
            elif choice2 == 6:
                break
            else:
                print("Invalid choice, please try again.")
                continue

        elif choice == 4:
            exit_program()
            break
        else:
            print("Invalid choice, please try again.")
            continue


def add_note():
    note = input("Enter your note:")
    id = random.randint(1, 10)
    print(f'Your note has been added with ID:{id}')
    json_notes["notes"].append({"id": id, "note": note})

    with open(name_file, "w") as file:
        json.dump(json_notes, file)


def show_notes():
    with open(name_file, "r") as file:
        data = json.load(file)
        for note in data["notes"]:
            print(f'ID: {note["id"]}, Note: {note["note"]}')


def delete_note():
    id_delete = int(input("Enter yout note id to delte: "))
    for note in json_notes["notes"]:
        if note["id"] == id_delete:
            json_notes["notes"].remove(note)
            print(f'Note with ID:{id_delete} has been deleted.')
            with open(name_file, "w") as file:
                json.dump(json_notes, file)
        else:
            print(f'Note with id:{id_delete} not found')
            return


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


if __name__ == "__main__":
    main()
