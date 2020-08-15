import random
from search import linear_search
from time import time
from search import binarySearch
data = range(100000)
start = time()
index = binarySearch(data, data[0])
end = time()
elapsed = end - start
print ('Total time elspsed for binary search is: '+str(elapsed))

datalin = random.sample(range(1000), 1000)
startlin = time()
length = int(len(datalin)/2)
indexlin = linear_search(datalin, datalin[length])
endlin = time()
elapsedlin = endlin - startlin
print( 'Total time elapsed for linear search is: '+str(elapsedlin))

