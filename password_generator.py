import string
import random
import pickle

data = {}                                 #dictonary          

def generate_password () :
    password_length = int(input("How long Password You want ??"))
    print("Which type of password you want.\n 1. PIN \n 2. Mix password(Numbers and Letter) \n 3. Hard password(Number,characters and letter)")
    password = ''
    option = int(input("Choose option : "))
    if option==1:
        s = "0123456789"
        password = random.sample(s,password_length)
        password = "".join(password)
        print(password)
    elif option==2:
        s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = random.sample(s,password_length)
        password = "".join(password)
        print(password)
    elif option==3:
        s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*!"
        password = random.sample(s,password_length)
        password = "".join(password)
        print(password)

    else:
        print("Wrong input:") 
        exit()

    save = input("Do you want to save this Password ?? y/n : ")
    if save=='y':
        account_name = input("For which account you want to store this password:")
        data[account_name] = password
    else:
        again = input("Do you want a new password ?? y/n :")
        if again=='y':
            generate_password()  
        else:
            exit()
    with open ("password","bw") as f:
        pickle.dump(data,f)

      
def get_password():
    account_name = input("Enter account name to get password :")
    with open ("password","br") as f:
        data = pickle.load(f)
    if account_name in data:
        print(f"your {account_name} password is :  {data[account_name]}")    

    else :
        print("Sorry no account found !")    

if __name__ == '__main__':
    option = int(input("1. Generate password\n2. Check Password\nChoose a option "))
    if option==1:
        generate_password()
    elif option==2:
        get_password()  
    else:
        print("wrong choice")
        exit()
    
    # with open ('password',"br") as f:
    #     data = pickle.load(f)
    # print(data) 