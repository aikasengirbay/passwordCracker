import mmap
import getpass



print
print
print
print
print
print
print
print
print
print
print
print
print
print"""
                        |^C^C0,8            ^C^C0,12|  ^C^C0,14| |^C^C0,12
                        |C^C0,8             ^C^C0,12|__^C^C0,14|_|^C^C0,12
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
                        (^C^C0,14___________^C^C0,12"""



print
print"                                 Terminal-based Password Cracker          "
print 
print "                                            *** - ***                    "
print 
print "                          Check if your password compromised by a hackers "


# def find_password():
#     """Gives option to edit/delete items the list"""
    
#     # your_password = raw_input("Enter a password > ")
#     your_password = getpass.getpass("Enter a password > ")
#     your_password = str(your_password)
#     if len(your_password) <= 5:
#         print
#         print "Your password can be cracked by the time you sneeze"
#         print
#         print  "!!! Remember, Long password = Strong password !!!"
#         print 
#     elif len(your_password) <= 7:
#         print
#         print "Your password can be cracked in the hour you get your drive-thru order"
#         print
#         print  "!!! Remember, Long password = Strong password !!!"
#         print
#     elif len(your_password) <= 9:
#         print
#         print "Your password can be cracked in the hour you spend doing yoga"
#         print
#         print  "!!! Remember, Long password = Strong password !!!"
#         print  
#     elif len(your_password) <= 14:
#         print
#         print "Your password can be cracked by your next birthday"
#         print
#         print  "!!! Remember, Long password = Strong password !!!"
#         print 
#     elif len(your_password) >= 15:
#         print 
#         print"*** Wowwww!!!! ****"
#         print "Your password takes longer to crack than raising a child "
#         print 
#         print "!!! But I still know your password !!!"


#     with open('rockyou.txt', 'rb') as f:
#         m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        
#         if m.find(your_password) != -1:
#             print 
#             print "*** {} *** Password found".format(your_password)
#             print 
#         else:
#             print 
#             print "Password not found"
#             print
#             print "!!! Remember, Long password = Strong password !!!"
    
#     test_file = open('rockyou.txt', mode = "a")
#     test_file.write("\r" + your_password)
#     test_file.close()
  



def display_main_menu():
    """Displays main options, takes in user input, and calls find_password function."""
   
    print
    print
    print "             Hey...."
    print
    user_options = "   Would you like to test a password, Yes/No ? "
    print
    


    while True:
        answer = raw_input(user_options)
        answer = answer.lower()
        if answer == "yes":
            print 
            print "      !!! Never Enter Your Real Password !!!"
            print 
            # find_password()
            # your_password = getpass.getpass("Enter a password > ")
            your_password = getpass.getpass("   Enter a password > ")
            your_password = str(your_password)
           
            with open('rockyou.txt', 'rb') as f:
                m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
                if m.find(your_password) != -1:
                    print 
                    print "                                 *** {} *** Password found ".format(your_password)
                    print
                    if len(your_password) <= 0:
                        print
                        print
                        print "                         Give me Your Password"
                        print
                    elif len(your_password) <= 5:
                        print "                      Your password is only " + str(len(your_password)) + " characters" + " & it can be cracked while you sneeze"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print 
                    elif len(your_password) <= 7:
                        print 
                        print "                       Your  " + str(len(your_password)) + " characters password can be cracked in the hour you get your drive-thru order"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print
                    elif len(your_password) <= 9:                
                        print   
                        print "                       Your " + str(len(your_password)) + " characters password can be cracked in the hour you spend doing yoga"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print  
                    elif len(your_password) <= 14:
                    
                        print
                        print "                      Your  password is " + str(len(your_password)) + " characters" + " & it can be cracked by your next birthday"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print 
                    elif len(your_password) >= 15:
                    
                        print  
                        print"                                         *** Wowwww!!!! ****"
                        print "                      Your " + str(len(your_password)) + " characters" + " password could take longer to crack than raising a child "
                        print
                        print "                              !!! But hackers still know your password !!!"
                        print

                       
                else:
                    print   "                                        Password not found!"
                    print 
                    if len(your_password) <= 0:
                        print
                        print
                        print "                         Give me Your Password"
                        print
                    elif len(your_password) <= 5:
                        print "                      Your password is only " + str(len(your_password)) + " characters" + " & it can be cracked while you sneeze"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print 
                    elif len(your_password) <= 7:
                        print 
                        print "                       Your  " + str(len(your_password)) + " characters password can be cracked in the hour you get your drive-thru order"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print
                    elif len(your_password) <= 9:                
                        print   
                        print "                       Your " + str(len(your_password)) + " characters password can be cracked in the hour you spend doing yoga"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print  
                    elif len(your_password) <= 14:
                    
                        print
                        print "                      Your  password is " + str(len(your_password)) + " characters" + " & it can be cracked by your next birthday"
                        print
                        print  "                          !!! Remember, Long password = Strong password !!!"
                        print 
                    elif len(your_password) >= 15:
                    
                        print  
                        print"                                         *** Wowwww!!!! ****"
                        print "                      Your " + str(len(your_password)) + " characters" + " password could take longer to crack than raising a child "
                        print
                        print                          
                        print

            test_file = open('rockyou.txt', mode = "a")
            test_file.write("\r" + your_password)
            test_file.close()
       
        elif answer == "no":
            print 
            print "                                          ***  Bye  ***"
            print 
            print "                      !!! Remember, Long password = Strong password !!!"
            print
            print
            print
            print
            print
            print
            break
        else:
            print "That is not an option"



display_main_menu()
