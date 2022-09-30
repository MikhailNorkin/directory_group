import controller as c
from colorama import *

while True:
    print(Fore.BLACK + Back.CYAN)
    out_input = input(
        'Если хотите поработать со справочником, нажмите что угодно, кроме "q", + Enter.\nЕсли хотите завершить работу, введите "q" на клавиатуре + Enter. \n')
    if out_input == 'q':
        print(Fore.BLACK + Back.MAGENTA +
              'Спасибо, что выбрали наше приложение! Заходите еще!!!')
        break
    else:
        c.button_click()
