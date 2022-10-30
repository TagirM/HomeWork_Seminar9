from argparse import Action


name = []
phone = []
action = []
t_book = {}


def init(person_name, number):
    global name
    global phone
    global action
    name = person_name
    phone = number


def create_new_note(person_name: list, note: dict, number: list):
    note[person_name] = number
    return note


def create_new_list(person_name: list, book: dict):
    book[person_name[0]] = ''

    return book


def update_note(person_name: list, note: dict, number: list):
    note[person_name] = number
    return note


def delete_note(person_name: list, note: dict):
    del note[person_name]
    return note


def append_number(person_name: list, number: list, note: dict):
    note[person_name] = note.get(person_name, []) + ' ' + number    
    return note
