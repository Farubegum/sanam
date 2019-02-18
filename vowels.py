sam=input('')
san=sam.isalpha()
if(len(sam)==1):
	if san==True:
		if sam in('a','e','i','o','u','A','E','I','O','U'):
			print("Vowel")
		else:
			print("Consonant")
	else:
			print("invalid")
else:
	print("invalid")
