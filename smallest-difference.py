#!/usr/local/bin/python3

from sys import maxsize 

# Time Complexity - O(n * m)
def smallestDifference(arrayOne, arrayTwo):
    minDiff = maxsize
    i = 0
    j = 0
	while i < len(arrayOne) and j < len(arrayTwo):
		x, y = arrayOne[i], arrayTwo[j]
		currentDiff = abs(x - y)
		if currentDiff < minDiff:
			minDiff = currentDiff
			output = [x, y]
		
		if x < y:
			i += 1
		if y <= x:
			j += 1
	return output

if __name__ == "__main__":
   print(smallestDifference([], [])) 