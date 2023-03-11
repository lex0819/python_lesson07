# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)
# Вывод:
# same

# ordinary algoritmic resolve
def same_by1(characteristic, objects: object) -> bool:
    if len(objects) == 0:
        return True
    res = characteristic(objects[0])
    for object in objects:
        if characteristic(object) != res:
            return False
    return True


# resolve with map() and set() and len()
# map() returns array of results of characteristic(objects)
# if all are same that set() will contains only one item
def same_by(characteristic, objects: object) -> bool:
    return len(set(map(characteristic, objects))) == 1


values = [0, 2, 10, 6]
values1 = [1, 3, 11, 61, 2]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
