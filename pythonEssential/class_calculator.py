# class_calculator.py
# this script demonstrates how to create a simple calculator class

# classes ===============================================
class Calculator:
	def __init__(self):
		self._total = 0
			
	def setMemory(self, val):
		self._memory = val
	
	def getMemory(self):
		return self._memory
		
	def getTotal(self):
		return self._total
		
	def operation(self, a, b, op):
		if(op == 'add'): tot = a + b
		elif(op == 'sub'): tot = a - b
		elif(op == 'mult'): tot = a * b
		elif(op == 'div'): tot = a / b
		self._total = tot
		return tot
			
	def add(self, a, b): return self.operation(a, b, 'add')
	def subtract(self, a, b): return self.operation(a, b, 'sub')
	def multiply(self, a, b): return self.operation(a, b, 'mult')
	def divide(self, a, b): return self.operation(a, b, 'div')

# main ==================================================
def main():
	c1 = Calculator()
	print('1 + 2 is ', c1.add(1, 2))
	print('1 - 2 is ', c1.subtract(1, 2))
	print('1 * 2 is ', c1.multiply(1, 2))
	print('1 / 2 is ', c1.divide(1, 2))
	print('The current total is ', c1.getTotal())

if __name__ == '__main__': main()