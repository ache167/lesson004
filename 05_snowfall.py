# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 40
x_screen_res, y_screen_res = 1200, 800
sd.resolution = (x_screen_res, y_screen_res)
y_top_half = int(y_screen_res / 2) + 200
# нарисовать снежинку в точке center с длинной лучей length цветом color
#         factor_a - место ответвления лучиков factor_a=0.6
#         factor_b - длина лучиков factor_b=0.35
#         factor_c - угол отклонения лучиков factor_c=60
snowflakes_starting_points = []
snowflakes_lengths = []
snowflakes_factors_a_b_c = []
snowflakes_fallen_coordinates = []
snowflakes_fallen_lengths = []
snowflakes_fallen_factors_a_b_c = []

for i in range(N):
    snowflakes_starting_points.append([sd.randint(0, x_screen_res), sd.randint(y_top_half, y_screen_res + 450)])
    snowflakes_lengths.append(sd.randint(10, 50))
    snowflakes_factors_a_b_c.append(
        [round(random.uniform(0.3, 0.9), 2), round(random.uniform(0.15, 0.55), 2), round(sd.randint(50, 70), 2)])

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

while True:
    for i in range(len(snowflakes_starting_points)):
        point = sd.get_point(snowflakes_starting_points[i][0], snowflakes_starting_points[i][1])
        sd.start_drawing()
        sd.snowflake(center=point, length=snowflakes_lengths[i], factor_a=snowflakes_factors_a_b_c[i][0],
                     factor_b=snowflakes_factors_a_b_c[i][1], factor_c=snowflakes_factors_a_b_c[i][2],
                     color=sd.background_color)

        if snowflakes_starting_points[i][1] >= snowflakes_lengths[i]:
            snowflakes_starting_points[i][1] -= sd.randint(12, 40)
            left_or_right_rand = round(random.uniform(0, 1), 2)
            if left_or_right_rand < 0.5:
                snowflakes_starting_points[i][0] -= sd.randint(3, 10)
            else:
                snowflakes_starting_points[i][0] += sd.randint(3, 10)

            point2 = sd.get_point(snowflakes_starting_points[i][0], snowflakes_starting_points[i][1])

            sd.snowflake(center=point2, length=snowflakes_lengths[i], factor_a=snowflakes_factors_a_b_c[i][0],
                         factor_b=snowflakes_factors_a_b_c[i][1], factor_c=snowflakes_factors_a_b_c[i][2],
                         color=sd.COLOR_WHITE)
        else:
            # adding snowflake that fallen into a ground to fallen lists
            snowflakes_fallen_coordinates.append([snowflakes_starting_points[i][0], snowflakes_starting_points[i][1]])
            snowflakes_fallen_factors_a_b_c.append(
                [snowflakes_factors_a_b_c[i][0], snowflakes_factors_a_b_c[i][1], snowflakes_factors_a_b_c[i][2]])
            snowflakes_fallen_lengths.append(snowflakes_lengths[i])

            # removing a fallen snowflake from list of falling snowflakes
            snowflakes_starting_points.pop(i)
            snowflakes_lengths.pop(i)
            snowflakes_factors_a_b_c.pop(i)

            # creating a new snowflake in a list of falling snowflakes
            snowflakes_lengths.append(sd.randint(10, 50))
            snowflakes_starting_points.append([sd.randint(0, x_screen_res), y_screen_res + 50])
            snowflakes_factors_a_b_c.append(
                [round(random.uniform(0.3, 0.9), 2), round(random.uniform(0.15, 0.55), 2),
                 round(sd.randint(50, 70), 2)])

    for i in range(len(snowflakes_fallen_coordinates)):
        point = sd.get_point(snowflakes_fallen_coordinates[i][0], snowflakes_fallen_coordinates[i][1])

        sd.snowflake(center=point, length=snowflakes_fallen_lengths[i], factor_a=snowflakes_fallen_factors_a_b_c[i][0],
                     factor_b=snowflakes_fallen_factors_a_b_c[i][1], factor_c=snowflakes_fallen_factors_a_b_c[i][2])

    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

