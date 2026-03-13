#files
file = open("tasks.txt", "w")
file.write("Hello to the file\n")
file.write("Learn leetcode\n")
file.close()

#using with
with open("tasks.txt", "w") as file:
    file.write("Hello world, this is using with in file handling")

#reading a file
with open("tasks.txt", "r") as file:
    data = file.read()
print(data)

#json
import json
tasks = ["Learn Python", "Solve leetcode"]
with open("tasks.json", "w") as file:
    json.dump(tasks, file)
with open("tasks.json", "r") as file:
    det = json.load(file)
print(det)