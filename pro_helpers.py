import os
import json
from validation import ask_prog_name ,ask_prog_details,ask_prog_target,ask_prog_date
def clear():
    os.system('clear')
    return

def view_all_projects(result):
    #the taples lib to be added later
    clear()
    print("="*50)
    print("=Listing Projects=".center(50))
    print("="*50)
    for user in result['data']:
         pm_name =f"{user['Fname']} {user['Lname']}"
         if user['Projects'] == []:
             continue
         else:
            for project in user['Projects']:
                print(f"Project Name: {project['Title']}")
                print(f"Project Manager: {pm_name}")
                print(f"Project Details: {project['Details']}")
                print(f"Project Totaltarget: {project['Totaltarget']}")
                print(f"Project Startdate: {project['Startdate']}")
                print(f"Project Enddate: {project['Enddate']}")
                print("="*50)
    print("="*50)
    x=input("press any to continue")
    
    return





def edite_project():
    pass
def delete_project(result):
    clear()
    print("="*50)
    print("=Select Project to Delete=".center(50))
    pass

def create_project(result):
    new_project = {}
    print("="*50)
    print("=Create a New Project=".center(50))
    print("="*50)
    new_project["Title"]=ask_prog_name()
    new_project["Details"]=ask_prog_details()
    new_project["Totaltarget"]=ask_prog_target()
    date = ask_prog_date()
    new_project["Startdate"]=date["Startdate"].strftime("%d/%m/%Y")
    new_project["Enddate"]=date["Enddate"].strftime("%d/%m/%Y")
    
    curruser = result['user']
    
    for user in result['data']:
        if user["Email"]==curruser["Email"]:
            user["Projects"].append(new_project)
            
            with open('data.json', 'w') as f:
                json.dump(result['data'], f, indent=4)
                f.close()
            print(f"Project {new_project['Title']} added successfully")
            break
    x=input("press any to continue")
    return




    

