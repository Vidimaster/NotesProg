from model import Notes
import text
import view

def start():

    nb = Notes()

    while True:
        choice = view.main_menu()
        if choice == 1:
            nb.open_file()
            view.print_message(text.load_successful)
        elif choice == 2:
            nb.save_file()
            view.print_message(text.save_successful)
        elif choice == 3:
            view.show_notes(nb.notes2, text.empty_notes_error)
        elif choice == 4:
            new_note = view.input_note(text.input_note)
            nb.add_note(new_note)
            view.print_message(text.note_action(new_note[0], text.operation[0]))
        elif choice == 5:
            c_id = int(view.input_requset(text.input_note_id))
            new_note = view.input_note (text.input_edit_note)
            name = nb.edit_note(c_id, new_note)
            view.print_message (text.note_action(name, text.operation[1]))
        elif choice == 6:
            c_id = int(view.input_requset(text.input_del_note_id))
            name = nb.delete_note(c_id)
            view.print_message(text.note_action(name, text.operation[2]))
        elif choice == 7:
            view.print_message(text.exit_program)
            break


