# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_counts = {}

for student in students:
    name = student['first_name']
    
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
        
for name, count in name_counts.items():
    print(f'{name}: {count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_counts = {}

for student in students:
    name = student['first_name']
    
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
        
popular_name = max(name_counts, key=name_counts.get)
print(f'Самое частое имя среди учеников: {popular_name}') 

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

class_number = 1
for class_students in school_students:
    name_counts = {}
    for student in class_students:
        name = student['first_name']
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
            
    popular_name = max(name_counts, key=name_counts.get)
    print(f'Самое частое имя в классе {class_number}: {popular_name}')
    class_number += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for class_info in school:
    class_name = class_info['class']
    students = class_info['students']
    
    girls = 0
    boys = 0
    
    for student in students:
        name = student['first_name']
        if name in is_male and not is_male[name]:
            girls += 1
        elif name in is_male and is_male[name]:
            boys += 1
        
    print(f'Класс {class_name}: девочки {girls}, мальчики {boys}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

def count_students(students, gender_data):
    girls = 0
    boys = 0
    
    for student in students:
        name = student['first_name']
        if name in gender_data and not gender_data[name]:
            girls += 1
        elif name in gender_data and gender_data[name]:
            boys += 1
            
    return girls, boys

max_girls_class = max_boys_class = None
max_girls_count = max_boys_count = 0

for class_info in school:
    class_name = class_info['class']
    students = class_info['students']
    
    class_girls, class_boys = count_students(students, is_male)
        
    if class_girls > max_girls_count:
        max_girls_count, max_girls_class = class_girls, class_name
            
    if class_boys > max_boys_count:
        max_boys_count, max_boys_class = class_boys, class_name
            
print(f'Больше всего мальчиков в классе {max_boys_class}')
print(f'Больше всего девочек в классе {max_girls_class}')
