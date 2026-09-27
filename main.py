from task_hard_3 import generate_fibonacci
from task_hard_10 import load_from_json, save_to_json
from task_medium_2 import sum_odd_numbers
from task_medium_8 import reverse_string
from task_medium_10 import generate_squares_dict


def main():
    print("=== ЛАБОРАТОРНАЯ РАБОТА №2 | ВАРИАНТ 10 ===")

    print("\n--- Задание 10 (Среднее): Словарь квадратов ---")
    print("Квадраты до 5:", generate_squares_dict(5))

    print("\n--- Задание 2 (Среднее): Сумма нечётных чисел ---")
    print("Сумма нечётных до 9:", sum_odd_numbers(9))

    print("\n--- Задание 8 (Среднее): Разворот строки ---")
    print("Разворот 'структурное':", reverse_string("структурное"))

    print("\n--- Задание 3 (Повышенное): Фибоначчи ---")
    print("8 чисел Фибоначчи:", generate_fibonacci(8))

    print("\n--- Задание 10 (Повышенное): JSON ---")
    data = {"variant": 10, "lab": 2, "ok": True}
    save_to_json(data, "demo.json")
    print("Записано и прочитано:", load_from_json("demo.json"))


if __name__ == "__main__":
    main()
