# sort()

def main():
	# sort numerically
	pointsInaGame = [0, 20, -20, 32]
	sortedGame = sorted(pointsInaGame)
	print(sortedGame)
	print(sorted(pointsInaGame, reverse=True))
	
	# sort alphabetically
	dogs = ['Jazz', 'Rikki', 'Lady']
	print(sorted(dogs))
	print(sorted(dogs, reverse=True))
	
	# sort alphabetically with key parameters
	dogs = ['jazz', 'rikki', 'Lady']
	print(sorted(dogs))
	print(sorted(dogs, key=str.upper))
	print(sorted(dogs, key=str.upper, reverse=True))
	
	# sort data in a list of tuples
	students = [
		('Alice', 'B', 12),
		('Eliza', 'A', 16),
		('John', 'C', 15)
	]
	
	# sort tuples based on name
	print(sorted(students, key=lambda student:student[0]))
	
	# sort tuples based on grade
	print(sorted(students, key=lambda student:student[1]))
	
	# sort tuples based on age
	print(sorted(students, key=lambda student:student[2], reverse=True))	


	

	

	
	



if __name__=='__main__':main()