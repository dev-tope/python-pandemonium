import time, os
print("To-do list")
print()

taskList = []

def prettyPrint():
  counter = 1
  for task, date, priority in taskList:
    print (f"{counter}. {task} | {date} | {priority}")
    counter += 1
    
def findTaskMain():
 global taskMain 
 taskMain = []
 for task, date, priority in taskList:
  taskMain.append(task, date, priority)
  return taskMain
  
while True:  
  print("What would you like to do today?\n 1.Add Task\n 2.View Tasks\n 3.Edit Task \n 4.Remove Task")
  print()
  action = input("> ")
  print()
  
  if action == "1":
    time.sleep(0.5)
    os.system("clear")
    newTask = []
    
    task = input("Enter the task > ")
    newTask.append(task)
   
    
    dueDay = input("Due Day > ")
    newTask.append(dueDay)
    
    priority = input("Priority Level > ")
    newTask.append(priority)
    
  
    taskList.append(newTask)
    time.sleep(0.5)
    os.system("clear")
    print(f"{task} Added!")
    time.sleep(1)
    os.system("clear")
  
  
  if action == "2":
    time.sleep(0.5)
    os.system("clear")
    
    print("1.View All\n 2.View Priority")
    viewAction = input("> ")
    
    if viewAction == "1":
      time.sleep(0.5)
      os.system("clear")
      prettyPrint()
      print()
      
    if viewAction == "2":
      print("What task priority do you want to view\n 1.High\n 2.Medium\n 3.Low")
      viewPriorityAction = input("> ")
      for task in taskList:
        if viewPriorityAction == "1":
          if task[2].strip().lower() == "high":
            print(task[0])
        elif viewPriorityAction == "2":  
          if task[2].strip().lower() == "medium":
            print(task[0])
        elif viewPriorityAction == "3":
          if task[2].strip().lower() == "low":
            print(task[0])
          
    menuOpt = input("Go back to main menu? y/n")
    if menuOpt.strip().lower() == "y":
      continue
      
  if action == "3":
    prettyPrint()
    print()
    print("What task do you want to edit")
    editChoice = input("> ")
    