# math and random modules 

# import modules ==============
import math, random


# main() ======================
def main():
	
	# constants
	print('\nconstants: ========================')
	print(
		'pi: ', math.pi,
		'\ne:' , math.e,
		'\nnan: ', math.nan,
		'\nninf: ', math.inf,
		'\n-inf: ', -math.inf
	)
	
	# trig
	print('\ntrig: ========================')
	obst_direction = math.cos(math.pi / 4)
	print(obst_direction)
	
	# ceiling and floor
	print('\nceiling & floor: ========================')
	cookies = 10.3
	candy = 7
	age = 47.9
	print(math.ceil(cookies)) # round up
	print(math.ceil(candy))   # round up
	print(math.floor(age))    # round down
	
	# factorial & square root
	print('\nfactorial & square root: ========================')
	print(
		'factorial of 3: ', math.factorial(3),
		'\nsquare root of 64:', math.sqrt(64)
	)
	
	# greatest common denominator GCD
	print('\ngreatest common denominator (GCD): ========================')
	print(
		'\ngcd of 8 & 52: ', math.gcd(8,52)
	)
	
	# degrees & radians
	print('\ndegrees & radians: ========================')
	print(
		'\n360 degrees is ', math.radians(360), ' radians'
		'\n2*pi is: ', math.pi*2,
		'\n2pi radians is ', math.degrees(math.pi*2), ' degrees'
	)
	
	# the random numbers
	print('\nrandom numbers: ========================')
	
	# print a random number
	print('random number is: ', random.random())
	
	# flip a coin
	decider = random.randrange(2)
	coinFace = 'Tails'
	if (decider == 1):
		coinFace = 'Heads'
	else:
		coinFace = 'Tails'
	print('coin flip is {}: {}'.format(decider, coinFace))
	
	# roll a die
	dieFace = random.randrange(1,7)
	print('die roll is: ', dieFace)
	
	
	# random choices
	print('\nrandom choices: ========================')
	
	# randome sample
	lotteryWinners = random.sample(range(100), 5)
	print('winning lottery numbers are: ', lotteryWinners)
	
	# random choice
	possiblePets = ['bird', 'snake', 'dog']
	print('your pet choice is: ', random.choice(possiblePets))
	
	# random shuffle
	cards = ['jack', 'king', 'queen', 'ace']
	suits = ['diamonds', 'hearts', 'spades', 'clubs']
	random.shuffle(cards)
	random.shuffle(suits)
	z = zip(cards, suits)
	print(cards, '  ', suits, ' ')
	print('your random card is: {} of {}'.format(random.choice(cards), random.choice(suits)))


if __name__=='__main__':main()