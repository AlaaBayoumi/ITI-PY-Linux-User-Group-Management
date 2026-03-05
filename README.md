# ITI-PY-Linux-User-Group-Management


A simple **Python CLI tool** for managing Linux users and groups using system administration commands.

This tool provides an easy way for system administrators to manage user accounts and groups directly from a command-line interface.

---

## Features

* Add new users
* Modify existing users
* Delete users
* List system users
* Add groups
* Modify groups
* Delete groups
* List groups
* Lock user accounts
* Unlock user accounts
* Change user passwords

---

## Requirements

* Linux Operating System
* Python 3.x
* Root privileges

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/linux-user-manager.git
```

Enter the project folder:

```
cd linux-user-manager
```

Run the program:

```
sudo python3 user_manager.py
```

---

## Usage

When running the program, a menu will appear:

```
====== Linux User Manager ======

1 Add User
2 Modify User
3 Delete User
4 List Users
5 Add Group
6 Modify Group
7 Delete Group
8 List Groups
9 Disable User
10 Enable User
11 Change Password
12 About
13 Exit
```

Choose the desired operation and follow the instructions.

---

## Example

Add a new user:

```
Enter new username: testuser
Enter password: ********
```

---

## Security Note

This tool must be run with **root privileges** because it uses Linux system commands such as:

* `useradd`
* `usermod`
* `userdel`
* `groupadd`
* `groupmod`
* `groupdel`

---

## Disclaimer

This project is intended for **educational and system administration practice**.
Use carefully on production systems.

---

## Author

Developed using **Python for Linux system administration automation**.
