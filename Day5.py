#practice 1 - userclass

class user:

    def __init__(self, username, email):
        self.username = username
        self.email = email
    def display(self):
        print(self.username, self.email)

u1 = user('savitha', 's@gmail.com')
u1.display()

#practice 2 - Bank account class

class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def showbalance(self):
        print(self.balance)
acc = BankAccount("Savitha", 400)
acc.showbalance()
acc.withdraw(100)
acc.showbalance()
acc.deposit(400)
acc.showbalance()

#task manager
class TaskManager:
    def __init__(self):
        self.tasks = []
    def show_tasks(self):
        for t in self.tasks:
            print(t)
    def add_task(self, task):
        self.tasks.append(task)

tm = TaskManager()
tm.add_task("Read a book")
tm.show_tasks()
tm.add_task("Learn Python")
tm.show_tasks()

