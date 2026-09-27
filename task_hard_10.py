import json
from pathlib import Path


def save_to_json(data: dict, file_path: str | Path) -> None:
    """Сериализует словарь в JSON-файл с отступами."""
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_from_json(file_path: str | Path) -> dict:
    """Считывает и десериализует данные из JSON-файла."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    test_data = {
        "lab_number": 2,
        "variant": 10,
        "student": "Логинов Степан",
        "tasks": ["medium_10", "medium_2", "medium_8", "hard_3", "hard_10"],
        "status": "completed",
    }
    json_path = "output_data.json"
    save_to_json(test_data, json_path)
    restored = load_from_json(json_path)
    print("Прочитано из JSON:", restored)
