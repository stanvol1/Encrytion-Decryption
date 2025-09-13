import time
import os
import random

m = "message.txt"

loop = True
new_line = False

if not os.path.isfile(m):  
    open("message.txt", "x")
    
else:
    new_line = True
    
while loop:
    offset_list = []
    selection = input("Write a new message [w] or exit [x] ")
    if selection == "w":
        message = input("what message would you like to encrypt? ")
        encryptedmsg = ""
        for ch in message:
            random_int = int(random.randint(-25, 25))
            randoffset = random_int
            offset_list.append(randoffset)
            print(randoffset)
            asc = 32 + ((ord(ch) + randoffset - 32) % 95)
            ench = chr(asc)
            encryptedmsg += ench
        print(encryptedmsg)
        key = (", ".join(map(str, offset_list)))
        with open("message.txt", "a", encoding="utf-8") as f:
            if not new_line:
                f.write(encryptedmsg + " ")
                f.write(key + "\n")
            else:
                f.write("\n" + encryptedmsg + ", ")
                f.write(key + "\n")
        time.sleep(5)
    elif selection == "x":
        loop = False
        break
    else:
        print("it's case sensitive, w or x")
        
