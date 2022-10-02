import csv
from io import UnsupportedOperation
import user_interface as ui
from dictionaries import dict_field as d1
from dictionaries import dict_translate as d2
import os
import re
import check as ch
from colorama import *
init()


# def add_contact():
#     '''
#     Добавление контакта 
#     '''
#     with open("classmates.csv", encoding='utf-8') as data:
#         # Создаем объект DictReader, указываем символ-разделитель ","
#         file_reader = csv.DictReader(data, delimiter = ",")
#         # Счетчик для подсчета количества строк и вывода заголовков столбцов
#         count = 0
#         # Считывание данных из CSV файла
#         for row in file_reader:
#             if count == 0:
#                 # Вывод строки, содержащей заголовки для столбцов
#                 print(f'Файл содержит столбцы: {", ".join(row)}')
#             # Вывод строк
#             print(f' {row["Имя"]} - {row["Успеваемость"]}', end='')
#             print(f' и он родился в {row["Год рождения"]} году.')
#             count += 1
#         print(f'Всего в файле {count + 1} строк.')



# <<<<<<< HEAD
# # Чтение из файла (Открыть контакт) ? как открыть выборочно?
# def reading_contact():
#     '''
#     чтение из файла
#     '''
#     with open('contacts.csv', newline = '', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile, delimiter=',')
#         for row in reader:
#             print(row['id'], row['Фамилия'], row['Имя'], row['Отчество'], row['Тип_телефона'], row['Номер_телефона'], row['Комментарий'])
# =======
# # # Чтение из файла (Открыть контакт) ? как открыть выборочно?
# # def reading_contact():
# #     with open('contacts.csv', newline = '', encoding='utf-8') as csvfile:
# #         reader = csv.DictReader(csvfile, delimiter=',')
# #         for row in reader:
# #             print(row['id'], row['Фамилия'], row['Имя'], row['Отчество'], row['Тип_телефона'], row['Номер_телефона'], row['Комментарий'])
# =======

# >>>>>>> e17b9ca35e10253cc8e6d2c3c06a93fb57f9a514

        
# Запись в файл (Добавить контакт) ? Добавить id контакта и пустые вводы
def write_unit(txt):
    element = input(txt)
    return element

def write_tel_type(txt):
    type_dict = {1: 'Сотовый', 2: 'Рабочий', 3: 'Домашиний'}
    for item in type_dict.items():
        print(item)    
    element = int(input(txt))
    return type_dict[element]




def add_contact():
    '''
<<<<<<< HEAD
    запись в файл
    '''
    surname = write_unit("Введите фамилию: ")
    names = write_unit("Введите имя: ")
    patronymic = write_unit("Введите отчество: ")
    tel_type = write_tel_type("Введите тип номера телефона (1,2,3): ");

    type_dict = {'Сотовый' : 1, 'Рабочий' :2, 'Домашиний':3}

    #Проверяем есть ли такой человек и тип телефона в справочнике
    with open('contacts.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(csvfile, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            # Вывод строк
            surname_found = row["Фамилия"]
            names_found = row["Имя"]
            patronymic_found = row["Отчество"]
            tel_type_found = type_dict[row["Тип"]]
            tel_number_found = row["Телефон"]
            if surname == surname_found and names == names_found and patronymic == patronymic_found and type_dict[tel_type] == type_dict[row["Тип"]]:
                print("Такая запись существует")
            count += 1    
    #tel_number = write_unit("Введите номер телефона: ")
    #tel_comment = write_unit("Введите комментарий: ")

        # print(f'Всего в файле {count + 1} строк.')



=======
    Добавление контакта в новую строку.
    Первая строка - строка заголовков столбцов.
    Предусмотрены случаи:
    отсутствия файла, пустого файла, уже заполненного файла.
    '''
    ui.print_instructions_for_input()
    string_in_file, header = [], []
    for i in range(1, 7):
        header.append(d2[d1[i]])
        if i == 1:
            text = ui.input_data(d2[d1[i]])
            if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) != None:
                f = ch.check_double_surname(text)
            if re.match('^[а-яёА-ЯЁ]{2,}[-][а-яёА-ЯЁ]{2,}$', text) == None:
                f = ch.check_textfield(text)
                f = str(f).capitalize()
        if i == 2:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]))
            f = str(f).capitalize()
        if i == 3:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]), 0)
            f = str(f).capitalize()
        if i == 4:
            f = ch.remove_spaces_in_string(ui.input_data(d2[d1[i]]))
            f = ch.check_mobile(f)
        if i == 5:
            f = ch.remove_spaces_in_string(ui.input_data(d2[d1[i]]))
            f = ch.check_homephone(f)
        if i == 6:
            f = ch.check_free_textfield(ui.input_data(
                d2[d1[i]]))
            f = str(f).capitalize()
        string_in_file.append(f)
    try:
        open('contacts.csv')
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            if os.stat('contacts.csv').st_size != 0:
                file_writer.writerow(string_in_file)
            elif os.stat('contacts.csv').st_size == 0:
                file_writer.writerow(header)
                file_writer.writerow(string_in_file)
    except (FileNotFoundError, UnsupportedOperation):
        with open('contacts.csv', 'a', encoding='utf-8') as phonebook:
            file_writer = csv.writer(
                phonebook, delimiter='|', lineterminator="\r")
            file_writer.writerow(header)
            file_writer.writerow(string_in_file)


def find_contact(data):
    '''
    Поиск контакта по имени / фамилии.
    '''
    line = []
    count = 0
    try:
        open('contacts.csv')
        with open('contacts.csv', encoding='utf-8') as phonebook:
            file_reader = csv.reader(phonebook, delimiter='|')
            for row in file_reader:
                if data.capitalize() in row:
                    count += 1
                    line.append(row)
                    print(row)
            if count == 0:
                print('Нет совпадений.')
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонная книга пуста, поэтому Вы не можете ее открыть!')
    return line


def open_phonebook():
    '''
    Функция открывает файл с контактами (если он есть) и выводит список в консоль.
    '''
    try:
        open('contacts.csv')
        with open('contacts.csv', encoding='utf-8') as phonebook:
            file_reader = csv.reader(phonebook, delimiter='|')
            for row in file_reader:
                if len(row) > 0:
                    print(row)
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонной книги нет - Вы не можете ее открыть!')
>>>>>>> d8fc36276e55be83aca1ef67d8b32d868f6596c6

    # with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:

<<<<<<< HEAD
    #     writer.writerow([surname, names, patronymic, tel_type, tel_number, tel_comment])

add_contact()
=======
def delete_contact(data):
    '''
    Фунция удаляет найденный контакт. НЕ ДОРАБОТАНА!!!
    '''
    try:
        open('contacts.csv')
        search_line = find_contact(data)
        if len(search_line) == 1:
            print(Fore.BLACK + Back.MAGENTA +
                  f'Найдено 1 совпадение:\n{search_line}\n')
            operation = ui.confirm_operation()
            if operation == '1':
                print(1)
            if operation == '2':
                print(Fore.BLACK + Back.MAGENTA +
                      'Вы отказались от удаления записи. Переходим в основное меню.')
        if len(search_line) > 1:
            for i in range(0, len(search_line)):
                print(Fore.BLACK + Back.MAGENTA + 'Больше одной строки')
                print(f'№ {i+1} - {search_line[i]}')
            line_del = input(
                'Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
            flag = False
            while flag == False:
                try:
                    int(line_del)
                    if int(line_del) > 0:
                        if int(line_del) < len(search_line):
                            print(1)
                            flag = True
                    else:
                        print(Fore.GREEN + Back.RED)
                        line_del = input(
                            'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
                except ValueError:
                    print(Fore.GREEN + Back.RED)
                    line_del = input(
                        'Неверно указан номер строки! Введите номер строки, которую хотите удалить (из тех, что вышли на экран - укажите просто цифру).\n')
    except FileNotFoundError:
        print(Fore.GREEN + Back.RED +
              'Телефонная книга пуста, поэтому удалять нечего!')


# delete_contact('Дарья')
>>>>>>> d8fc36276e55be83aca1ef67d8b32d868f6596c6
