# ✅ Problem Statement

Milad and Majid are building a long binary string consisting of 0s and 1s.

    The string is constructed in the following way:
    
    In the first step, Milad writes the digit 1, so the string becomes 1.
    
    Then in each subsequent turn, the current player takes the string built so far, inverts all bits (i.e., changes every 1 to 0 and every 0 to 1), and appends this inverted string to the end of the current string.
    
    The next turn goes to the other player, and this process continues infinitely.

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

