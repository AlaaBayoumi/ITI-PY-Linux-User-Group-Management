
import subprocess
import os



def run_cmd(cmd):
    try:
        subprocess.run(cmd, check=True)
        print("Operation completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

#  User Functions

def add_user():
    username = input("Enter new username: ")
    password = input("Enter password: ")

    run_cmd(["useradd","-m",username])
    subprocess.run(f'echo "{username}:{password}" | chpasswd',shell=True)


def modify_user():
    username = input("Enter username: ")

    print("\n1 Change Home Directory")
    print("2 Change Primary Group")
    print("3 Add user to group")
    print("4 Change Username")
    print("5 Change Shell")
    print("6 Change UID")

    choice = input("Select option: ")

    if choice == "1":
        path = input("New home directory: ")
        run_cmd(["usermod","-d",path,username])

    elif choice == "2":
        group = input("Group name: ")
        run_cmd(["usermod","-g",group,username])

    elif choice == "3":
        group = input("Group name: ")
        run_cmd(["usermod","-aG",group,username])

    elif choice == "4":
        newname = input("New username: ")
        run_cmd(["usermod","-l",newname,username])

    elif choice == "5":
        shell = input("Shell path: ")
        run_cmd(["usermod","-s",shell,username])

    elif choice == "6":
        uid = input("New UID: ")
        run_cmd(["usermod","-u",uid,username])


def delete_user():
    username = input("Username to delete: ")
    run_cmd(["userdel","-r",username])


def list_users():

    print("\n--- Users ---")

    with open("/etc/passwd") as f:
        for line in f:
            parts=line.split(":")
            if int(parts[2]) >= 1000:
                print(parts[0])


def disable_user():
    username=input("Username: ")
    run_cmd(["usermod","-L",username])


def enable_user():
    username=input("Username: ")
    run_cmd(["usermod","-U",username])


def change_password():
    username=input("Username: ")
    password=input("New Password: ")

    subprocess.run(f'echo "{username}:{password}" | chpasswd',shell=True)


#  Group Functions 
def add_group():
    name=input("Group name: ")
    run_cmd(["groupadd",name])


def modify_group():

    group=input("Group name: ")

    print("1 Change group name")
    print("2 Change GID")

    choice=input("Select option: ")

    if choice=="1":
        newname=input("New name: ")
        run_cmd(["groupmod","-n",newname,group])

    elif choice=="2":
        gid=input("New GID: ")
        run_cmd(["groupmod","-g",gid,group])


def delete_group():
    name=input("Group name: ")
    run_cmd(["groupdel",name])


def list_groups():

    print("\n--- Groups ---")

    with open("/etc/group") as f:
        for line in f:
            parts=line.split(":")
            if int(parts[2]) >= 1000:
                print(parts[0])


#  ABOUT Program

def about():

    print("\nLinux User Manager")
    print("Python System Administration Tool")
    print("Manage users and groups easily")
    print("Features:")
    print("- User Management")
    print("- Group Management")
    print("- Password Control")
    print("- Account Lock/Unlock")

def main():

    if os.getuid()!=0:
        print("Run with sudo")
        return

    while True:

        print("\n====== Linux User Manager ======")
        print("1 Add User")
        print("2 Modify User")
        print("3 Delete User")
        print("4 List Users")
        print("5 Add Group")
        print("6 Modify Group")
        print("7 Delete Group")
        print("8 List Groups")
        print("9 Disable User")
        print("10 Enable User")
        print("11 Change Password")
        print("12 About")
        print("13 Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_user()

        elif choice == "2":
            modify_user()

        elif choice == "3":
            delete_user()

        elif choice == "4":
            list_users()

        elif choice == "5":
            add_group()

        elif choice == "6":
            modify_group()

        elif choice == "7":
            delete_group()

        elif choice == "8":
            list_groups()

        elif choice == "9":
            disable_user()

        elif choice == "10":
            enable_user()

        elif choice == "11":
            change_password()

        elif choice == "12":
            about()

        elif choice == "13":
            break

        input("\nPress Enter to continue...")


if __name__=="__main__":
    main()
