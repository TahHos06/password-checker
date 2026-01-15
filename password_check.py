#Password Checker based on NIST SP 800-63B (NIST Password Guidelines)
common_passes = set() #A set of common passwords
with open("C:/Users/hossa/Downloads/archive/rockyou.txt", "r", encoding="latin-1") as file:
    for i, line in enumerate(file):
        if i >= 100000:
        
            break
        line = line.lower()
        common_passes.add(line.strip())


def password_length_check(password): #This function checks if password is between 8 and 64 characters
    if len(password) <= 64 and len(password) >= 8: #NIST RECOMMENDS HAVING AT LEAST 64 CHARACTERS AS A MINIMUM MAXIMUM TO ALLOW FOR SECURE PHRASES
        return True
    elif (len(password) > 64):
        return False
    else:
        return False
    
def common_password_check(password): #This function checks if the password is a common/compromised password based on the list above
    if password in common_passes:
        return False
    else:
        return True

def repeated_chars_check(password): #This functions checks if the password is only comprised of one character like "aaaaaaaa" or "bbbbbbb"
    if (len(set(password)) == 1):
        return True
    else:
        return False

def pattern_check(password): #This function checks if the password is only comprised of a pattern
    pattern_exists = False
    for i in range(len(password)): #this loop essentially guesses and checks for patterns by seeing if multiplying it by a certain number returns the pattern.
        pattern = password[0:i+1] 
        #print(pattern)
        #print(len(pattern))
        if ((pattern * (len(password) // len(pattern))) == password) and (len(pattern) != len(password)): #Tests if the pattern repeats a certain number of times to create the password
            pattern_exists = True
            break
        
    return pattern_exists
            

def main():
    password = input("Enter a password: ")
    password = password.strip()
    password = password.lower()
    user_input = ""

    while user_input != "x":
        user_input = input("## MAIN MENU ##\nWhat would you like to do?:\na- add new password\nx- exit program\nl- check password length\nc- check for common/compromised passwords\nr- check if password is only compromised of repeated characters\np- check if password is only comprised of patterns\ne- go through all checks and get score for password\n-----> ")
        user_input = user_input.lower()
        
        if user_input == "a":
            password = input("Enter a new password: ")
            password = password.strip()
            password = password.lower()
        
        elif user_input == "l":
            if password_length_check(password):
                print("The password passes the length check.")
            else:
                print("Password is either too short (less than 8 characters) or too long (more than 64 characters)")
        
        elif user_input == "c":
            
            if common_password_check(password):
                print("Password passes the common/compromised password check.")
            else:
                print("Password is common or compromised. Please enter new password.")
        
        elif user_input == "r":
            if repeated_chars_check(password):
                print("Password only consists of one character. Please enter new password.")
            else:
                print("Password passes repeated characters test.")

        elif user_input == "p":
            if pattern_check(password):
                print("You're password is compromised of an easy pattern. Please enter a new password.")
            else:
                print("Password passes the pattern check.")
        
        elif user_input == "e":
            count = 0
            if password_length_check(password):
                print("The password passes the length check.")
                print("")
                count += 1
            else:
                print("Password is either too short (less than 8 characters) or too long (more than 64 characters)")
                print("")
            
            if common_password_check(password):
                print("Password passes the common/compromised password check.")
                print("")
                count += 1
            else:
                print("Password is common or compromisd. Please enter new password.")
                print("")
            
            if repeated_chars_check(password):
                print("Password only consists of one character. Please enter new password.")
                print("")
            else:
                print("Password passes repeated characters test.")
                print("")
                count += 1
            
            if pattern_check(password):
                print("You're password is compromised of an easy pattern. Please enter a new password.")
                print("")
            else:
                print("Password passes the pattern check.")
                print("")
                count +=1
            
            if count == 4:
                print("🟢 - Password is Strong!")
            elif count == 3 or count == 2:
                print("🟡- Password is almost there!")
            elif count == 1 or count == 0:
                print("🔴- Weak Password, do not use!")
    print("Exiting Program...Goodbye!")


if __name__ == "__main__":
    main()