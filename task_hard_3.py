def generate_fibonacci(count: int) -> list[int]:
    """Генерирует список первых count чисел последовательности Фибоначчи."""
    if count <= 0:
        return []
    if count == 1:
        return [0]

    fib_series = [0, 1]
    while len(fib_series) < count:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


if __name__ == "__main__":
    count = 10
    print(f"Первые {count} чисел Фибоначчи:", generate_fibonacci(count))
