✅ Problem Statement

Write a program that calculates the value of eˣ using the following series expansion (up to three decimal places):

𝑒
𝑥
=
1
+
𝑥
1
!
+
𝑥
2
2
!
+
𝑥
3
3
!
+
…
e
x
=1+
1!
x
	​

+
2!
x
2
	​

+
3!
x
3
	​

+…

The program receives two numbers — x (the exponent) and n (the number of terms in the series).
You must compute the sum of the first n terms of this series and print the result rounded to three decimal places.

⏱ Time Limit

1 second

💾 Memory Limit

128 MB

🧩 Input

The first line contains a real number x.

The second line contains an integer n.

Constraints:

0
≤
𝑥
,
𝑛
≤
1000
0≤x,n≤1000
💡 Output

Print the value of eˣ, calculated up to three decimal places.

🧮 Example 1

Input:

5
10


Output:

143.689

🧮 Example 2

Input:

3
15


Output:

20.086

✅ Solution (Python)
x = float(input())
n = int(input())

ex = 0
loop_element = 1

for i in range(1, n + 1):
    ex += loop_element
    loop_element = loop_element * (x / i)

ex = round(ex, 3)
print(f"{ex:.3f}")
