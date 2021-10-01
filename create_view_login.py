import os
import string
import time

from cryptography.fernet import Fernet


def create_Key():
    key = Fernet.generate_key()
    with(open("key.key", "wb")) as key_f:
        key_f.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key_fer = load_key()
fer = Fernet(key_fer)

def view_Pwd():
    with(open('Pwd.txt', 'r')) as f:
        for line in f.readlines():
            data = line.rstrip()
            user_name, passw = data.split("|")
            print("Username: " + user_name + "\n" + "Password: " + fer.decrypt(passw.encode()).decode())
def create_Pwd():
    user_name = input("Please enter username: ")
    pwd = input("Please enter your password: ")
    if len(list(set(pwd)&set(string.ascii_lowercase))) > 0 and len(list(set(pwd)&set(string.ascii_uppercase))) > 0 and len(list(set(pwd)&set(string.digits))) > 0 and len(list(set(pwd)&set(string.punctuation))) > 0:
        print("Password is strong.")
        with(open("Pwd.txt", "a")) as f:
            f.write(user_name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    else:
        print("Please enter weak password. Password includes lowercase, uppercase, digits, punctuation")
        quit()
def login_system():
    countFail = 0
    opt = input(" - log: Login system\n - q: Quit\n Choose a option: ").lower()
    while True:
        if opt == "q":
            quit()
        elif opt == "log":
            print("\nLogin system:")
            username = input("Username: ")
            password = input("Password: ")
            print("Login...")
            time.sleep(1)

            if checkUserExitting(username, password):
                print("Login successfully")
                break
            else:
                print("Login failed")
                msg = input("Do you want to exit? (y/n): ").lower()
                if msg == "y":
                    quit()
                elif msg == "n":
                    continue
                else:
                    print("Please type correct answer.")
                countFail += 1
            
            if countFail > 5:
                print("You enter incorrectly username|password more than 5 times.")
                break
        else:
            print("Please type correct options next time")
            
    if countFail > 0:
        print("You login fail", countFail, "times.")



def call_CreatePwd():
    while True:
        print("Options:\n Add: add a new password\n View: show password")
        options = input("Please choose 2 options: add or view. If you wanna quit, you type Q: ").lower()
        if options == "q":
            break
        if options == "add":
            create_Pwd()
        elif options == "view":
            view_Pwd()
        else:
            print("Please type correctly options in next time.")

def checkUserExitting(username, password):
    #Check user exists in database
    with open('Pwd.txt') as f:
        for line in f:
            data = line.rstrip()
            user, passw = data.split("|")
            if username == user and password == fer.decrypt(passw.encode()).decode():
                result = True 
                break
            else:
                result = False 
    print(result)
    return result




def main():

    file = os.path.isfile('./key.key')
    if not file:
        create_Key()
    opts = input(" - 1: call_CreatePwd\n - 2: Login System\n Choose your option: ")
    if opts.isdigit():
        opts = int(opts)
    if opts == 1:
        call_CreatePwd()
    elif opts == 2:
        login_system()
    else:
        print("Please choose a correct options")
        exit()

if __name__ == '__main__':
    main()