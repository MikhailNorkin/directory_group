import csv

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
    запись в файл
    '''
    surname = write_unit("Введите фамилию: ")
    names = write_unit("Введите имя: ")
    patronymic = write_unit("Введите отчество: ")
    tel_type = write_tel_type("Введите тип номера телефона (1,2,3): ");
    tel_number = write_unit("Введите номер телефона: ")
    tel_comment = write_unit("Введите комментарий: ")
    type_dict = {'Сотовый' : 1, 'Рабочий' :2, 'Домашиний':3}

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
            if surname == surname_found and names == names_found and patronymic == patronymic_found and type_dict[tel_type] == type_dict[row["Тип"]]\
            and tel_number == tel_number_found:
                print("Такая запись существует")
            count += 1    

        # print(f'Всего в файле {count + 1} строк.')




    # with open('contacts.csv', 'a', newline='', encoding='utf-8') as csvfile:

    #     writer.writerow([surname, names, patronymic, tel_type, tel_number, tel_comment])

add_contact()
