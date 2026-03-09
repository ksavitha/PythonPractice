student = {"name": "Tom",
           "age": 10,
           "grade": "A"}
print(student["name"])
student["city"] = "San jose"
print(student)

numbers = {1, 2, 4, 2, 3}
print(numbers)

#word frequency counter
text = "python is easy and python is powerful"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

#group even and odd numbers
numbers = {1, 2, 3, 4, 6, 5, 7}
groups = {
    "odd": [],
    "even": []
}

for n in numbers:
    if n % 2 == 0:
        groups["even"].append(n)
    else:
        groups["odd"].append(n)
print(groups)

#expense tracker
expenses = {}
while True:
    expensename = input("Enter the expense name or done:" )
    if expensename == "done":
        break
    amt = float(input("Enter expense amount:"))
    expenses[expensename] = amt
print(expenses)
total = sum(expenses.values())
print("Total amount spent:" , total)

