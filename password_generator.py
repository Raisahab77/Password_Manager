import string
import random
from cryptography.fernet import Fernet

# -------------------------------------- Encryption Key ------------------------------------
key = b'09sK__iqyskrgwjMIviEX-I8Z-iPvkdoSJTAVzw_jKY='


fernet = Fernet(key)


def encrypt_message(message):
    """
    This function takes Original password as input
    and convert it in cypher text.
    """
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decrypt_message(encMessage):
    """
    This function takes Input the encoded password
    and decode it using the same key in its original form.
    """
    decMessage = fernet.decrypt(encMessage).decode()
    return decMessage

data = {}                                           #dictonary          


def generate_password () :
    """
    This function generate password and ask user to save the
    password if user wants to save the password it ask for
    account name and save it in the password.txt file 
    it uses cryptography to encrypt the password so no one can
    see password directly using text file.
    """
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
        generate_password()

    save = input("Do you want to save this Password ?? y/n : ")
    if save=='y':
        account_name = input("For which account you want to store this password:")
        #------------------------ Creating password in password.txt file ----------------------
        with open ("password.txt","a") as f:
            #------------------ Here we Encrypt password using encrypt_message function -------
            encrypted_password = encrypt_message(password)   #Here password that we generate
            f.write(f"{account_name}:{encrypted_password}\n")
            print(f"{account_name}:{encrypted_password}")
    else:
        again = input("Do you want a new password ?? y/n :")
        if again=='y':
            generate_password()  
        else:
            exit()
      
def get_password():
    """
    This function ask user to input account name for which user wants
    password and open password.txt and read password.txt line by line 
    if account name present than it fetch account password which is in
    encrypted form and it decrypt password and show to user.
    """
    #------------- flag variable become true if it get account name --------------
    flag = False
    account_name = input("Enter account name to get password :")
    with open ("password.txt","r") as f:
        for line in f:
            line = line.replace(":", " ")
            # This line returns a list
            line = line.split()
            # here first element of list is account name which is line[0]
            if line[0] == account_name:
                #---------------- we initlize flag to true --------------------- 
                flag = True
                # Here line[1] is password of account
                encMessage = line[1]
                # encrypted message is in string form to decrypt it we have to convert it in bytes
                # bytes is look like -> b'dhfgfhejhh' we have to convert it into string 
                # In this line we remove < ' > using replace
                encMessage = encMessage.replace("\'","")
                # In this line we remove only first character of string which is b
                encMessage = encMessage[1:]
                # In this line we get plain string like  -> gwjgashjfsaha
                # now we type cast string to bytes 
                encMessage = bytes(encMessage,"utf-8")
                print(type(encMessage))
                # To decrypt password we must have bytes data otherwise it through error
                password = decrypt_message(encMessage)
                print(password)      
                print(type(password))      
                print(f"password for {line[0]} is {password}")   
    # ------------------- If Flag value is False than it shows account not found ------------- 
    if flag == False:
        print("Account not found :")

def mainWindow():
    option = int(input("1. Generate password :\n2. Check Password :\n3. Exit \nChoose a option :- "))

    if option==1:
        generate_password()
    
    elif option==2:
        get_password()  
    
    elif option==3:
        exit()
    
    else:
        print("wrong choice")
        mainWindow()
            
if __name__ == '__main__':
    while True:
        mainWindow()
        