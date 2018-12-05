# coroutine.py
'''
A coroutine is another important tool that you can build out of a
Python generator. While a generator is something that produces a sequence,
with a new value being produced each time the generator is called,
a coroutine is something that you constantly feed things to, and it
will take whatever is passed and do something with it. Coroutines may
return something, but they may not. What you give to the coroutine, what it does
with the given item, and what it returns are all completely up to you.

Unlike generators, the purpose of coroutines is not to iterate over sequences.
Though it it technically a generator object, the coroutine is designed to repeatedly
do something with the stuff sent to it and then stop when it reaches the yield
statement. It sounds like a function, but there is a key difference in that the
coroutine has properties and states that can be referenced and altered.

A coroutine's most important ability is to change the state of its own properties,
the state of something else, or both.

send() is a method that was added to generators exclusively for the purpose of
coroutine functionality. In a coroutine, the 'yield' statement is used to capture
the value of whatever is passed to the send() method. So, in a coroutine, 'yield'
not only pauses the flow, but it also captures values.

So.... for generators, think 'yield'
       for coroutines, think 'yield' and send()

'''
# functions ==========================
def coroutine_example():
	while True:
		x = yield
		# do something with x
		print(x)

# main ===============================
def main():
	print('Running coroutine...\n')

	c = coroutine_example()
	# use next() to prime the coroutine
	# or to restart it from last state
	next(c) 
	c.send(10)
	
	print('\nDone.')

if __name__=='__main__': main()