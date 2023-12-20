from random import randint
start = 1
end = 1000
value = randint,{start,end}

print("The computer choose a number beetwen",start,"and", end)
guess = None

while guess !=value:
    text = input("guess the number:")
    guess = int(text)
    if guess < value:
        print("the expected number is higher")
        if guess > value:
            print("the expected number is lower")
print("congratulation you dit it, your a champ")


class Task:
    def __init__(self,description,completed=False):
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed=True

    def __str__(self):
        status = "Done" if self.completed else "not done"
        return f"{self.description} -status: {status}"


class TaskList:
    def __init__(self):
        self.task = []

    def add_task(self, description):
        task = Task(description)
        self.task.append(task)


    def remove_task(self,index):
        if 0 <= index < len(self.task):
            del self.task[index]


def main():
    task_list = TaskList()
    while True:
        print("\nOption")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as completed")
        print("4. List Task")
        print("5. Quit")

        choice = input("Enter your choice")

        if choice =="1":
            description = input("Enter your task description")
            task_list.add_task(description)
            print("Task added")
        elif choice == "2":
            index=int(input("Enter the index of the task you are trying to remove"))
            task_list.remove_task(index)
            print("task removed")
        elif choice == "3":
            index = int(input("Enter the index of the task to mark  as completed"))-1
            task_list.mark_task_as_completed(index)
            print("Task marked as completed")
        elif choice == "4":
            print('\nTask List')
            task_list.display_task()

        elif choice =="5":
            print("Exit")

