# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
def get_color(number):
    if number == 0:
        return sd.COLOR_RED
    elif number == 1:
        return sd.COLOR_ORANGE
    elif number == 2:
        return sd.COLOR_YELLOW
    elif number == 3:
        return sd.COLOR_GREEN
    elif number == 4:
        return sd.COLOR_CYAN
    elif number == 5:
        return sd.COLOR_BLUE
    elif number == 6:
        return sd.COLOR_PURPLE


def draw_shape(point_bottom_left, lines_count=3, angle=0, length=100, width=3, color=sd.COLOR_YELLOW):
    figure_angle = (360 / lines_count)
    v1 = None

    for i in range(lines_count):
        if v1:
            if i == lines_count - 1:
                sd.line(start_point=v1.end_point, end_point=point_bottom_left, width=width, color=color)

            else:
                v1 = sd.get_vector(start_point=v1.end_point, angle=angle + i * figure_angle, length=length,
                                   width=width)
            v1.draw(color=color)
        else:
            # first line in a shape
            v1 = sd.get_vector(start_point=point_bottom_left, angle=angle, length=length, width=width)
            v1.draw(color=color)


def draw_triangle_v2(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=3, width=5, color=color)


def draw_square_v2(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=4, width=5, color=color)


def draw_pentagon_v2(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=5, width=5, color=color)


def draw_hexagon_v2(start_point, angle=0, length=100, color=sd.COLOR_YELLOW):
    draw_shape(point_bottom_left=start_point, angle=angle, length=length, lines_count=6, width=5, color=color)


point1 = sd.get_point(50, 50)
point2 = sd.get_point(380, 50)
point3 = sd.get_point(150, 380)
point4 = sd.get_point(450, 380)
point5 = sd.get_point(200, 200)
print("Possible colors:")
print("0 : red")
print("1 : orange")
print("2 : yellow")
print("3 : green")
print("4 : cyan")
print("5 : blue")
print("6 : purple")

user_input = ""
while True:
    user_color = input("Enter a number for shapes color > ")
    try:
        user_input = int(user_color)

    except ValueError:
        print("Invalid input, must be a number")

    if user_input and 0 <= user_input <= 6:
        break
    else:
        if user_input:
            print("Invalid input, must be a number between 0 - 6")
        continue

color_tuple = get_color(number=user_input)

draw_triangle_v2(start_point=point1, angle=30, length=110, color=color_tuple)
draw_square_v2(start_point=point2, angle=20, length=110, color=color_tuple)
draw_pentagon_v2(start_point=point3, angle=60, length=110, color=color_tuple)
draw_hexagon_v2(start_point=point4, angle=35, length=110, color=color_tuple)

sd.pause()
