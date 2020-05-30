# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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


point_middle = sd.get_point(250, 250)
print("Possible shapes:")
print("0 : triangle")
print("1 : square")
print("2 : pentagon")
print("3 : hexagon")

user_input = ""
while True:
    user_color = input("Enter a number for a shapes > ")
    try:
        user_input = int(user_color)
    except ValueError:
        print("Invalid input, must be a number")

    if user_input and 0 <= user_input <= 3:
        break
    else:
        if user_input:
            print("Invalid input, must be a number between 0 - 3")
        continue

if user_input == 0:
    draw_triangle_v2(start_point=point_middle, length=110)
elif user_input == 1:
    draw_square_v2(start_point=point_middle, length=110)
elif user_input == 2:
    draw_pentagon_v2(start_point=point_middle, length=110)
elif user_input == 3:
    draw_hexagon_v2(start_point=point_middle, length=110)

sd.pause()
