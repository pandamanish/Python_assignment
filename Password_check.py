import string
def password_strength(password):
    try: 
        # Initialized flags to check different criteria
        uppercase_check = False
        lowercase_check = False
        digitcase_check = False
        specialchar_check = False
        #list to append not match cases
        check_unsolved = []
        # Checked minimum length requirement of password
        if len(password) < 8:
            check_unsolved.append("*Length is too short (Minimum 8 Characters)\n")
        
        
        # Iterating over each characters in the password to match cases
        for i in password:
            if i.isupper():
                uppercase_check = True
            if i.islower():
                lowercase_check = True
            if i.isdigit():
                digitcase_check = True
            if not i.isalnum():
                specialchar_check = True
        
       
       
       
        # Checked if all required cases are met or not, if not append to check_unsolved
        if not uppercase_check:
            check_unsolved.append("*Password must be missing with atleast 1 Uppercase letter\n")
            
        if not lowercase_check:
            check_unsolved.append("*Password must be missing with atleast 1 Lowercase letter\n")
            
        if not digitcase_check:
            check_unsolved.append("*Password must be missing with atleast 1 Numeric digit\n")
            
        if not specialchar_check:
            check_unsolved.append("*Password must be missing with atleast 1 Special character\n")
        
        # Checking if the 'check_unsolved' is not empty then printing the statements
        if check_unsolved:
            print("Password is not Strong!Kindly find the changes to be made below: \n")
            for check in check_unsolved:
                print(check)
            return False
        
        else:
            
            return True
    except Exception as e:
        print(f"ERROR:{e}")





# checking if the strength is true and if not it will ask for the password again
while True:
    password = input("Enter a strong password: ")
    if password_strength(password):
        print("Hurray!! Your Password is Strong enough!!")
        break
    else:
        continue
