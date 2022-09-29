def user_data(data):
    '''
    вывод данных в консоль
    ''' 
    print(data)


def get_data(string):
    '''
    получение данных от пользователя
    '''
    return input(string)


def reading_menu():
    '''
    вывод справки меню в консоль
    '''
    with open('menu_start.txt', 'r', encoding='utf-8') as txtfile:
        for line in txtfile:
            print(line.rstrip())