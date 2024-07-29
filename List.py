class List:
	'''
	 colors=['red', 'yellow', 'blue', 'black']
	 prices=[5, 8, 9, 8, 9]
	 myList= ['fruits', 'shirt', 9, true, 1.7, 1988, 'c']
	'''

	#Create
	fruit=[]
	print(fruit)
	prices=list()
	print(prices)

	#Add using append() and insert() methods
	fruit=['orange','apple']
	print(fruit)
	fruit.append('banana')
	print(fruit)
	fruit.insert(0,'tomatoes')
	print(fruit)
	fruit.insert(2,'orange')
	print(fruit)

	#Read using zero index and negative index
	print(fruit[0])
	print(fruit[2])
	print(fruit[-1])
	print(fruit[-3])

	#Update
	fruit[0]='apple'
	print(fruit)

	#Delete using remove(), clear(), and pop() methods
	fruit.pop()
	print(fruit)
	fruit.remove('apple')
	print(fruit)
	#fruit.clear()
	#print(fruit)

	#Slicing
	print(fruit[0:2])
	print(fruit[1:2])
	print(fruit[1:3])

	#Index method
	print(fruit.index('apple'))

	#In/not In operator
	print('apple' in fruit)
	print('tomatoes' not in fruit)

	#Length function
	print(len(fruit))

	#Extend() method
	myFruit=['mango', 'cherry']
	fruit.extend(myFruit)
	print(fruit)
	
	#For loop
	for item in fruit:
		print(item)



     







