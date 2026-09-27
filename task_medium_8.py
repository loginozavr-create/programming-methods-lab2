def reverse_string(text: str) -> str:
    """Возвращает перевёрнутую строку."""
    return text[::-1]


if __name__ == "__main__":
    sample = "Hello, Python!"
    print("Исходная строка :", sample)
    print("Развёрнутая строка:", reverse_string(sample))
