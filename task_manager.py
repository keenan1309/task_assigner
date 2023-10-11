#=====importing libraries===========
# '''This is the section where you will import libraries'''
import datetime
current_time = datetime.date.today()

#====Login Section====
# '''Here you will write code that will allow a user to login.
#     - Your code must read usernames and password from the user.txt file
#     - You can use a list or dictionary to store a list of usernames and passwords from the file.
#     - Use a while loop to validate your user name and password.
# '''
val = True
while val:

    user_name = input("Can you please insert a username : ")
    user_pass = input("Can you please insert a password : ")
    admin_user = open("user.txt", "r+")
    users = admin_user.readlines()

    for user in users:

        split_user = user.strip().split(", ")
        if split_user[0] == user_name and split_user[1] == user_pass:
            print("Thank you credentials has been confirmed.")
            val = False
            break
        else:
            pass
    if split_user[0] != user_name and split_user[1] != user_pass:
        print("Invalid please try again.")

admin_user.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':

# '''In this block you will write code to add a new user to the user.txt file
# - You canresent a relevan follow the following steps:
#     - Request input of a new username
#     - Request input of a new password
#     - Request input of password confirmation.
#     - Check if the new password and confirmed password are the same.
#     - If they are the same, add them to the user.txt file,
#     - Otherwise you pt message.'''

        new_user = input("Can you please assist with a user name :")
        new_pass = input("Can you please assist with a new password :")
        admin_user = open("user.txt","a+")
        admin_user.write(f"\n{new_user}, {new_pass}")
        print("Thank you this has been done...")
        admin_user.close()
        pass


    elif menu == 'a':

# '''In this block you will put code that will allow a user to add a new task to task.txt file
# - You can follow these steps:
#     - Prompt a user for the following: 
#         - A username of the person whom the task is assigned to,
#         - A title of a task,
#         - A description of the task and 
#         - the due date of the task.
#     - Then get the current date.
#     - Add the data to the file task.txt and
#     - You must remember to include the 'No' to indicate if the task is complete.'''
    
        assignee_name = input("Please insert this to the name of the person this should be assigned too : ")
        task_title = input("Can you insert the title of the task : ")
        task_description = input("Can you please insert a task description : ")
        due_date = input("Please enter the due date in the following format ' dd/mmm/yyyy ' :")
        admin_user = open("tasks.txt","a+")
        admin_user.write(f"\n{assignee_name}, {task_title}, {task_description}, {current_time}, {due_date}, No")
        print("Thank you this has been done")
        admin_user.close()

    elif menu == 'va':
# '''In this block you will put code so that the program will read the task from task.txt file and
#  print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#  You can do it in this way:
#     - Read a line from the file.
#     - Split that line where there is comma and space.
#     - Then print the results in the format shown in the Output 2 
#     - It is much easier to read a file using a for loop.'''
        print("See the complete task list : ")
        admin_user = open("tasks.txt","r+")
        tasks = admin_user.readlines()
        for i in tasks:
            i_split = i.split(", ")
            print(f'''              
Task Assigned too : {i_split[0]}
Task Title : {i_split[1]}
Task Description: {i_split[2]}
Current date : {i_split[3]}
Due date : {i_split[4]}
Completed : {i_split[5]}
''')
        pass

    elif menu == 'vm':
# '''In this block you will put code the that will read the task from task.txt file and
#  print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#  You can do it in this way:
#     - Read a line from the file
#     - Split the line where there is comma and space.
#     - Check if the username of the person logged in is the same as the username you have
#     read from the file.
#     - If they are the same print it in the format of Output 2 in the task PDF'''
        print("See the complete task list : ")
        admin_user = open("tasks.txt","r+")
        tasks = admin_user.readlines()
        for i in tasks:
            i_split = i.strip().split(", ")
            if i_split[0] == user_name:
                print(f'''              
Task Assigned too : {i_split[0]}
Task Title : {i_split[1]}
Task Description: {i_split[2]}
Current date : {i_split[3]}
Due date : {i_split[4]}
Completed : {i_split[5]}
    ''')
        pass

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")