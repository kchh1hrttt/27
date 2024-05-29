import os


def analyze_file_extensions(directory_path):
    """
    Аналізує розширення файлів у вказаній директорії та виводить статистику.

    Args:
        directory_path (str): Шлях до директорії для аналізу.
    """

    extension_counts = {}  # Словник для зберігання кількості та сумарної довжини назв файлів за розширенням

    # Перевірка існування директорії
    if not os.path.exists(directory_path):
        print(f"Помилка: Директорія '{directory_path}' не знайдена.")
        return

    for filename in os.listdir(directory_path):
        # Отримання розширення файлу
        base, extension = os.path.splitext(filename)

        # Ігнорування файлів без розширення
        if extension:
            # Оновлення словника extension_counts
            if extension in extension_counts:
                extension_counts[extension][0] += 1  # Збільшення кількості файлів
                extension_counts[extension][1] += len(filename)  # Збільшення сумарної довжини назв
            else:
                extension_counts[extension] = [1, len(filename)]  # Ініціалізація для нового розширення

    # Виведення результатів у форматі таблиці
    print("Розширення | Кількість файлів | Сумарна довжина назв")
    print("-----------|------------------|---------------------")
    for extension, (count, total_length) in extension_counts.items():
        print(f"{extension:<10} | {count:<16} | {total_length:<21}")


# Отримання шляху до директорії від користувача
directory_path = input("Введіть шлях до директорії: ")

# Виклик функції для аналізу розширень файлів
analyze_file_extensions(directory_path)
