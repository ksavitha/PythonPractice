# lists
numbers = [10, 20, 30, 40]
print(numbers)
print(numbers[0])
numbers.append(79)
print(numbers)

for n in numbers:
    print(n)
i = 1
while i <= 5:
    print(i)
    i = i+1
print("Printing range: ")
for i in range(1, 5):
    print(i)

#Find the max number
numlist = [30,54,28,45]
maxnumber = numlist[0]
for n in numbers:
    if n > maxnumber:
        maxnumber = n
print(maxnumber)

#remove duplicates
nums = [28, 49, 56, 33, 1, 2, 3, 3, 2, 2]
uninums = []
for n in nums:
    if n not in uninums:
        uninums.append(n)
print("unique numbers: ", uninums)


#count frequency
numbers = [1, 2, 2, 3, 4, 4, 5]
freq = {}
for n in numbers:
    freq[n] = freq.get(n, 0) + 1
print(freq)

# paragraph word counter
text = input("Please enter the paragraph")
words = text.split()
print("number of words in the paragraph", len(words))
