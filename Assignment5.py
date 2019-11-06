# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Yunan Xu>,<11.5.2019>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "Todo.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection



# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
objFile=open("Todo.txt","w")
dicRow={"Task":"Washing dishes","Priority":"2"}
objFile.write(dicRow["Task"]+","+dicRow["Priority"]+'\n')
dicRow={"Task":"Doing homework","Priority":"1"}
objFile.write(dicRow["Task"]+","+dicRow["Priority"]+'\n')
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("-------------------------------------")  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile=open("Todo.txt","r")
        for row in objFile:
            lstRow=row.split(",")
            dicrow={"Task":lstRow[0],"Priority":lstRow[1]}
            print(dicrow)
        objFile.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        #objFile=(objFile,"")
        Taskn=input("Enter your task here : ")
        Pri=input("Enter your priority here: ")
        dic={"Task":Taskn,"Priority":Pri}
        lstTable=[dic]
        #objFile.write(dic["Task"]+","+dic["Priority"]+'\n')
        #objFile.close()

        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        delete=input("item you want to delete : ")
        with open("Todo.txt", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if delete not in line:
                    f.write(line)
            f.truncate()

        f.close()


        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("Todo.txt", "a")
        objFile.write(dic["Task"] + "," + dic["Priority"] + '\n')
        objFile.close()

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exist the program")

        break  # and Exit the program

