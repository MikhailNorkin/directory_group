import csv
from io import UnsupportedOperation
import user_interface as ui
from dictionaries import dict_field as d1
from dictionaries import dict_translate as d2
import os
import check as ch
from colorama import *
init()


def add_contact():
    '''
    Добавление контакта в новую строку.
    Первая строка - строка заголовков столбцов.
    Предусмотрены случаи:
    отсутствия файла, пустого файла, уже заполненного файла.
    '''
    ui.print_instructions_for_input()
    string_in_file, header = [], []
    for i in range(1, 7):
        header.append(d2[d1[i]])
        if i == 1 or i == 2:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]))
        if i == 3:
            f = ch.check_textfield(ui.input_data(
                d2[d1[i]]), 0)
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
