# ✅ Problem Statement

On a beautiful summer morning, a terrible incident occurred in the central processor. A sneaky virus called Megabyte somehow gained access to the memory of his sister, Hexadecimal (who was no less sneaky than him). In order to gain full control over his sister, he tried to load n distinct natural numbers from 1 to n.

However, his plan failed. The reason was simple: Hexadecimal only understood numbers written in base 2. That is, if a number in decimal representation contained any digit other than 0 or 1, it could not be stored in memory.

Now, Megabyte wants to know how many numbers were successfully loaded into memory.

-----------------------------------------------------------------------

Input: The input consists of a single integer n.

Output: Print a single integer — the number of successfully loaded numbers.

-----------------------------------------------------------------------

Example :
input: 10 --------->>>> output: 2


# ✅ Solution (Python)

```python
def countBinaries(N):
	powersOfTwo = [0] * 11
	powersOfTwo[0] = 1
	for i in range(1, 11):
		powersOfTwo[i] = powersOfTwo[i - 1] * 2
	ctr = 1
	ans = 0
	while (N > 0):
		if (N % 10 == 1):
			ans += powersOfTwo[ctr - 1]
		elif (N % 10 > 1):
			ans = powersOfTwo[ctr] - 1
		ctr += 1
		N = N // 10
	return ans
N = int(input())
print(countBinaries(N))

