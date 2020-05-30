# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def draw_triangle(point_bottom_left, angle=0, length=100):
    width = 3
    figure_angle = 360 / 3
    v1 = None
    for i in range(3):
        if v1:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length, width=width)
            v1.draw()
        else:
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw()


def draw_square(point_bottom_left, angle=0, length=100):
    width = 3
    figure_angle = 360 / 4
    v1 = None
    for i in range(4):
        if v1:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length, width=width)
            v1.draw()
        else:
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw()


def draw_pentagon(point_bottom_left, angle=0, length=100):
    width = 3
    figure_angle = 360 / 5
    v1 = None
    for i in range(5):
        if v1:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length, width=width)
            v1.draw()
        else:
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw()


def draw_hexagon(point_bottom_left, angle=0, length=100):
    width = 3
    figure_angle = 360 / 6
    v1 = None
    for i in range(6):
        if v1:
            v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length, width=width)
            v1.draw()
        else:
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw()


point1 = sd.get_point(50, 50)
point2 = sd.get_point(380, 50)
point3 = sd.get_point(150, 380)
point4 = sd.get_point(450, 380)
point5 = sd.get_point(200, 200)
# draw_triangle(point1, 30)
# draw_square(point2, 20)
# draw_pentagon(point3, 60)
# draw_hexagon(point4, 35)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def draw_shape(point_bottom_left, lines_count=3, angle=0, length=100, width=3):
    figure_angle = (360 / lines_count)
    v1 = None

    for i in range(lines_count):
        if v1:
            if i == lines_count - 1:
                sd.line(start_point=v1.end_point, end_point=point_bottom_left, width=width)

            else:
                v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length,
                                   width=width)
            v1.draw()
        else:
            # first line in a shape
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw()


def draw_triangle_v2(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=3, width=5)


def draw_square_v2(start_point, angle=0, length=100):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=4, width=5)


def draw_pentagon_v2(start_point, angle=0, length=100):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=5, width=5)


def draw_hexagon_v2(start_point, angle=0, length=100):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=6, width=5)


draw_triangle_v2(start_point=point1, angle=30, length=110)
draw_square_v2(start_point=point2, angle=20, length=110)
draw_pentagon_v2(start_point=point3, angle=60, length=110)
draw_hexagon_v2(start_point=point4, angle=35, length=110)

draw_shape(point5, 14)
sd.pause()
