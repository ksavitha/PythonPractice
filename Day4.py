#Functions in python
def greet():
    print("Hello to python")


greet()

def add(a, b):
    print(a+b)


add(2, 4)

def add(a, b):
    return a + b


result = add(5, 3)
print(result)

def greet(name = "Guest"):
    print("Hello", name)
greet("Tom")
greet()

def square(x):
    return x * x
square = lambda x:x*x
print(square(8))

nums = [1, 2, 3, 4]
result = list(map(lambda x:x*x, nums))
print(result)

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

students = [{'Name': 'John', 'score': 90},
            {'Name': 'Anna', 'score': 30},
            {'Name': 'Tom', 'score': 76}]
students.sort(key=lambda s: s['score'])
print(students)

#Grading system

students = {"Tom": 85,
            "Anna": 92,
            "John": 87,
            "Mike": 60}

def get_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"
for name, score in students.items():
    grade = get_grade(score)
    print(name, score, grade)
