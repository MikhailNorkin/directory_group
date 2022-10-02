<<<<<<< HEAD
import contact_actions as ca
import contact_guide as cg

import user_interface as ui
=======
import user_interface as ui
import contact_actions as ca
import os
os.system("cls")


def button_click():
    '''
    Запуск и отработка приложения.
    '''
    operation = ui.get_operation()
    if operation == 1:
        result = ca.open_phonebook()
    elif operation == 2:
        result = ca.add_contact()
    elif operation == 3:
        data = ui.input_text()
        print('Функция в стадии разработки.')
    elif operation == 4:
        data = ui.input_text()
        result = ca.find_contact(data)
    elif operation == 5:
        print('Функция в стадии разработки.')
    elif operation == 6:
        print('Функция в стадии разработки.')
    # ui.view_result(result)
>>>>>>> d8fc36276e55be83aca1ef67d8b32d868f6596c6
