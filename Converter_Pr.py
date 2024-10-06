def convert_value(input_system, input_unit, input_value):

    conversions = {
        (1, 1): input_value * 25.4,  # дюйм в миллиметры
        (1, 2): input_value * 304.8,  # фут в миллиметры
        (1, 3): input_value * 914.4,  # ярд в миллиметры
        (1, 4): input_value * 1609344.0,  # миля в миллиметры
        (2, 1): input_value * 44.45,  # вершок в миллиметры
        (2, 2): input_value * 711.2,  # аршин в миллиметры
        (2, 3): input_value * 2133.6,  # сажень в миллиметры
        (2, 4): input_value * 1066800.0,  # верста в миллиметры
        (3, 1): input_value / 1000.0,  # миллиметры в СИ
        (3, 2): input_value / 100.0,  # сантиметры в СИ
        (3, 3): input_value * 1.0,  # метры в СИ
        (3, 4): input_value * 1000.0  # километры в СИ
    }

    return conversions.get((input_system, input_unit), None) or ValueError(
        "Неверный выбор системы или единицы измерения.")



def main():
    print("Добро пожаловать в конвертер величин!")
    while True:
        print("Выберите систему мер:")
        print("1. Американская система")
        print("2. Старорусская система")
        print("3. Международная система единиц (СИ)")
        input_system = int(input("Ваш выбор: "))
        if input_system not in [1, 2, 3]:
            print("Неверный выбор системы мер. Попробуйте снова.")
            continue

        print("Выберите единицу измерения:")
        if input_system == 1:
            print("1. Дюйм")
            print("2. Фут")
            print("3. Ярд")
            print("4. Миля")
        elif input_system == 2:
            print("1. Вершок")
            print("2. Аршин")
            print("3. Сажень")
            print("4. Верста")
        elif input_system == 3:
            print("1. Миллиметр")
            print("2. Сантиметр")
            print("3. Метр")
            print("4. Километр")

        input_unit = int(input("Ваш выбор: "))
        if input_unit not in [1, 2, 3, 4]:
            print("Неверный выбор единицы измерения. Попробуйте снова.")
            continue
        input_value = float(input("Введите значение: "))
        output_value = convert_value(input_system, input_unit, input_value)
        if input_system == 1 or input_system == 2:
            print(f"Результат: {output_value} мм")
        else:
            print(f"Результат: {output_value} м")
        if input("Хотите конвертировать другую величину? (да/нет) ").lower() != "да":
            break

if __name__ == "__main__":
    main()