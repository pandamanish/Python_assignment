import string

def check_password_strength(password):
    upper_check=False
    lower_check=False
    digit_check=False
    special_char_check=False
    check_unsolved=[]
    if len(password)<8:
        check_unsolved.append("*Length is too short(Minimum 8 Characters)\n")
        
    
    for  i in password:
        if i.isupper():
            upper_check=True
        if i.islower():
            lower_check=True
        if i.isdigit():
            digit_check=True 
        if not i.isalnum():
            special_char_check=True
    
    if not upper_check :
        check_unsolved.append("*Password must include atleast 1 Upper case\n")
        
    if not lower_check:
        check_unsolved.append("*Password must include atleast 1 Lower case\n")
        
    if not digit_check:
        check_unsolved.append("*Password must include atleast 1 Numeric value\n")
        
    if not special_char_check:
        check_unsolved.append("*Password must include atleast 1 Special character\n")
    if check_unsolved:
        print("Password is not Strong!! Please find the following changes:\n")
        for check in check_unsolved:
            print(check)
            return False
    return True

   
password=input(str("input password\n"))

if  check_password_strength(password):
    print("Password is Strong!!")
 
