import matplotlib.pyplot as plt
import json
import pandas as pd
from tabulate import tabulate

print("Student Productivity \n")
name=input("Enter your name:")

task_list=[]

count=1

def add_task():
    task=input("\nEnter your task :")
    while True:
        due_date=input("Enter the due date (DDMMYYYY):")
        if len(due_date)==8:
            break
        else:
            print("Kindly follow the date format and enter it")
            continue
    formatted=due_date[:2]+"/"+due_date[2:4]+"/"+due_date[4:]
    priority=input("What is the priority of this task (high/medium/low):")
    data_group={"Task":task,"Due date":formatted,"Priority":priority,"Completed":False}
    task_list.append(data_group)
    
    print("\nThe task added successfully!")
    

def view_task():
   
    print("_______________________Your Tasks_________________________\n")
    
    df=pd.DataFrame(task_list)
    df.index+=1
    print(tabulate(df,headers='keys',tablefmt='grid'))

def completed_task():
    print("_______________________Your Completed Tasks_________________________\n")
    count=1
    index=0
    for i in task_list:
        
        if i["Completed"]==True:
            print(count,".","Task:",task_list[index]["Task"],"\n","   Due date:",task_list[index]["Due date"],"\n","   Priority:",task_list[index]["Priority"],"\n","   Completed:",task_list[index]["Completed"])
            count+=1
            index+=1
    
open("Task history.json","w").close()


def save_task():
    with open("Task history.json","w") as f:
        json.dump(task_list,f,indent=4)

def pie_chart():
    
    completed=0
    pending=0
    for i in task_list:
        if i["Completed"]:
            completed+=1
        else:
            pending+=1
    data=[completed,pending]
    label=["Completed","Pending"]
    plt.pie(data,labels=label,autopct='%1.1f%%',shadow=True,wedgeprops={'edgecolor':'black','linewidth':2})
    plt.title("Your Tasks")
    plt.show()
                

task_list=[]
while True:
    print("\n1.Add a task\n2.View all tasks\n3.Mark completed\n4.List of completed tasks\n5.Save all tasks in a file\n6.Analysing your tasks through pie chart\n7.Exit")
    print("\nWhat action should be performed?")
    
    try:
        choice=int(input("\nEnter the respective serial number to perform the action:"))
        if choice==1:
            add_task()
            continue
    
        elif choice==2:
            if len(task_list)==0:
                print("\nKindly add any task to view it")
            else:
                view_task()
            continue
    
        elif choice==3:
            if len(task_list)==0:
                print("\nKindly add any task to mark it as completed")
                continue
            else:
                view_task()
                total_tasks=[]
                
                for i in range(1,len(task_list)+1):
                    total_tasks.append(i)
                
                complete=int(input(f"\nWhich task have you completed ({total_tasks}):"))
                task_list[complete-1]["Completed"]=True 
                print("\nTask marked as completed")
                while True:
                    check=input("\nWould you like to delete the task? (Yes/No):")
                    check.lower()
                    if check=="yes":
                        for i in task_list:
                            if i["Completed"]==True:
                                task_list.remove(i)
                        print("The task deleted successfully")
                        break
                    elif check=="no":
                        break
        
                    else:
                        print("Kindly enter valid input (Yes/No)!")
                        continue
                    
           
        elif choice==4:
            if len(task_list)==0:
              print("\nKindly add any task to view it")
            else:
                completed_task()
            continue
            
        elif choice==5:
            save_task()
            print("\nFile saved successfully")
            continue
    
        elif choice==6:
            if len(task_list)==0:
                print("\nKindly add any task to view the pie chart")
            else:
                pie_chart()
            continue
    
        elif choice==7:
            break
    except ValueError:
        print("Enter any number (1,2,3,..)")

    
    
    
    