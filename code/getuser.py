import getpass
print(getpass.getuser())

try:
	open('123123.png')
	print(1)
except:
	print(2)