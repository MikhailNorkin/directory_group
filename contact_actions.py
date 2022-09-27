import csv

# def add_contact():
#     '''
#     Добавление контакта 
#     '''
#     with open("contacts.csv", encoding='utf-8') as data:
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

# add_contact()

with open('contacts.csv', newline = '', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row['Имя'], row['Тип_телефона'], row['Номер_телефона'], row['Комментарий'])

        


        