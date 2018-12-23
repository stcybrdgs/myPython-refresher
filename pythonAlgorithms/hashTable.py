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
# imports =============================

# globals =============================

# classes =============================

# functions ===========================

# main ================================
def main():
	print('Done.')

if __name__ == '__main__' : main()