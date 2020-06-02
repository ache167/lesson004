# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def draw_branches(start_point, angle, length):
    if length < 3:
        return

    next_angle_right_branch = angle - 30
    next_angle_left_branch = angle + 30

    length_factor = 0.75

    left_branch = sd.get_vector(start_point=start_point, angle=next_angle_left_branch, length=length * length_factor)
    left_branch.draw()
    right_branch = sd.get_vector(start_point=start_point, angle=next_angle_right_branch, length=length * length_factor)
    right_branch.draw()

    draw_branches(start_point=right_branch.end_point, angle=next_angle_right_branch, length=length * length_factor)
    draw_branches(start_point=left_branch.end_point, angle=next_angle_left_branch, length=length * length_factor)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75

def draw_branches_randomized(start_point, angle, length):
    if length < 3:
        return

    angle_range_left = int(0.6 * 30)
    angle_range_right = int(1.4 * 30)
    angle_random_change_left = sd.randint(angle_range_left, angle_range_right)
    angle_random_change_right = sd.randint(angle_range_left, angle_range_right)
    next_angle_left_branch = angle + angle_random_change_left
    next_angle_right_branch = angle - angle_random_change_right

    length_range_left = int(0.8 * 0.75 * length)
    length_range_right = int(1.2 * 0.75 * length)
    length_left_rand_factor = sd.randint(length_range_left, length_range_right)
    length_right_rand_factor = sd.randint(length_range_left, length_range_right)

    left_branch = sd.get_vector(start_point=start_point,
                                angle=next_angle_left_branch, length=length_left_rand_factor)
    left_branch.draw()

    right_branch = sd.get_vector(start_point=start_point, angle=next_angle_right_branch,
                                 length=length_right_rand_factor)
    right_branch.draw()

    draw_branches_randomized(start_point=left_branch.end_point, angle=next_angle_left_branch,
                             length=length_left_rand_factor)
    draw_branches_randomized(start_point=right_branch.end_point, angle=next_angle_right_branch,
                             length=length_right_rand_factor)


ground_point_start = sd.get_point(300, 0)
ground_point_end = sd.get_point(300, 30)
sd.line(start_point=ground_point_start, end_point=ground_point_end)

root_point = sd.get_point(300, 30)
draw_branches_randomized(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.random_number()

sd.pause()
