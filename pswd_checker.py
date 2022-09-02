#requirements for a password to be strong
# 8 or more characters
#Combination of letters (upper and lower), numbers , and special symbols
# DOES NOT CONTAIN any words, names, phrases

def upp_low_alphabet():
    upper_case = []
    lower_case = []
    for i in range(97, 123):
        lower_case.append(chr(i))
    for i in range(65, 91):
        upper_case.append(chr(i))
    combined = upper_case + lower_case
    return combined
        
def check_cases(usr_list):
    res = False
    special = ['!', '@', '#', '$', '%' , '^', '&', '*', '(', ')']
    for i in usr_list:
        #we would have to create corner cases here
        if(i in upp_low_alphabet() or i in special or len(usr_list) >= 8):
            res = True
            break
    if(res == True):
        print("The password you entered is strong!")
    else:
        print("The password does not have capital letters and special characters and is under 8, add some!")

def main():
    usr_input = input("Enter a password you want me to check: ")
    usr_list = []
    for i in usr_input:
        usr_list.append(i)
    check_cases(usr_input)

main()
