# Преобразование типов данных

a = '1'
print(type(a))

a = int(a)
print(type(a))

user_input = int(input("Enter a number: "))
print(user_input)
print(type(user_input))


#  Типы данных в Python
# Number (целое число)
# String (строка)
# Boolean (логический тип данных)
# Float (числа с плавающей точкой)
# List (список)
# Dictionary (словарь)
# Tuple (кортеж)
# Set (множество)


# List - список - структура данных для хранения последовательностей.
# Экземпляры значений, находящихся в списке, называются элементами списка.

my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last']
print(my_list[6])
print(my_list[-1])
print(my_list[-3])

my_list[2] = 42
print(my_list)

my_list = []
my_list.append(8)
my_list.append(7)
my_list.append('text')
print(my_list)
print(len(my_list))
print(my_list.index(8))
poped = my_list.pop(0)
print(poped)

print(8 in my_list)


# Картежи - Хранят данные различных типов
# Неизменяемы
# Занимают меньший размер
# Оптимизируются интепретатором
# По поведению похожи на списки. Главное отличие - нет функций, позволяющих что-то добавить в кортеж или изменить внутри него

my_tuple = (1, 3, 6, 3, None, 'text', False, 2.42)
print(my_tuple.count(3)) #посчитает сколько объектов (например 3) есть в картеже, ответ 2 шт.


# Dictionary(словари)

my_dict = {'key': 'value', 'two': 'value2', 'three': 3} #ключ: значение
print(my_dict['key'])
print(len(my_dict)) #скажет сколько объектов в словаре

rrrt