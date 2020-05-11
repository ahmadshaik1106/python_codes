#created by ahmad on 02-10-2019
def fun():
	steps =int(input("How many steps do you want?   :")) 
	print()
	k0="__"
	k1=" |"
	for i in range(steps):
		print(k0,"  \--»",i+1)
		print(k1,end='')
		k1="  "+k1
	print()
	print('___________________________________________')
	print()
c="y"
while True:
	if c=="y" or c=="Y":
		fun()
	elif c=='n' or c== "N":
		break
	else:
		print('  Invalid input  !!!     \n')
	c=input('Do you want to continue (y/n) ?:')
	print()
