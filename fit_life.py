# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
WATER_ML_L = 1000


def helloy_how_you_name():
    """Запрос у пользователя имя и возраста с проверкой на корректность"""
    user_name = input("Как вас зовут? ")
    while True:
        try:
            user_age = int(input(f"{user_name} сколько вам полных лет? "))
            if user_age < 0:
                print("Возраст не может быть отрицательным")
                continue
            break
        except ValueError:
            print("Пожалуйста, укажите возраст целым числом")
    return user_name, user_age


# 2. Сбор данных
def start_info(user_name):
    """Запрос у пользователя роста и веса с проверкой на корректоность"""
    while True:
        try:
            user_weight = float(input(f"{user_name}, какой ваш вес в кг "))
            if user_weight > 500 or user_weight < 0:
                print("Вы ввели неправдоподобный вес")
                continue
            break
        except ValueError:
            print("Пожалуйста введите число через знак ' . ' к примеру 36.0")
            continue
    while True:
        try:
            user_height = float(input(f"{user_name} какой ваш рост в метрах "))
            if user_height < 0 or user_height > 2.72:
                print("Вы ввели неправдоподобный рост")
                continue
            break
        except ValueError:
            print("Пожалуйста введите число через знак ' . ' к примеру 1.75 ")

    return user_weight, user_height


# 3. Расчеты ИМТ и нормы воды
def recomendation(user_weight, user_height):
    """Расчет ИМТ и нормы воды на основе введенных  данных пользователя"""
    bmi = user_weight / user_height**2
    water_needed = user_weight * WATER_PER_KG / WATER_ML_L

    return (bmi, water_needed)


# 4. Вывод красивого результата

print('Добрый день, я FitlifeBot!')
print('Я помогу вам следить за вашим здоровьев')
user_name, user_age = helloy_how_you_name()
user_weight, user_height = start_info(user_name)
bmi, water_needed = recomendation(user_weight, user_height)
print(f'{user_name}, ваш индекс массы тела равен: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_needed:.1f} л. в день')
print()
print("Расчет окончен. Будьте здоровы!")
