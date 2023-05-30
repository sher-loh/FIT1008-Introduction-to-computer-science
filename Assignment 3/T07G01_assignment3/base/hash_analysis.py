from hash_table import LinearProbePotionTable
""" 
A block of code that test the hash functions.
LinearProbePotionTable(x = int, y = boolean)
x represents the table size 
y represents the hash function used (True = good_hash, False = bad_hash)
"""
potion_hash = LinearProbePotionTable(100, True)

# insert in the hash table
for i in range(101):
    potion_hash.__setitem__(str(i), str(i))
    print(potion_hash.statistics())
