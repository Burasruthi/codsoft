class Todolist:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)
        print("Task added Successfully")

    def display_task(self):
        if self.tasks:
            print("TO-DO LIST")
            for index,task in enumerate(self.tasks, start=1):
                print(f"{index},{task}")
        else:
            print("List is empty")

    def update_task(self,index,new_task):
        if 1<=index<=len(self.tasks):
            new_task=self.tasks[index-1]
            print("task updated successfully")
        else:
            print("can't update task")

    def delete_task(self,index):
        if 1<=index<=len(self.tasks):
            del self.tasks[index-1]
            print("task deleted successfully")
        
def main():
    todo_list=Todolist()
    while True:
        print("\n --To-dolist--\n" \
               "1.Add task\n" \
               "2.display task\n" \
               "3.update task\n" \
               "4.delete task\n" \
               "5.exit" )
        
        choice=int(input("enter your choice:"))

        if(choice==1):
            n_task=int(input("enter how many no of tasks you want to add:"))
            for i in range(n_task):
                task=input("enter task:")
                todo_list.add_task(task)

        elif(choice==2):
            todo_list.display_task()

        elif(choice==3):
            index=int(input("enter the index no you want to update:"))
            new_task=input("enter new task:")
            todo_list.update_task(index,new_task)
        
        elif(choice==4):
            index=int(input("enter the index number of the task you want to delete:"))
            todo_list.delete_task(index)

        elif(choice==5):
            print("exit")
            break
        
        else:
            print("Invalid choice")


main()


    
