import numpy as np
import math
import sys

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ$"

message = input("Enter string (whitespace will be removed):").upper()
message = message.replace(" ","")
key = input("\nEnter such a key whose inverse is not 0 and a square matrix can be made from letters of key\n(eg:HILL, VIEW, GYBNQKURP):")

z = math.modf(math.sqrt(len(key)))                              #modf() returns fractional and integer part
if z[0] != 0:                                                   #If fractional part is non zero, that means
    print("Unacceptable matrix")                                #elements present in key will not form a square matrix
    sys.exit("Restart program.")

if len(message)%int(z[1]) != 0:                                 #This will fill empty space in message with $
    for i in range(int(z[1]) - len(message)%int(z[1])):         #so that equal vectors are made.
        message += "$"
print("\nOriginal string after some adjustments:\" ",message,"\" ,encrypting using Key:",key)

key_lst = list()
for i in range(len(key)):                                       #For loop to convert key string into list
    key_lst.append(key[i].upper())
key_mataz = np.array(key_lst).reshape(int(z[1]),int(z[1]))
key_mat = np.zeros((int(z[1]),int(z[1])),dtype=int)
for i in range(int(z[1])):                                      #For loop to assign alphabets a number
    for j in range(int(z[1])):                                  #eg(A=0,B=1...,Z=25)
        for k in range(len(alphabets)):                         #for alphabets present in key
            if key_mataz[i,j] == alphabets[k]:
                key_mat[i,j] = k

msg_lst = list()
for i in range(len(message)):                                   #For loop to convert message string into list
    msg_lst.append(message[i].upper())
msg_mataz = np.array(msg_lst).reshape(int(len(message)/int(z[1])),int(z[1]))
msg_mataz = msg_mataz.T
msg_mat = np.zeros((int(z[1]),int(len(message)/int(z[1]))),dtype=int)
for i in range(int(z[1])):                                      #For loop to assign alphabets a number
    for j in range(int(len(message)/int(z[1]))):                #eg(A=0,B=1...,Z=25)
        for k in range(len(alphabets)):                         #for alphabets present in message
            if msg_mataz[i,j] == alphabets[k]:
                msg_mat[i,j] = k

result_mat = np.zeros((int(z[1]),int(len(message)/int(z[1]))),dtype=int)
for i in range(int(len(message)/int(z[1]))):                    #For loop to multiply key matrix with message matrix
    result_mat[:,i] = key_mat @ msg_mat[:,i]
result_mat = result_mat%26
ciph_txt = ""
ciph_mat = np.zeros((int(z[1]),int(len(message)/int(z[1]))),dtype=str)
for i in range(int(z[1])):
    for j in range(int(len(message)/int(z[1]))):                #For loop to assign alphabets to numbers
        for k in range(27):                                     #present in the cipher matrix
            if result_mat[i,j] == k:
                ciph_mat[i,j] = alphabets[k]
for i in range(int(z[1])):                                      #For loop to convert cipher matrix into string
    for j in range(int(len(message)/int(z[1]))):
        ciph_txt += ciph_mat[i,j]
print("\nString after encryption:",ciph_txt)

#inv = np.linalg.inv(key_mat)                                   #inv() is used to find inverse of matrix
det = np.linalg.det(key_mat)
inv = np.linalg.inv(key_mat)
inv_res_mat = np.zeros((int(z[1]),int(len(message)/int(z[1]))),dtype=int)
for i in range(int(len(message)/int(z[1]))):                    #For loop to multiply inverse matrix with
    inv_res_mat[:,i] = inv @ result_mat[:,i]                    #cipher matrix
inv_res_mat = inv_res_mat%26
deciph_mat = np.zeros((int(z[1]),int(len(message)/int(z[1]))),dtype=str)
for i in range(int(z[1])):
    for j in range(int(len(message)/int(z[1]))):
        for k in range(27):                                     #present in the cipher matrix
            if inv_res_mat[i,j] == k:
                deciph_mat[i,j] = alphabets[k]
deciph_txt = ""
for i in range(int(z[1])):                                      #For loop to convert cipher matrix into string
    for j in range(int(len(message)/int(z[1]))):
        deciph_txt += deciph_mat[i,j]
print("\nString after decryption:",deciph_txt)