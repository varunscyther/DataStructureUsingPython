# Find sorted arrays percentile


P-th percentile (0<P≤100) of a list of K ordered values (sorted from least to greatest) is the smallest value in the list such that no more than P percent of the data is strictly less than the value and at least P percent of the data is less than or equal to that value.

It can be obtained by first calculating the ordinal rank and then taking the value from the ordered list that corresponds to that rank. The original rank kk is calculated using this formula

k = [p/100 * K]

Given two sorted arrays aa and bb size of n and m.

Implement a function find_percentile(a, b, p) that finds p-th percentile of an array c, where c is the result of merge arrays a and b.

***Time limit: 0.1 seconds per test.***

Note that solutions working for linear time from O(n+m) will not satisfy the time limit. To get full score the solution should work faster.

***Input data:***

The function takes two arrays a and b and quantile parameters q and k.

 _0 ≤ n, m ≤ 10^6, 0<p≤100_

You can assume that at least one of the arrays is not empty.

_**Output data:**_

One int —p-th percentile of merged arrays.

Examples:

|s.no |a|b|p|output|
|---|---|---|---|---|
|1|[1, 2, 7, 8, 10]|[6, 12]|50|7|
|2|[1, 2, 7, 8]	|[6, 12]|50|6|
|3|[15, 20, 35, 40, 50]|[]|30|20|
|4|[15, 20]|[25, 40, 50]|40|20|


**_Test sets:_**

Part 1. 50-th percentile is called the median. 
For all tests from this test set p = 50 and you should find the median of two sorted arrays.
For this test set n,m≤100 and solution working for linear time from n and m will satisfy the time limit.

Part 2. For all tests p=50,0≤n,m≤10^6. Solution working for O(n+m) will satisfy the time limit.

Part 3. Small tests 0≤n,m≤100, 0<p≤100.

Part 4. Large tests 0≤n,m≤10^6 ,0<p≤100.

**_Hints:_**

Hint 1. Remember what algorithms with log in time complexity do you know?

Hint 2. After you come up with some solutions try to prove its correctness and estimate time and space complexity.
It can help you find mistakes (if any) in this stage, and you will be asked to do this anyway in the next task.

Hint 3. Try unit test and stress test to find mistakes (if any), you will be asked to implement unit tests and stress test anyway in the next task.

Here is a file with function definitions, and a couple of sample input-output pairs:
