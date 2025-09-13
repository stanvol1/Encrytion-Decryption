import time
import os

d = "decrypt.txt"

if not os.path.isfile(d):
    open("decrypt.txt", "x")
key = []
key_list = []
key_input = input("Input your key here ")
key.append(key_input)
key = [item.strip() for item in key_input.split(',')]
for number in key:
    key_list.append(int(number))
    
print(key_list)

text_input = input("Input your text here ")

encryptedmsg = ""
i = 0
for ch in text_input:
    asc = 32 + ((ord(ch) - key_list[i] - 32) % 95)
    i += 1
    ench = chr(asc)
    encryptedmsg += ench


with open("decrypt.txt", "a", encoding="utf-8") as f:
    f.write(encryptedmsg + "\n")


print(encryptedmsg)
