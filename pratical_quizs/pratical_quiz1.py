"""
Every day, Petr Tort either catches his bus or misses it. In the former case, he comes to the office on time,
in the latter case he is late. Petr knows that his boss gets angry if Petr is late two days in a row.
For a given number n of days, Petr wants to compute the number of possible combinations of catching and
missing the bus that will not make the boss angry.

For example, if n=2, then the only way to make the boss angry is two be late both days.
Therefore, the three remaining combinations are fine, and the answer is three.

Complete the code below to compute the number of combinations for a given n. Use dynamic programming to make the
complexity of your algorithm O(n) (in particular, not_angry(10000) should be very fast). """


def not_angry(n) :
    # tbl[i] is going to contain the number of possible combinations for i days
    tbl = [1] * (n + 1)
    if n > 0 :
        # base case: for just one day, there are ?? options
        tbl[1] = 1
    for i in range(2, n + 1) :
        tbl[i] = (n - 2) * tbl[i - 1] * (i - 1) + 2 * (i - 2) * tbl[i - 2]
    return tbl[n]


# should print 8
print(not_angry(4))

# 2 - 1, 2
#  1 - Catches, 2 - Misses
#  1 - Misses, 2 - Catches
#  1 - Catches, 2 - Catches
#  1 - Misses , 2 - Misses


# 2 - 1, 2, 3, 4
#  1 - Catches, 2 - Catches, 3 - Catches, 4 - Catches
#  1 - Misses, 2 - Catches, 3 - Catches, 4 - Catches
#  1 - Misses, 2 - Misses, 3 - Catches, 4 - Catches - Boss Angry
#  1 - Misses, 2 - Misses, 3 - Misses, 4 - Catches - Boss Angry
#  1 - Misses, 2 - Misses, 3 - Misses, 4 - Misses - Boss Angry
#  1 - Misses, 2 - Catches, 3 - Misses, 4 - Catches
#  1 - Misses, 2 - Catches, 3 - Misses, 4 - Misses  - Boss Angry
#  1 - Catches, 2 - Misses, 3 - Catches, 4 - Misses
#  1 - Catches, 2 - Misses, 3 - Catches, 4 - Misses
#  1 - Catches, 2 - Misses, 3 - Catches, 4 - Misses
