import smtplib
import os
import sys
from halo import Halo




txt_file = open("spamList.txt", "r")
file_content = txt_file.read()
#print("The file content are: ", file_content) #FOR TESTING PURPOSES, IGNORE THIS COMMENT!

content_list = file_content.split(",")
txt_file.close()
#print("The list is: ", content_list) #FOR TESTING PURPOSES, IGNORE THIS COMMENT!


def emailMechanism():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection: 
            print("\n#--------------------------------------#\n")
            clientEmail = content_list 
            print("Sending Emails....")
            

            spinner = Halo(text='Loading', spinner='dots')
            spinner.start()

            email_address = 'yourEmail@gmail.com' #SENDERS EMAIL GOES HERE! (REPLACE CURRENT DISPLAYED EMAIL)
            email_password = 'yourAppPassword' #USE YOUR EMAIL ACCOUNTS APP PASSWORD HERE TO GET PROGRAM RUNNING! REPLACE "n/a" WITH SAID  APP PASSWORD!#
            connection.login(email_address, email_password )
            connection.sendmail(from_addr=email_address, to_addrs=clientEmail, 
                msg="subject:" + s + "\n\n "  + f + "")
            

            print("\n#--------------------------------------#\n")
            spinner.stop()
            print("Emails Sent successfully!\n")
          


def satisfactory():
    print("\n\n#--------------------#\n\n")
    satisfactory1=input("Is this satisfactory (y/n): ")
    if satisfactory1 == "y":
        emailMechanism()
        
    if satisfactory1 == "n":
        print("\n\n#----------RESTARTING PROGRAM----------#\n\n")
        os.execl(sys.executable, sys.executable, *sys.argv)

def finalEmail():
    print ("\n\n#----------Here is your final email:----------#\n\n ")


#EVERYTHING HERE AND BELOW IS MOSTLY CUSTOMIZABLE, AND DOES NOT RELATE TO THE OVERALL FUCTIONALITY OF THIS TOOL.
#THOUGH, BE CAREFUL TO KNOW HOW EVERYTHING WORKS FIRST!#

print('Hello! and welcome to the email spam bot tool! \n\n')
subject=input("To get started, is the email subject line pre-set? (y/n): ")
if subject=="y":
    s="#put whatever you want to input in here#"
if subject=="n":
    s=input("please insert your desired subject line here: ") #REPLACE STRING CONTENT WITH YOUR DESIRED SUBJECT LINE!




prewritten=input("\n\nIs this email prewritten? (y/n): ")
if prewritten=="y":
    customtext=("##put whatever you want here:## ") #PUT YOUR OWN CUSTOM MESSAGE HERE, OR REPLACE VARIABLES CONTENT WITH A CSS/HTML TEMPLATE IF DESIRED!#
    f=customtext
    print ("Here is your final email: \n" "Subject:"+s+ "\n\nBody:\n" + customtext + "")
    satisfactory()

if prewritten=="n":
    email=input("what do you want your email to say? : ")
    f=email
    print ("Here is your final email: \n\n" "Subject:"+s+ "\n\n\n"+ email + "")
    satisfactory()
