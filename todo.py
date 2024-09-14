"""
### ToDo Notes Project

This project demonstrates a simple ToDo Notes application. Users can:
- Add notes
- View notes
- Delete notes
- Exit the application

---

#### Key Features:
- A menu-driven interface to interact with the user.
- List-based storage for notes.
"""

# Class to manage ToDo Notes
class ToDo:
    def __init__(self):
        self.notes = []  # List to store notes

    # Method to add a note
    def add_note(self, note):
        self.notes.append(note)
        print(f'Note added: "{note}"')

    # Method to view all notes
    def view_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("\nYour ToDo Notes:")
            for i in range(len(self.notes)):
                print(f"{i+1}. {self.notes[i]}")

    # Method to delete a note by its index
    def delete_note(self, index):
        if index <= 0 or index > len(self.notes):
            print("Invalid note number!")
        else:
            removed_note = self.notes.pop(index - 1)
            print(f'Removed note: "{removed_note}"')

# Function to interact with the user
def todo_notes_app():
    todo = ToDo()

    while True:
        # Display menu
        print("\nToDo Notes Menu:")
        print("1. Add a Note")
        print("2. View Notes")
        print("3. Delete a Note")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        # Perform actions based on user choice
        if choice == '1':
            note = input("Enter your note: ")
            todo.add_note(note)
        elif choice == '2':
            todo.view_notes()
        elif choice == '3':
            todo.view_notes()
            if todo.notes:
                note_index = int(input("Enter the number of the note to delete: "))
                todo.delete_note(note_index)
        elif choice == '4':
            print("Exiting ToDo Notes app. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

# Run the ToDo Notes app
todo_notes_app()
