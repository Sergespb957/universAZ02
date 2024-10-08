import pandas as pd

# 1. Создаем DataFrame с данными
data = {
    'Имя': ['Аня', 'Борис', 'Вика', 'Геннадий', 'Дарья', 'Егор', 'Жанна', 'Иван', 'Кира', 'Лев'],
    'Математика': [5, 4, 3, 5, 2, 4, 3, 5, 4, 3],
    'Физика': [4, 5, 3, 4, 2, 5, 4, 3, 5, 4],
    'Химия': [5, 3, 4, 5, 2, 4, 3, 5, 4, 3],
    'Русский язык': [4, 4, 3, 5, 2, 4, 5, 3, 4, 4],
    'Литература': [3, 4, 5, 4, 2, 3, 5, 4, 3, 4]
}

df = pd.DataFrame(data)

# 2. Выводим первые несколько строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# 3. Вычисляем среднюю оценку по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# 4. Вычисляем медианную оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# 5. Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для Математики:", Q1_math)
print("Q3 для Математики:", Q3_math)
print("IQR для Математики:", IQR_math)

# 6. Вычисляем стандартное отклонение
std_devs = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_devs)
