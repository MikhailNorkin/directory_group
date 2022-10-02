import controller as c
<<<<<<< HEAD
 
c.button_click()
=======
from colorama import *

while True:
    print(Fore.BLACK + Back.CYAN)
    out_input = input(
        'Если хотите поработать со справочником, нажмите что угодно (кроме "0"), + Enter.\nЕсли хотите завершить работу, введите "0" на клавиатуре + Enter. \n')
    if out_input == '0':
        print(Fore.BLACK + Back.MAGENTA +
              'Спасибо, что выбрали наше приложение! Заходите еще!!!')
        break
    else:
        c.button_click()
>>>>>>> d8fc36276e55be83aca1ef67d8b32d868f6596c6
