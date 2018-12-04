# prac_1203.py

# classes ============================
# pattern 1
# simple class with no constructor
# class variables and class methods only
class VarMethOnly:
	# class constructor __init__
	#     none
	
	# class variables
	var1 = 'Variable One'
	var2 = 'Variable Two'
	
	# class methods
	def method1(self): print('Method One')
	def method2(self): print('Method Two')
	def getVar1(self): return self.var1
	def getVar2(self): return self.var2

# pattern 2
# class with constructor
# includes default constructor variables
# as well as setter and getter methods
class Occupations():
	# constructor method
	def __init__(self, job = 'Manager', field = 'Restaurants'):
		self._job = job
		self._field = field
	
	# class methods
	def setJob(self, j): self._job = j
	def setField(self, f): self._field = f
	def getJob(self): return self._job
	def getField(self): return self._field

# pattern 3
# class with construtor taking *args
# where args must be passed in specific order
class Dogs():
	def __init__(self, *args):
		# breed, color, sound
		self._breed = args[0]
		self._color = args[1]
		self._sound = args[2]
	
	def getDog(self):
		print('The ' + self._color + ' ' + self._breed + ' says ' + self._sound + '.')

# pattern 4
# class with constructor taking **kwargs
# where kwargs may be passed in any order
class Books():
	def __init__(self, **kwargs):
		self._size = kwargs['size'] if 'size' in kwargs else 'big'
		self._type = kwargs['type'] if 'type' in kwargs else 'English'
	
	def getSize(self): return self._size
	def getType(self): return self._type

# main ===============================
def main():
	print('Class Pattern 1: -------------------------- ')
	vars1 = VarMethOnly()
	print(vars1.getVar1(), ', ', vars1.getVar2())
	vars1.method1()
	vars1.method2()
	print('Done.')
	
	print('\nClass Pattern 2: -------------------------- ')
	occs1 = Occupations()
	occs2 = Occupations('Developer', 'IT')
	occs3 = Occupations()
	occs3.setJob('Collector')
	occs3.setField('Sanitation')
	print(occs1.getJob(), ', ', occs1.getField())
	print(occs2.getJob(), ', ', occs2.getField())
	print(occs3.getJob(), ', ', occs3.getField())
	
	print('\nClass Pattern 3: -------------------------- ')
	dog1 = Dogs('Chihuahua', 'Brown', 'Yap')
	dog1.getDog()

	print('\nClass Pattern 4: -------------------------- ')
	book0 = Books(type = 'Chinese', size = 'Medium Sized')
	book1 = Books(type = 'Math', size = 'Gigantic')
	book2 = Books()
	print('The book is a {} {} book.'.format(book0.getSize(), book0.getType()))
	print('The book is a {} {} book.'.format(book1.getSize(), book1.getType()))
	print('The book is a {} {} book.'.format(book2.getSize(), book2.getType()))
	
if __name__ == '__main__': main()

