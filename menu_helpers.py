def helper_sec_menu(result):
    
    print("="*50)
    print(f"Welcome {result['user']['Fname']}".center(50))
    print("="*50)
    print("1- View All Project")#done
    print("2- Add Project")#done
    print("3- Delete a Project")#done
    print("4- Edite Project")#done
    print("5- Logout")
    choice = input("Enter your choice : ")
    return choice


def helper_first_menu():
    print("="*50)
    print("=Welcome to Crowd-Funding=".center(50))
    print("="*50)
    print("1- Register")
    print("2- Login")
    print("3- Exit")
    choice = input("enter your choice Number: ")
    return choice


