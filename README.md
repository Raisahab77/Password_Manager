# Password_Manager
This is password manager created in python it generate password and can store the password in a text file and when user needs to see the password user can check the password.
Basically it is command line based program. It has three option-
1.option for generate passwords.First it ask user to input length of the password and then show three option.
    i. option generate simple password with only digits
    ii. option generates mix password with digits and upper and lower case letter
    iii. option is last option it generates complex password with numbers, characters and letters.
    After Generating password it asks to save the password if user press y then it encrypt the password and save to the password.txt file.
    In password.txt passwords are save in encrypted form so no one can directly access the password.
2. option for show password.
    If user chooses second option than it asks user for account name.
    After inputting account name it search for account name in password.txt file if account name match than if fetch password.
    After getting password it decrypt the password and show to user. 
3. Exit
