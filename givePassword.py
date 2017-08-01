



print "**** ---- ****"
print 
print "This is a Terminal-based password cracker"
print 

def find_password():
    """Gives option to edit/delete items the list"""
    
    your_password = raw_input("Enter a password > ")
    # your_password = my_list.index(your_password)
    test_file = open('rockyou.txt').read()
    # test_file = test_file.write()
    run_test = test_file.split("\r")

    if your_password in run_test:
        print 
        print "*** {} *** password found".format(your_password)
        print 
    elif your_password not in run_test:
        print 
        print "Password not found"
        print
    test_file = open('rockyou.txt', mode = "a")
    test_file.write("\r" + your_password)
    test_file.close()
  



def display_main_menu():
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = "Would you like to test your password, y/n ? "


    while True:
        answer = raw_input(user_options)
        if answer == "y":
            find_password() 
        elif answer == "n":
            break
        else:
            print "That is not an option"


display_main_menu()
