import logging

import sys

# Шаблон строки лога (аналог template в Serilog)

# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение

# Press Shift+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def log():

    # Шаблон строки лога (аналог template в Serilog)

    # Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение

    log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"

    date_format = "%Y-%m-%d %H:%M:%S"



    # Базовая настройка корневого логгера

    logging.basicConfig(

        level=logging.DEBUG,  # Минимальный уровень логирования (аналог MinimumLevel.Debug)

        format=log_format,

        datefmt=date_format,

        handlers=[

            logging.StreamHandler(sys.stdout),  # Настройка логирования в консоль

            logging.FileHandler("logs/file_txt.log", encoding="utf-8")  # Настройка логирования в файл

        ]

    )



    logging.info("Логгер успешно сконфигурирован")

    logging.info("Приложение запущено")





def CalculationCoordinate(a,b,c):

    bX = (a**2+b**2-c**2)/(a*2)

    bY = (b**2 - bX**2) ** 0.5

    return (int(bX), int(bY))



def Triangle(a, b, c):

    Status = ""

    A = (0, 0)

    B = (0, 0)

    C = (0, 0)

    try:

        a = float(a)

        b = float(b)

        c = float(c)

    except ValueError:

        A = B = C = (-2, -2)

        Status = "Некорректные данные"

        logging.exception(f"Введена не цифра.\n Результаты вычисления: Статус = {Status}, Стороны = {a, b, c}, Вершины = {A, B, C}")

        return Status, (A, B, C)



    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or c + b <= a:

        A = B = C = (-1, -1)

        Status = "Не треугольник"

        logging.error(f"Одно из введеных чисел меньше нуля или сумма двух сторон не образуют треугольник.\n Результаты вычисления: Статус = {Status}, Стороны = {a, b, c}, Вершины = {A, B, C}")

        return Status, (A, B, C)



    if a == b == c:

        Status = "Равносторонний"

    elif a == b or a == c or b == c:

        Status = "Равнобедренный"

    else:

        Status = "Разносторонний"



    C = (a, 0)

    B = CalculationCoordinate(a, b, c)



    logging.info(f"Вычисление прошло успешно.\n Результаты вычисления: Статус = {Status}, Стороны = {a, b, c}, Вершины = {A, B, C}")
    return Status, (A, B, C)





if __name__ == '__main__':

    log()

    print("Введите стороны треугольника\n")

    print("Сторона a:")

    a = input()

    print("Сторона b:")

    b = input()

    print("Сторона c:")

    c = input()

    Triangle(a, b, c) 