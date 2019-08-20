print ("Check whether the item is in the list.txt file or not")
user_password = {"name1":123, "name2":222}


def find_search(i):    
    myfile = open("list.txt")
    icecream = myfile.read()
    myfile.close()
    icecream = icecream.splitlines()
    if i in icecream:
        return "This flavour is in the list."
    else:
        return "No such flavour is in the list"

user=input("\nEnter user name - ")        
if user in user_password.keys():
    text=user_password[user]
    # print(text)
    password = int(input("\nEnter your pin - "))    
    if password == text:
        icecream_flavour = input("\nEnter flavour of icecream: ")
        print(find_search(icecream_flavour))
    else:
        print("Incorrect password!")
else:
    print("Invalid Username!") 

