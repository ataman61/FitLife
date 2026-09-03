import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Привет")

user_name = input("Как вас зовут? ")

user_age = int(input("Сколько вам лет? "))

user_weight = float(input("Введите ваш вес (кг): "))

user_height = float(input("Введите ваш рост (м): "))

bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

water_ml = user_weight * 30
water_l = water_ml / 1000

print("-" * 40)
print(f"Отчёт для пользователя: {user_name}, {user_age} лет")
print(f"Твой индекс массы тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print("Расчёт окончен. Будьте здоровы!")
