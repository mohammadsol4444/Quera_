def getNoOfWays(n):
	if n <= 2:
		return n
	return getNoOfWays(n - 1) + getNoOfWays(n - 2)

n = int(input())
print(getNoOfWays(n))

