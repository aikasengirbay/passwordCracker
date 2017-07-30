



print "**** ---- ****"
print 
print "This is a Terminal-based password cracker"
print 

def find_password():
    """Gives option to edit/delete items the list"""
    
    your_password = raw_input("Enter a password > ")
    # your_password = my_list.index(your_password)
    test_file = open('test.csv').read()
    run_test = test_file.split("\r")

    if your_password in run_test:

        print " {} Found ".format(your_password)
    else:
        print "Is not in the list"

    # if your_password in my_list:
    #     print 
    #     print "*** {} *** password found".format(your_password)
    #     print 
    # elif your_password not in my_list:
    #     print 
    #     print "password not found"
    #     print 
    # my_list.append(your_password) 
  



# def display_main_menu(my_list):
#     """Displays main options, takes in user input, and calls view or add function."""

#     user_options = "Would you like to test your password, y/n ?"


#     while True:
#         answer = raw_input(user_options)
#         # Collect input and include your if/elif/else statements here.
#         if answer == "y":
#             find_password(my_list) 
#         elif answer == "n":
#             break
#         else:
#             print "That is not an option"

#-------------------------------------------------
 
# username = raw_input( "> ")

# if username in open('test.csv').read():
#     print " {} Found ".format(username)
# else:
#     print "Is not in the list"

# display_main_menu()


find_password()
