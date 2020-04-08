from numpy import random
import os,sys
import time
print()

def heart():
	for i in range(33):
		print(' ',end='')
		for j in range(33):
			if  (i+j==48 or i-j==16 or (j==0 and 16>i>6) or (j==32 and 16>i>6) or i+j==6 or (i-j==-7 and j<17) or i-j==-26 or (i+j==25 and j>16)       or  (((i==11 or i==15 or i==19)and 19>j>13)or (j==14  and 15>i>10) or j==18 and 20>i>15)         or (((i==10 or i==18)and 13>j>7 ) or j==8 and 19>i>9)          or ((i==10 or i==14 or i==18)and 25>j>19 or j==20 and 19>i>9) ):
				print('\u001b[41m'+' ',end=' ')
				print('\u001b[40m'+'',end='')
				
			elif (i+j<6 or i+j>48 or i-j>16 or i-j<-26)  or 25>i+j>1 and j-i>7:
				print('\u001b[40m'+' ',end=' ')
				print('\u001b[40m'+'',end='')
				
			else:
				rand=chr(random.randint(33,97))
				print('\u001b[47m'+'\033[31m'+str(rand),end='')
				print('\u001b[47m'+' ',end='')
				print('\u001b[44m'+'',end='')
		time.sleep(.03)
		if i<32:
			print()
	print('\033[37m',)
	
for i in range(1):
	heart()
