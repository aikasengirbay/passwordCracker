import mmap
import getpass



print"""
        |^C^C0,8            ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |C^C0,8            ^C^C0,12|__^C^C0,14|_|^C^C0,12
        |^C^C0,8            ^C^C0,14|____)^C^C0,12
        |^C^C0,8____________^C^C0,12|
        |^C^C0___________  _^C^C0,12|____
        |^C^C1,8  G i v e   ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8   GivE     ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8     me     ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8   M    E   ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8   y o u r  ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8  Y o u R   ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8  Password  ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8  PassworD  ^C^C0,12|  ^C^C0,14| |^C^C0,12
        |^C^C1,8  PASSWORD  ^C^C0,12|  ^C^C0,14| |^C^C0,12
        (^C^C0,14______________)^C^C0,12"""



print
print"              Terminal-based Password Cracker          "
print 
print "                         *** - ***                    "
print 
print "         Check if your password compromised by a hackers "
print 
print

def find_password():
    """Gives option to edit/delete items the list"""
    
    # your_password = raw_input("Enter a password > ")
    your_password = getpass.getpass("Enter a password > ")


    with open('rockyou.txt', 'rb') as f:
        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    
        if m.find(your_password) != -1:
            print 
            print "*** {} *** Password found".format(your_password)
            print 
	else:
            print 
            print "Password not found"
            print
    
    test_file = open('rockyou.txt', mode = "a")
    test_file.write("\r" + your_password)
    test_file.close()
  



def display_main_menu():
    """Displays main options, takes in user input, and calls find_password function."""
    
    user_options = "Would you like to test a password, Yes/No ? "
    print


    while True:
        answer = raw_input(user_options)
        answer = answer.lower()
        if answer == "yes":
            print 
            print "!!! Never Save to Enter Your Real Password !!!"
            print 
            find_password() 
        elif answer == "no":
            break
        else:
            print "That is not an option"


display_main_menu()
