# print("Hello World")
# print("IT RUN")
# print(10 + 30)
# print(3000 + 1234)
# print(50 - 23)
# print(10 * 20)
"""
Привет!!!
"""
# print(3 == 6)
# print(6 == 6)
# print(6 != 6)
# print(3 != 10)
# print(10 > 5)
# print(3 > 4)
# print(5 < 3)
# print(6 < 8)
# print(6 >= 3)
# print(9 >= 9)
# print(6 <= 6)
# print(6 <= 5)

# Переменные

# number = 55
# print(number)
# print(number + 5)

# name = "Sardor"
# print(name)
# surname = "Zahidov"
# print(surname)
# print(name + " " + surname)


# num_1 = int(input("Ведите первое число: ")) 
# num_2 = int(input("Ведите Второе число: ")) 
# if num_1 > num_2: 
#     print("Первое число больше второго") 
# else: 
#     print("Второе число больше первого") 
 
# num = int(input("Введите число: ")) 
# if num % 2 == 0: 
#     print(num, "чётное") 
# else:  
#     print(num, "нечётное") 
 
# num = int(input("Введите чило: ")) 
# if num == 10: 
#     print("Десять") 
# elif num == 20: 
#     print("Двадцать") 
# elif num == 100: 
#     print("Сто") 
# else: 
#     print("Если условия не совпали то срабатывает else") 
 
# num_1 = 500 
# num_2 = 40 
# num_3 = 57 
# if num_1 > num_2 and num_1 > num_3: 
#     print(num_1, "больше всех") 
# elif num_2 > num_1 and num_2 > num_3: 
#     print(num_2, "больше всех") 
# else: 
#     print(num_3, "больше всех") 
 
# password = input("Введите пароль: ") 
# confirm_password = input("Подтвердите пароль: ") 
# if password == "2020itrun" and confirm_password == "2020itrun": 
#     print("Welcome") 
# else: 
#     print("Error") 

# lst  = [1, 2, 3, 4,]
# print(lst)
# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# print(my_list)
# lst = [1, 2.0, True, "Hello", [1, 2, 3]]
# print(lst) 

# cars = ["BMW", "MERSEDES", "LEXUS", "LOTUS"]
# print(cars[::1]) Переворачиваем список
# print(cars[1:3]) Делаем срез списка от1 до 3
# cars.appened("TESLA")
# cars.appened("AUDI")Добавляем значение в конец списка с помошью метода appened
# cars.insert(0, "AUDI")Добавляем значение по индексу
# cars.pop(0)Удаляем из списка по индексу
# cars.remove("LEXUS")Удаляем из списка по значениям 
# print(cars)Выводим список cars
# del cars[0:3] Удаляем из списка с срезами с помошью оператора del
# print(cars)

# contacts = ["Sardor", "Adilet"]
# find_name = input("Введите имя которое вы хотите найти: ")
# if find_name.title() in contacts:
#     print("Контакт найден")
# else:
#     print("Не нашли")

# num_1 = int(input("Введите число: "))
# operation = input("+, -, *, /:")
# num_2 = int(input("Введите воторое число: "))
# if operation == "+":
#     print(num_1 + num_2)
# elif operation =="-":
#     print(num_1 - num_2)
# elif operation == "*":
#     print(num_1 * num_2)
# elif operation == "/":
#     print(num_1 / num_2)
# else:
#     print("Неправильная операция")
# 
# numbers = [0.1, 10, 1, 3, 5, 100, 500, 30, 40, 1200]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# data = () Создаём пустой катеж
# print(type(data)) Выводим тип объекта

# data = ("Summer", "Outumn", "Spring") Создаем список и превращаем его в картеж
# lst = list(data) С помощью встроенноёй функции tuple превращяем список в кортеж
# print(lst) Выводим кортеж

# tup = (1, 0.2, False, "Hello", [1, 2, 3], ("Hello")) Внутри кортеже можно хранить различные типы данных
# print(tup)

# tup_cars = ("BMW", "LEXUS", "LOTUS") Создаем кортеж машин
# tup_cars[2] = "TESLA" Пробуем обновить кортеж с помошью метода append
# tup_cars.append("Hello")
# print(tup_cars) 
# tup_cars.remove("BMW") Пробуем удалить значение катежа
# print(tup_cars)
##########################################
# lst_cars = ["BMW", "LEXUS", "LOTUS"]
# lst_cars[2] = "TESLA"
# print(lst_cars)
# lst_cars.append("MERSEDES")
# print(lst_cars)
# lst_cars.remove("BMW")
# print(lst_cars)


# num1 = 10
# num2 = 20
# if num1 == 10 or num2 == 10:
#     print("First")
# elif num1 == 20 or num2 == 20:
#     print("Second")
# else:
#     print("Error")

# number = int(input("Введите первое число: "))
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")
# ########################
# number = int(input("Введите число: "))
# res = "Четное" if number % 2 == 0 else "Не четное"
# print(res)

# number = int(input("Введите число: "))
# print("Четное") if number % 2 == 0 else print("Не четное")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# res = "Первое число больше" if num1 > num2 else "Второе число больше"
# print(res)

# number4 = int(input("Введите число: "))
# res = ("Нечетное", "Четное")[number % 2 == 0]
# print(res)

# num1 = 20000
# num2 = 400
# num3 = 1000
# result = "Первое число" if num1 > num2 and num1 > num3 else "Второе число" if num2 > num1 and num2 > num3 else "Третье"
# print(result)

#################################################################################################################################

# try: 
#         print(10 / 0) 
# except ZeroDivisionError: 
#         print("Деление на ноль") 
 
# try: 
#         print(10 + "10") 
# except TypeError: 
#         print("Ошибка типа неподдеоживаемые типы опреандов для +: 'int" и 'str'") 
 
# try: 
#         number1 = int(input("Введите первое число: ")) 
#         number2 = int(input("Введите второе число: ")) 
# except ValueError: 
#         print("Введите число!") 
 
# try: 
#         print(100 / 0) 
# except ZeroDivisionError: 
#         raise OSError("У вас ошибка в коде!") 
 
# try: 
#         print(100 / 1) 
# except ZeroDivisionError: 
#         print("Деление на ноль") 
# finally: 
        # print("Я все равно сработаю") 
# while True: 
#         try: 
#                 num1 = int(input("Введите первое число: ")) 
#                 operation = input("*, /, +, -: ") 
#                 num2 = int(input("Введите второе число: ")) 
#                 if operation == "+": 
#                         print(num1 + num2) 
#                 elif operation == "-": 
#                         print(num1 - num2) 
#                 elif operation == "*": 
#                         print(num1 * num2) 
#                 elif operation == "/": 
#                         try: 
#                                 print(num1 / num2) 
#                         except ZeroDivisionError: 
#                                 print("Деление на ноль") 
#                 else: 
#                         print("Неправильная операция") 
#         except ValueError: 
#                 print("Введите целое число!") 
 
# student = {'name' : 'Sardor', 'age' : 13} 
# print(student['age']) 
# student['age'] = 14 
# del student['age'] 
# print(student) 
# print(student.get('age')) 
# student.setdefault('key' , 'value') 
# student['hello'] = 'World' 
# print(student) 
# student_dct = dict(name = 'Sardor', age = 13) 
# print(student_dct)

# car = {'name' : 'Mersedes', 'year' : 2022, 'color' : 'black'} 
# print(car.keys()) #Метод keys() возвращает специальную коллекцию ключей в словаре. 
# print(car.values()) #Метод values() возвращает специальную коллекцию значений в словаре. 
# print(car.items()) #Метод items() возвращает пары<<ключ - значение>> в формате кортежей. 
# for key, value in car.items(): 
#         print(key, value)
#####################################################################################################################3

#a=[1,2,3,4,5]#Создаем первый список
#b=[2,3,4,5,6]#Создаем второй список
#c=a+b#Объединяем списки a и b
#print(set(c))#Выводим результат в типе данных set
#names={"Adilet","Kurmanbek","Sardor","Adilet"}#Создаем множество set
#print(names)#Выводим множество
#numbers={1,2,3,4,5,6,7,8,9,10}#Создаем множество из чисел
#print(numbers)#Выводим результат
#logic={1,1.0,True}#Создаем множество из одинаковых данных
#print(logic)#
#strange_app=set('TikTok')#
#print(strange_app)#
#pangram = {'съешь же ещё этих мягких французских булок, да выпей чаю'}
#print(pangram)
#cars=["Bmw","Mercedes","Tesla","Audi","Tesla"]
#set_cars=set(cars)
#print(set_cars)
#types={1,2.0,False,'1',(10,20,30)}
#print(types)
#some_dict = {'key_one': 'val_one', 'key_two': 'val_two'}
#some_set = set(some_dict)
#print(some_set)
#card_suit = ['heart', 'diamond', 'club', 'spade', 'spade']
#suit_set = set(card_suit)
#print(suit_set)

#unbreakable_diamond = ['Jotaro', 'Josuke', 'Koichi']
#golden_wind = ['Jotaro', 'Koichi', 'Giorno']
# & - здесь оператор пересечения
#overlap = set(unbreakable_diamond) & set(golden_wind)
#print(overlap)
#stats = {1.65, 2.33, 5.0}
#stats.add(14.7)
#print(stats)
#it_company={"Google","Tesla","Amazon"}
#it_company.add("Microsoft")
#print(it_company)

#it_company.remove("Google")
#print(it_company)
#it_company.pop()
#print(it_company)

#for i in it_company:
# print(i)
#it_company={"Google","Tesla","Amazon"}
#it_company.append("Microsoft")
#frzn_it=frozenset(it_company)
#print(type("frzn_it"))
#nums = []
#for num in range(1,101):
#  nums.append(num)
#print(nums)
######################################
#nums=[num for num in range (1,101)]
#print(nums)
#nums=[]
#for i in range (101):
# if i %2==0:
#  nums.append(i)
#print(nums)
######################################
#nums=[i for i in range (101)if i%2==0]
#print(nums)
#petrol={
# "Ai 100": 60,
# "Ai 95":55,
# "Ai 92":50,
# "Ai 80":40,
# "DT":35
#}

#new_petrol={}
#for name,price in petrol.items():
# new_petrol.setdefault(name,price+15)
#print(new_petrol)
#new_petrol={name:price+15 for name,price in petrol.items()}
#print(new_petrol)
###################################################################################

# def shor_word(word): 
#         word_split = word.split() 
#         new_lst = [] 
#         for i in word_split: 
#                 new_lst.append(i.title()[0]) 
#         res = "".join(new_lst) 
#         print(res) 
 
# shor_word("Кыргызская Ресрублика") 
# shor_word("Ruby on Rails") 
# shor_word("For your interest") 
 
# def count_word(word): 
#         word_split = word.split(",") 
#         str_split = "". join(word_split).lower() 
#         word_split = str_split.split() 
#         for i in set(word_split): 
#                 print(word_split.count(i), i) 
# count_word("Money, money, money, it's always sunny.") 
 
 
 
# def welcome(*names): 
#         for name in names: 
#                 print(name, "welcome") 
 
# welcome("Sardor", "Kurmanbek", "Adilet") 
# welcome(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
 
# def translate(**words): 
#         for key, value in words.items(): 
#                 print(key, value) 
# translate(USA = "США", Russia = "Россия", Kyrgyzstan = "Кыргызстан") 
 
####################
##########################
def add(num1, num2):
        print(num1 + num2)

def sub(num1, num2):
        print(num1 - num2)

it = "IT RUN"

def students(*names):
        print(names)