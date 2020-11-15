import os
import datetime

"""
fUNCTIONALITY:
-Register products
    -id(auto)
    -title
    -category
    -stock
    -price
    
COMMENT MULTIPLE LINES

 def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("clear")
"""


def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y %H:%M")


def print_product_info(prod):
    print(
        str(prod.id).ljust(3) + " | " +
        prod.title.ljust(25) + " | " +
        prod.category.ljust(25) + " | " +
        str(prod.stock).ljust(3) + " | $" +
        str(prod.price).ljust(3)
    )


def clear2():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system("clear")

    # return os.system('cls' if os.name== 'nt' else 'clear;)


def print_menu():
    print('*'*50)
    print('Welcome - WareHouse ['+get_date_time()+']')
    print('*'*50)

    print('[1] Add product to Catalog')
    print('[2] Display Catalog')
    print('[3] Display Products out of stock')
    print('[4] Total stock value')
    print('[5] Cheapest products')
    print('[6] Delete product')

    print('[7] Update product')
    print('[8] Update stock')
    print('[9] Update price')

    print('[10] 3 high prices')
    print('[11] Disctinct categories')

    print('[x] Exit')

    print('-'*20)  # repeat the char


def print_header(text):
    clear2()
    print('*'*50)
    print(text)
    print('*'*50)
