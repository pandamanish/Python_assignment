import string

def check_password_strength(password):
    # Initialize flags to check different criteria
    upper_check = False
    lower_check = False
    digit_check = False
    special_char_check = False
    
    # List to store validation messages
    check_unsolved = []
    
    # Check minimum length requirement
    if len(password) < 8:
        check_unsolved.append("*Length is too short (Minimum 8 Characters)\n")
    
    # Iterate over each character in the password to check criteria
    for i in password:
        if i.isupper():
            upper_check = True
        if i.islower():
            lower_check = True
        if i.isdigit():
            digit_check = True
        if not i.isalnum():
            special_char_check = True
    
    # Check if all required criteria are met
    if not upper_check:
        check_unsolved.append("*Password must include at least 1 Uppercase letter\n")
        
    if not lower_check:
        check_unsolved.append("*Password must include at least 1 Lowercase letter\n")
        
    if not digit_check:
        check_unsolved.append("*Password must include at least 1 Numeric digit\n")
        
    if not special_char_check:
        check_unsolved.append("*Password must include at least 1 Special character\n")
    
    # If there are validation messages, print them and return False
    if check_unsolved:
        print("Password is not Strong!! Please find the following changes:\n")
        for check in check_unsolved:
            print(check)
        return False
    else:
        # If all criteria are met, return True
        return True

# Main program loop to get password input and check its strength
while True:
    password = input("Enter a strong password: ")
    if check_password_strength(password):
        print("Password is Strong!!")
        break
    else:
        # If password is not strong, prompt for input again
        continue
