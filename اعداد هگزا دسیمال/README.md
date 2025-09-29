# ✅ Problem Statement

On a beautiful summer morning, a terrible incident occurred in the central processor. A sneaky virus called Megabyte somehow gained access to the memory of his sister, Hexadecimal (who was no less sneaky than him). In order to gain full control over his sister, he tried to load n distinct natural numbers from 1 to n.

However, his plan failed. The reason was simple: Hexadecimal only understood numbers written in base 2. That is, if a number in decimal representation contained any digit other than 0 or 1, it could not be stored in memory.

Now, Megabyte wants to know how many numbers were successfully loaded into memory.

For example, the first five steps of the game are as follows:

            Milad writes 1 → string: 1
            
            Majid inverts 1 → 0, and appends it → string: 10
            
            Milad inverts 10 → 01, and appends it → string: 1001
            
            Majid inverts 1001 → 0110, and appends it → string: 10010110
            
            Milad inverts 10010110 → 01101001, and appends it → string: 1001011001101001

# ✅ Solution (Python)

```python
def solve():
    L, R = map(int, input().split())
    s = "1"
    while len(s) < R:
        s += ''.join('0' if c == '1' else '1' for c in s)
    print(s[L-1:R])

