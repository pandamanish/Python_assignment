import string
password=input(str("input password\n"))

#print(password)

def check_password_strength(password):
    upper_check=False
    lower_check=False
    digit_check=False
    special_char_check=False
    flag=0
    if len(password)<=8:
        print("the length is too short")
        
    
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
        print("Upper case not provided")
        return
    if not lower_check:
        print("Lower case not provided")
        
        return
    if not digit_check:
        print ("Numeric value not provided")
      
        return
    if not special_char_check:
        print("Special character is not provided")
        
        return
   
    print("Password is strong")
    return True
    



if not check_password_strength(password):
    print("Password is not Strong")
