# hashTable.py
'''
a hash table is a form of associative array;
it's a data structure that maps keys to their values via a hash function
that uses the key to compute an index into the slots that are available in the
hash table and then it maps the key to the value;
sometimes, there are collisions where more than one value maps to the same slot,
in which case the hash function has to resolve the collision to keep the
correct value mapped to the correct key

most languages and frameworks already have hash table data structures that figure
out all of this stuff for you.

hash table PROS:
- hash tables can uniquely map a given key to a specific value
  (this ability supports implementing certain kinds of algorithms (counters, filters))
- hash tables are fst, typically faster than other kinds of table lookup structures,
  especially when the number of entries is large

hash table CONS:
- if number of entries in table is small, it's likely more efficient to just use a
  regular array or linked list to avoid collisions
- hash tables don't order entries in a predictable way, so unless you want to incur
  the cost of a separate sorting step, then hash tables may not be able to efficiently
  enumerate entries that are close to a given key because the data may be spread out
  randomly in the system's memory
  
'''
# main ================================
def main():
	# use dictionary constructor to create hash table all at once
	items1 = dict( {'key0' : 0, 'key1' : 1, 'key2' : 2, 'key3' : 3} )
	print('items1: ', items1)
	
	# use dictionary data type to create hash table by adding items
	items2 = {}
	k = 'key'
	v = 0
	while( v < 4 ):
		key = k + str(v)
		items2[key] = v
		v += 1
	print('items2: ', items2)
	
	# now if you want to find a value, you can access it via the key
	print('value 3 is: ', items2['key2'])
	
	# in an actual hash table, an algorithm does the mapping and the storage
	# locations in memory are not necessarily contiguous as they are in this example
	
	print('Done.')

if __name__ == '__main__' : main()