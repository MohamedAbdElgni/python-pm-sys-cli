import json
import re
data_path='data.json'


#! to be enhanced
mfile = open(data_path, 'r')
data = json.load(mfile)
mfile.close()
    
    
print(data)

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


