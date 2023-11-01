import text

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print (f'\t{i}. {item}')
    while True:
        choice = input (text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print (text.input_menu_error)

def print_message(msg: str):
    print ('\n' + '='*len(msg))
    print(msg)
    print ('='*len(msg)+'\n')

def show_notes(notes, msg: str):
    if notes:
        print('\n' + '*' * 67)
        for i, note in notes.items():
            print(i, "->", note)
        print('*' * 67 + '\n')
    else:
        print_message(msg)

def input_note(msg: str):

    note = []
    for input_text in msg:
        note.append(input(input_text))
    return note
   
def input_requset(msg: str) -> str:
    return input(msg)