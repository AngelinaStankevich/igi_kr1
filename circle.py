import math

def area(r):
    # Проверка на положительное значение радиуса
    if r <= 0:
        return "Радиус должен быть положительным числом"
    return math.pi * r * r

def perimeter(r):
    # Проверка на положительное значение радиуса
    if r <= 0:
        return "Радиус должен быть положительным числом"
    return 2 * math.pi * r

def display_results(r):
    # Проверка на положительное значение радиуса
    if r <= 0:
        print("Ошибка: радиус должен быть положительным числом.")
        return
    print(f"Для окружности с радиусом {r}:")
    print(f"Площадь: {area(r):.2f}")
    print(f"Периметр: {perimeter(r):.2f}")

# Пример использования
radius = float(input("Введите радиус: "))
display_results(radius)


