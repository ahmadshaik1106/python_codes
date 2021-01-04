vowels=['a','e','i','o','u']
consonents=[chr(c) for c in range(97,123) if  chr(c) not in vowels]
string=input('Enter something : ')
for letter in string:	
	if letter.lower() in vowels : 
		print(letter,' - vowel')		
	elif letter.lower() in consonents: 
		print(letter,' - consonent')		
	else:
		try:
			letter=int(letter)
			print(letter,' - number')
		except:
			print(letter,' - special character')
