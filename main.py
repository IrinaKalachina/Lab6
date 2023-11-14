class Company:
    """Описание фирмы"""
    def __init__(self):  # Присвоение атрибутам значений
        pass

    @property
    def vehicles(self):
        return self

    @property
    def drivers(self):
        return self

    def add_vehicle(self, vehicle):  # Добавление транспорта в класс
        pass

    def add_driver(self, driver):  # Добавление водителя в класс
        pass

    def __str__(self):  # Метод перевода объекта в строку
        pass


class Vehicle:  # Класс транспорт
    def __init__(self):
        pass

    def tip(self):
        return self

    def __str__(self):
        pass


class Driver:  # Класс водитель
    def __init__(self):
        pass

    def __str__(self):
        pass


def main():
    while True:
        print("\nМеню:")
        print("1. Создать новую фирму\n"
              "2. Создать новый транспорт\n"
              "3. Создать нового водителя\n"
              "4. Вывести содержимое фирм\n"
              "5. Вывести содержимое транспорта\n"
              "6. Вывести содержимое водителей\n"
              "7. Вывести представление конкретной фирмы\n"
              "8. Завершить работу программы")

        choice = input("Выберите действие: ")

        if choice == "1":
            print(f"Фирма создана.")
        elif choice == "4":
            print("\nСписок фирм:")
        elif choice == "5":
            print("\nСписок транспорта:")
        elif choice == "6":
            print("\nСписок водителей:")
        elif choice == "8":
            print("Программа завершена.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
