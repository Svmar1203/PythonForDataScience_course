duote = 'All is fair in love and war'

print(duote)

print(duote.upper())
print(duote.lower())
print(duote.title())
print(len(duote))

name = 'Health'
age = 30

print(int(age))
print(int(30.11))

print('\n')
#Function
print('here is an example function: ')

def adding(num):
	print(num + 100)
adding(50)
 
print("Boolean expressions: ")

bool1 = True
bool2 = 3*3 == 9
bool3 = False

print(bool1, bool2, bool3)
print(type(bool1))

#Conditional statements
def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "NO drink for You!"

print(drink(3))
print(drink(1))

def alcohol(age, money): 
	if(age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "come back with more money"
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))


nl()
#list