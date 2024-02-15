import os

def clear():
    os.system('clear')
    return

def view_all_projects(result):
    clear()
    print("="*50)
    print("=Listing Projects=".center(50))
    print("="*50)
    for user in result['data']:
         pm_name =f"{user['Fname']} {user['Lname']}"
         if user['Projects'] == []:
             print(f"No Projects Found for {pm_name}")
             continue
         try:
            for project in user['Projects']:
                print(f"Project Name: {project['Title']}")
                print(f"Project Manager: {pm_name}")
                print(f"Project Details: {project['Details']}")
                print(f"Project Totaltarget: {project['Totaltarget']}")
                print(f"Project Startdate: {project['Startdate']}")
                print(f"Project Enddate: {project['Enddate']}")
                print("="*50)
         except KeyError:
                continue
    print("="*50)
    x=input("Press Enter to continue")
    
    return
    


