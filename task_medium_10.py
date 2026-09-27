def generate_squares_dict(n: int) -> dict[int, int]:
    """Генерирует словарь {x: x^2} для чисел от 1 до n."""
    if n < 1:
        return {}
    return {x: x**2 for x in range(1, n + 1)}


if __name__ == "__main__":
    n = 7
    squares = generate_squares_dict(n)
    print(f"Словарь квадратов чисел до {n}:", squares)
