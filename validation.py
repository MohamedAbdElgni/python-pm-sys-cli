import json
import re
from datetime import datetime
data_path='data.json'


#! to be enhanced
try:
    mfile = open(data_path, 'r')
    mfile.close()
except FileNotFoundError:
    with open(data_path, 'w') as f:
        json.dump([], f, indent=4)
        f.close()

myfile = open(data_path, 'r')
data = json.load(myfile)    


curr_user={
    "Fname": "",
            "Lname": "",
            "Email": "",
            "Password": "",
            "Phone": "",
            "Projects":[]
}

curr_user_info={
    "Email": "",
    "Password": ""
}

curr_user_data={
    "Fname": "",
    "Lname": "",
    "Email": "",
    "Password": "",
    "Phone": "",
    "Projects":[]
}

other_users_data=0


def get_str_input(to_get="first name"):
    while True:
        str_ = input(f"Enter your {to_get.lower()}: ")
        if not re.fullmatch("^[a-zA-Z]{3,10}$", str_.lower()):
            print ("error")
        else:
            return str_.lower()
            
        

        
def get_password_input(status="reg"):
    while True:
        password = input("Enter your password: ")
        #! to be enhanced
        if not re.fullmatch("^[0-9]{3,4}$", password):
            print ("error format")
        else:
            if status == "reg":
                confirm_password = input("Confirm your password: ")
                if password != confirm_password:
                    print ("passwords do not match")
                else:
                    return password
            else:
                return password
            
        
def get_email_input(status="reg"):
    
        while True:
            email = input("Enter your email: ")
            # ! to be enhanced
            if not re.fullmatch(r"^\S+@\S+\.\S+$", email.lower()):
                print("Error: Invalid email format.")
            else:
                if status == "reg":
                    for user in data:
                        if email.lower() == user['Email'].lower():
                            print("Error: Email already exists.")
                            break
                    else:
                        return email.lower()
                else:
                    for user in data:
                        if email.lower() == user['Email'].lower():
                            return email.lower()
                    else:
                        print("Error: Email not found.")




def get_phone_input():
    while True:
        phone = input("Enter your phone number: ")
        #  with 010 or 011 or 012
        if not re.fullmatch("^(010|011|012)[0-9]{8}$", phone):
            print ("error format")
        elif phone in [user['Phone'] for user in data]:
            print ("phone already exist")
        else:
            return phone
            
        
        
def regester_new_user():
    print("*"*50)
    print("Enter your data to regester")
    curr_user["Fname"]=get_str_input("first name")
    curr_user["Lname"]=get_str_input("last name")
    curr_user["Email"]=get_email_input()
    curr_user["Password"]=get_password_input()
    curr_user["Phone"]=get_phone_input()
    curr_user["Projects"]=[]
    data.append(curr_user)
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=4)
        f.close()
    print("user added successfully")
    return {'user':curr_user, 'data':data, 'status':True, 'ops':"reged"}

def login_user():
    print("*"*50)
    print("Enter your data to login")
    curr_user_info["Email"]=get_email_input("log")
    curr_user_info["Password"]=get_password_input("log")
    for user in data:
        if user["Email"]==curr_user_info["Email"] and user["Password"]==curr_user_info["Password"]:
            print("user logged in successfully")
            curr_user_data["Fname"]=user["Fname"]
            curr_user_data["Lname"]=user["Lname"]
            curr_user_data["Email"]=user["Email"]
            curr_user_data["Password"]=user["Password"]
            curr_user_data["Phone"]=user["Phone"]
            curr_user_data["Projects"]=user["Projects"]
            return {'user':curr_user_data, 'data':data, 'status':True, 'ops':"loged"}
            
    else:
        print("user not found")
        login_user()



def ask_prog_name():
    while True:
        prog_name = input("Enter your project name: ")
        if not re.fullmatch("^[a-zA-Z]{3,15}$", prog_name.lower()):
            print ("Please enter a valid project name.")
        else:
            return prog_name.lower()
        

def ask_prog_details():
    while True:
        prog_details = input("Enter your project details: ")
        if not re.fullmatch("^[a-zA-Z0-9]{5,25}$", prog_details.lower()):
            print ("Please enter a valid project details.")
        else:
            return prog_details.lower()
        

def ask_prog_target():
    while True:
        prog_target = input("Enter your project target: ")
        if not re.fullmatch("^[0-9]{3,5}$", prog_target):
            print ("Please enter a valid project target.")
        else:
            return f"{prog_target} EGP"
        

def ask_prog_date():
    
    while True:
        start_date = input("Enter your project start date (dd/mm/yyyy): ")
        try:
            start_date = datetime.strptime(start_date, "%d/%m/%Y")
            break
        except:
            print("Please enter a valid Start date.")
    while True:
        end_date = input("Enter your project end date (dd/mm/yyyy): ")
        try:
            end_date = datetime.strptime(end_date, "%d/%m/%Y")
            break
        except:
            print("Please enter a valid End date.")
    
    if end_date < start_date:
        print("End date should be after start date.")
        ask_prog_date()
    else:
        return {"Startdate":start_date, "Enddate":end_date}
    
    

def del_project(result):
    print("="*50)
    print("=Enter project Number to Delete=".center(50))
    print("="*50)
    i=0
    input_range=[]
    if result['user']['Projects'] == []:
        print("No Projects found")
        return
    while i<len(result['user']['Projects']):
        try:
            print(f"{i+1}- {result['user']['Projects'][i]['Title']}")
            input_range.append(str(i+1))
            i+=1
        except KeyError:
            print("No Projects")
            return
    
    choice = input("Enter your choice : ")
    if choice in input_range:
        result['user']['Projects'].pop(int(choice)-1)
        with open('data.json', 'w') as f:
            json.dump(result['data'], f, indent=4)
            f.close()
        print("Project deleted successfully")
    else:
        print("Invalid choice")
        
    x=input("press any to continue")
    return


def update_project(result):
    
    print("="*50)
    print("=Enter project Number to Update=".center(50))
    print("="*50)
    i=0
    input_range=[]
    if result['user']['Projects'] == []:
        print("No Projects found")
        x=input("press any to continue")
        return
    while i<len(result['user']['Projects']):
        try:
            print(f"{i+1}- {result['user']['Projects'][i]['Title']}")
            input_range.append(str(i+1))
            i+=1
        except KeyError:
            return
    choice = input("Enter your choice : ")
    if choice in input_range:
        selected_project=result['user']['Projects'][int(choice)-1]
        print("="*50)
        print(f"=Update {selected_project['Title']}=".center(50))
        print("="*50)
        while True:
            print("1- Update Project Name")
            print("2- Update Project Details")
            print("3- Update Project Target")
            print("4- Update Project Date")
            print("5- Back")
            choice = input("Enter your choice : ")
            if choice == "1":
                selected_project['Title']=ask_prog_name()
            elif choice == "2":
                selected_project['Details']=ask_prog_details()
            elif choice == "3":
                selected_project['Target']=ask_prog_target()
            elif choice == "4":
                selected_project['Dates']=ask_prog_date()
            elif choice == "5":
                break
            else:
                print("Invalid choice")
                continue
        with open('data.json', 'w') as f:
            json.dump(result['data'], f, indent=4)
            f.close()
        print("Project updated successfully")
    else:
        print("Invalid choice")
    x=input("press any to continue")
    return


    