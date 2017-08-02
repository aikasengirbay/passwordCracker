import mmap
import getpass



print "**** ---- ****"
print 
print "This is a Terminal-based password cracker"
print 

def find_password():
    """Gives option to edit/delete items the list"""
    
    # your_password = raw_input("Enter a password > ")
    your_password = getpass.getpass("Enter a password > ")


    with open('master.dic', 'rb') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    
        if m.find(your_password) != -1:
            print 
            print "*** {} *** password found".format(your_password)
            print 
	else:
            print 
            print "Password not found"
            print
    
    test_file = open('master.dic', mode = "a")
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
