letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

msg_upp = input("Enter string (whitespace will be removed):").upper()
msg_upp = msg_upp.replace(" ","")
key_val = input("Enter shift number:")
print("\nOriginal string:\" ",msg_upp,"\" ,shifting it by",key_val)

x = int(key_val) % 26
ciph_txt = ""
for i in range(len(msg_upp)):						#For loop for encryption.
	for j in range(26):
		if msg_upp[i] == letters[j]:				#If matching alphabet is found in the list of letters
			ciph_txt += letters[j+x]				#then replace that alphabet with some alphabet ahead.
print("\nString after encryption:",ciph_txt)

deciph_txt = ""
for i in range(len(msg_upp)):						#For loop for decryption.
	for j in range(26):
		if ciph_txt[i] == letters[j+26]:			#If matching alphabet is found in the list of letters
			deciph_txt += letters[j+26-x]			#then replace that alphabet with some alphabet present before.
print("\nString after decryption:",deciph_txt)

print("\nHacking by Brute-Force:-\n")
hac_txt = ""
for i in range(26):									#For loop to generate all possible combinations
	for j in range(len(ciph_txt)):
		for k in range(26):
			if ciph_txt[j] == letters[k]:
				hac_txt += letters[k+i]
	print("KEY #%s: %s" % (i,hac_txt))
	hac_txt = ""