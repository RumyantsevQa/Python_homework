# Распаковка
# Используется для того, чтобы распределить элементы коллекции (список, словарь, множество, кортеж) по отдельным переменным.
# Используется только в ситуациях, когда вы наверняка знаете количество элементов, содержащихся в коллекции.

# my_list = [1, 3]
# my_tuple = (2, 6, 9)
#
# a, b = my_list
# c, d, e = my_tuple
# print(a, b, c, d, e)


# Срез
# Извлечение среза позволяет взять из списка определенную его часть.

# lll = [1, 3, 5, 7, 8, 11, 9]
# print(lll)
# print(lll[1:4])
# print(lll[:2])
# print(lll[3:])
# print(lll[1::2])
# print(lll[:])
# print(lll[::-1])
# print(lll[::-2])
# print(lll[-2:-6:-1])


# Методы строк
# Со строкой можно делать многое из того, что можно делать с другими коллекциями, т.к. строка это по сути тоже коллекция - последовательность символов.
# Больше всего функциональность строки похожа на функциональность кортежей.

# text = 'my long long string'
# print(text[3])
# print(len(text))
# print(text.index('long'))
# print('long' in text)
# print(text.count('long'))
# print(text.find('long'))
# print(text[3:-6])
# print(text.startswith('my'))
# print(text.endswith('string'))

# txt = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
# print(txt.capitalize()) #Делает первую букву предложения заглавной
# print(txt.title()) #Делает каждую первую букву заглавной
# print(txt.upper()) #Делает все буквы большими
# print(txt.lower()) #Делает все буквы маленькими

text = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
string_index = text.index('CaPITalIZatiOn')
print(text[:string_index].lower() + text[string_index:].upper())