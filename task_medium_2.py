def sum_odd_numbers(n: int) -> int:
    """Вычисляет сумму всех нечётных положительных чисел от 1 до n включительно."""
    if n < 1:
        return 0
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


if __name__ == "__main__":
    n = 10
    result = sum_odd_numbers(n)
    print(f"Сумма нечётных чисел до {n}:", result)
