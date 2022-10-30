import telephone_book as tb
import view


def writing_down():
    name = view.get_name()
    phone = view.get_number()
    action = view. what_to_do()
    for i in range(len(action)):
        if action[i] == 'новый контакт':            
            if name[i][0] not in tb.t_book:
                tb.create_new_list(name[i], tb.t_book)
            tb.create_new_note(name[i], tb.t_book, phone[i])
        elif action[i] == 'смена номера':
            tb.update_note(name[i], tb.t_book, phone[i])
        elif action[i] == 'дополнительный номер':
            tb.append_number(name[i], phone[i], tb.t_book)
        elif action[i] == 'удалить номер':
            tb.delete_note(name[i], tb.t_book)
    return tb.t_book
