import numpy as np
import sys

message = input("Enter string (whitespace will be removed):").upper()
message = message.replace(" ","")
col_sz = int(input("Enter column size:"))
if col_sz > len(message):                           #If column size entered is greater than length of the message
    col_sz = len(message)                           #then column size will reduce to length of message and
    row_sz = 1                                      #row size will be one.
else:
    for i in range(len(message)):
        if col_sz * (i+1) >= len(message):
            row_sz = i+1
            break
dif = int(row_sz * col_sz) - len(message)           #This will fill empty space in message with $
for i in range(dif):
    message += "$"

msg_lst = list()
for i in range(len(message)):                       #For loop to convert message string into list
    msg_lst.append(message[i])

tbl = np.zeros((row_sz,col_sz),dtype=str)
k = 0
for i in range(row_sz):                             #For loop to table of message.
    for j in range(col_sz):
        tbl[i,j] = msg_lst[k]
        k += 1
        if k == len(message):
            break

key = input("Enter Key(0-9):")
key_lst = list()
for i in range(len(key)):                           #For loop to convert key string into list.
    key_lst.append(int(key[i]))

if len(key_lst) != col_sz & max(key_lst) != col_sz:
    print("Unacceptable key.\nEither max column number in key is greater than column size or key is too short.")
    sys.exit("Restart program.")
print("\nOriginal string after some adjustments:\" ",message,"\" ,encrypting using Key:",key)

ciph_mat = np.zeros((row_sz,col_sz),dtype=str)
for i in range(len(key_lst)):                       #For loop for transposition of columns.
    ciph_mat[:,key_lst[i]-1] = tbl[:,i]

ciph_txt = ""
for i in range(col_sz):                             #For loop to convert cipher message list into string.
    for j in range(row_sz):
        if ciph_mat[j,i] == " ":
            ciph_txt += ""
        else:
            ciph_txt += ciph_mat[j,i]
print("\nString after encryption:",ciph_txt) 

deciph_mat1 = np.zeros((row_sz,col_sz),dtype=str)
k = 0
for i in range(col_sz):                             #For loop to rearrange cipher string into matrix/aaray
    for j in range(row_sz):
        if k < len(ciph_txt):
            deciph_mat1[j,i] = ciph_txt[k]
            k += 1
deciph_mat2 = np.zeros((row_sz,col_sz),dtype=str)
for i in range(len(key_lst)):                       #For loop for transposition of columns for decyphering.
    deciph_mat2[:,i] = deciph_mat1[:,key_lst[i]-1]
deciph_txt = ""
for i in range(row_sz):                             #For loop to convert decyphered message into string
    for j in range(col_sz):
        if ciph_mat[i,j] == " ":
            deciph_txt += ""
        else:
            deciph_txt += deciph_mat2[i,j]
print("\nString after decryption:",deciph_txt) 