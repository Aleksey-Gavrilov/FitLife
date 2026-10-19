# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
WATER_ML_L = 1000
MINIMUM_VALUE = 0
MAXIMUM_WEIGHT = 500
MAXIMUM_HEIGHT = 2.72


def take_name():
    """Запрос у пользователя имя"""
    user_name = input("Как вас зовут? ")
    return user_name


def take_age(user_name):
    """Запрос у пользователя возраста с проверкой на корректность"""
    while True:
        try:
            user_age = int(input(f"{user_name} сколько вам полных лет? "))
            if user_age <= MINIMUM_VALUE:
                print("Возраст не может быть отрицательным")
                continue
            break
        except ValueError:
            print("Пожалуйста, укажите возраст целым числом")
    return user_age


# 2. Сбор данных
def take_user_weight(user_name):
    """Запрос у пользователя веса с проверкой на корректоность"""
    while True:
        try:
            user_weight = float(input(f"{user_name}, какой ваш вес в кг "))
            if user_weight >= MAXIMUM_WEIGHT or user_weight <= MINIMUM_VALUE:
                print("Вы ввели неправдоподобный вес")
                continue
            break
        except ValueError:
            print("Пожалуйста введите число через знак ' . ' к примеру 36.0")
            continue
    return user_weight


def take_user_height(user_name):
    """Запрос у пользователя роста с проверкой на корректоность"""
    while True:
        try:
            user_height = float(input(f"{user_name} какой ваш рост в метрах "))
            if user_height <= MINIMUM_VALUE or user_height >= MAXIMUM_HEIGHT:
                print("Вы ввели неправдоподобный рост")
                continue
            break
        except ValueError:
            print("Пожалуйста введите число через знак ' . ' к примеру 1.75 ")

    return user_height


# 3. Расчеты ИМТ и нормы воды
def сalculation_bmi_and_water(user_weight, user_height):
    """Расчет ИМТ и нормы воды на основе введенных  данных пользователя"""
    bmi = user_weight / user_height**2
    water_needed = user_weight * WATER_PER_KG / WATER_ML_L

    return (bmi, water_needed)


# 4. Вывод красивого результата

print("Добрый день, я FitlifeBot!")
print("Я помогу вам следить за вашим здоровьев")
user_name = take_name()
user_age = take_age(user_name)
user_weight = take_user_weight(user_name)
user_height = take_user_height(user_name)
bmi, water_needed = сalculation_bmi_and_water(user_weight, user_height)
print(f"{user_name}, ваш индекс массы тела равен: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
