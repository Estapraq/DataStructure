'''
	ex:
	plates=['yellowPlate', 'redPlate', 'blackPlate']
	properties: 
	- Last-In-First-Out i.e LIFO 
	- certain operations should be preformed with time/space 
	complixity of O(1): 
	 Pop - removing the top (front) element
	 Push - adding element to the front  
	 peek - return the front element
	 isEmpty - return true if stack is empty, false if it i not
	 isFull - return true if stack is full, false if it i not
''' 
class Stack:
	def __init__(self) -> None:
		self.stack= []

	def isEmpty(self):
		return len(self.stack)==0

	def push(self,item):
		self.stack.append(item)
		print(item, "is added to the stack")

	def pop(self):
		if(self.isEmpty()):
			return float('-inf')
		return self.stack.pop()

	def peek(self):
		if(self.isEmpty()):
			return float('-inf')
		return self.stack[len(self.stack)-1] #return stack[-1]

#test above functions
myStack: Stack= Stack()
myStack.push('yellowPlate')
myStack.push('redPlate')
print(myStack) #this will giveyou the memory, and you 
               #need the Dunder method to print
myStack.pop()
print(myStack)
print(myStack.peek())










	



