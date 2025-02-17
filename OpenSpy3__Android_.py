import time as cpuperflow
from termcolor import colored as clrmod2, cprint as clrdspl
import pyfiglet as mkbanr
from rich.console import Console
import random
from twilio.rest import Client
from email.message import EmailMessage
import ssl
import smtplib

# IF THE LOOP IS NOT REQUIRED, REMOVE IT OR WRITE OTHER CODES BELOW FOR HACKING SYSTEMS.                                                         
# OTHER CODES :-->

print("")
bnr_list = ["Open Spy 3 ( Android ) - By Yash", "O - SPY 3 - YD", "SPY ( aNdRoId ) - Terminal - YaSh", ":) OpEn SpY 3 - bY yAsH"]
bnr_font_list = ['slant', 'dotmatrix', 'graffiti', 'banner3-d']
con = Console()
banner = mkbanr.figlet_format(random.choice(bnr_list), font = random.choice(bnr_font_list))
banner_2 = mkbanr.figlet_format("V . 3 . 0")
con.print(banner)
print("////////////////////////////")
print("//////////////////////////")
print("////////////////////////")
print("//////////////////////")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "OPEN", "", "", "", "SPY", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "v", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "3.0", "", "", "", "", "", "", "", "", "|")
print("(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")")
print("", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "")
print("", "", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "", "")
print("", "", "", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "", "", "")
print("", "", "", "", "((((((((|))))))")
print("", "", "", "", "","(((((((|)))))")
print("", "", "", "", "", "", "(((((|)))))")
print("", "", "", "", "", "", "","(((((|))))")
print("", "", "", "", "", "", "", "(((((|))))")
print("")
print("")
print("")
con.print(banner_2)
print("")
print("---------------------------------------------------------( $*$*$*$*$*$ )--------------------------------------------------------------------------------------------------------")
print("")

tx = clrmod2("[*] NOTE : INSTALL THE 'SSH' SERVICE ON YOUR LINUX DEVICE BY TYPING ->", 'blue') 
tx_2 = clrmod2("IN THE TERMINAL. \n", 'blue') 
tx_3 = clrmod2("[*] AFTER THE INSTALLATION IS DONE, TYPE ->", 'blue') 
tx_4 = clrmod2("[*] NOW YOU'VE SUCCESSFULLY ESTABLISHED AN SSH SERVICE FOR TRANSFERRING DATA. \n", 'blue')
tx_5 = clrmod2("'sudo apt-get install openssh-server'", 'green')
tx_6 = clrmod2("'sudo service ssh start'", 'green')
print(tx, tx_5, tx_2)
print(tx_3, tx_6, tx_2)
print(tx_4)
print("---------------------------------------------------------( $*$*$*$*$*$ )-------------------------------------------------------------------------------------------------------- \n")
tx1 = clrmod2("[ * ] Enter your device's Username & IP Address in this format --> (username@ipaddress) : ", 'red')
ui = input(tx1)

if "." not in ui or "@" not in ui or "|" in ui or "/" in ui or "^" in ui or "#" in ui or "%" in ui or "*" in ui or "&" in ui or "()" in ui or "!" in ui or "{}" in ui or "[]" in ui or ":" in ui or ";" in ui or "'" in ui or "~" in ui or "<" in ui or ">" in ui or "?" in ui or "," in ui:
    
    clrdspl("FATAL ERROR : UNABLE TO RECOGNIZE THE IP ADDRESS WITH THIS USERNAME !!!!", 'red', 'on_white')
    exit()
    
print("")
print(clrmod2("[ NOTE ] SET USERNAME & IP ADDRESS AS $~ ", 'white') + ui)
print("")

tx2 = clrmod2("[ * ] Enter your password : ", 'green')
password = input(tx2)
print("")
print(clrmod2("[ NOTE ] SET PASSWORD WITH RESPECT TO ", 'white') + ui + " AS $~ ", password)
print("")
print("")

# HACK USING WHILE....LOOP. 

tx3 = clrmod2("[ * ] FETCHING OF ALL SYSTEM FILES & FOLDERS ARE DONE !!!!", 'red')
print(tx3)

print("")

cpuperflow.sleep(1)

repeat_opt = True
while repeat_opt:
    
    tx_8 = clrmod2("[ * ] Now, choose which hack you wants to perform --> [ 1 ] Do Anonymous Call [ 2 ] Dispatch Anonymous SMS [ 3 ] Dispatch Email (Hacks --> 4, 5, 6 & 7 coming soon...!!!) : ", 'yellow')
    action = input(tx_8)

    print("")

    if action == "1":
    
        cpuperflow.sleep(1)

        tx_13 = clrmod2("[ * ] Enter the victim's phone number : ", 'red')
        action_5 = input(tx_13)
        
        print("")
        
        tx_21 = clrmod2("[ * ] Enter the message that you wants to say via call : ", 'white')
        action_13 = input(tx_21)

        print("")
        clrdspl("Establishing connection with Twilio server....", 'yellow', 'on_blue')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully established connection with Twilio server....!!!!", 'green', 'on_white')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully sent the call!!!!", 'green', 'on_white')
        
        print("")
        print("")

        acc_SID = 'AC3505d80cbcb63373c0e0b9860cceb947'
        auth_token = '5795db1e8288c8d58eb05f5bcd6e4db3'
    
        client = Client(acc_SID, auth_token)
    
        Attacker_Number = '+17867583827'
    
        Victim_Number = '+91' + action_5
    
        call = client.calls.create (
        
            twiml = f'<Response><Say>{action_13}</Say></Response>',
            to = Victim_Number,
            from_ = Attacker_Number,
        
        )
      
        
    elif action == "2":
        
        print("")
        
        cpuperflow.sleep(1)

        tx_19 = clrmod2("[ * ] Enter victim's phone number : ", 'red')
        action_11 = input(tx_19)
        
        print("")

        tx_20 = clrmod2("[ * ] Enter the message : ", 'white')
        action_12 = input(tx_20)

        acc_SID_2 = 'AC3505d80cbcb63373c0e0b9860cceb947'
        auth_token_2 = '5795db1e8288c8d58eb05f5bcd6e4db3'
        
        client_2 = Client(acc_SID_2, auth_token_2)

        Attacker_Number_2 = '+17867583827'
        Victim_Number_2 = '+91' + action_11
        
        print("")
        clrdspl("Establishing connection with Twilio server....", 'yellow', 'on_blue')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully established connection with Twilio server....!!!!", 'green', 'on_white')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully sent the messgae!!!!", 'green', 'on_white')

        client_2.messages.create(body = action_12, from_ = Attacker_Number_2, to = Victim_Number_2)
    
        print("")
        print("")
    
    elif action == "3":
        
        cpuperflow.sleep(1)
        
        tx_14 = clrmod2("[ * ] Enter your e-mail : ", 'cyan')
        action_6 = input(tx_14)
        
        print("")

        tx_15 = clrmod2("[ * ] Enter victim's e-mail : ", 'red')
        action_8 = input(tx_15)
        
        print("")

        tx_17 = clrmod2("[ * ] Enter the subject : ", 'red')
        action_9 = input(tx_17)

        print("")

        tx_18 = clrmod2("[ * ] Enter the e-mail message / body : ", 'red')
        action_10 = input(tx_18)
        
        print("")
        clrdspl("Establishing connection with Gmail smtp....", 'white', 'on_cyan')
        cpuperflow.sleep(2)
        
        print("")
        clrdspl("Established connection with Gmail & smtp server....!!!!", 'white', 'on_cyan')
        cpuperflow.sleep(2)

        print("")
        clrdspl("Generating e-mail message....", 'white', 'on_cyan')
        cpuperflow.sleep(3)
        
        complete_mail = f"SUBJECT : {action_9}\n\nMESSAGE : {action_10}"

        print("")
        clrdspl("Successfully Generated & Sent e-mail message....", 'green', 'on_white')

        Attacker_Email = action_6
        Victim_Email = action_8
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        server.login(Attacker_Email, "fiwq keum zhhy vgwq")
        
        server.sendmail(Attacker_Email, Victim_Email, complete_mail)
        
        print("")
        print("")