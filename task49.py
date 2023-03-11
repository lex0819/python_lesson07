# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


# number pi is not needed because it doesn't need for comparesion, we need only r1*r2
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(orbits)


def find_farthest_orbit_ordinary(list_of_orbits: list) -> tuple:
    max_square = 0
    max_ind = 0
    for i in range(len(list_of_orbits)):
        if list_of_orbits[i][0] != list_of_orbits[i][1]:
            square = list_of_orbits[i][0] * list_of_orbits[i][1]
            if max_square < square:
                max_square = square
                max_ind = i
    return list_of_orbits[max_ind]


def find_farthest_orbit(list_of_orbits: list) -> tuple:
    return max(list_of_orbits, key=lambda r: r[0] != r[1] and r[0] * r[1])


print(*find_farthest_orbit(orbits))
