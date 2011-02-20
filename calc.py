#! /usr/bin/env python

from operator import mul

total = 104
black = 52
red = 52
peach = 8
red_no_p = red - peach
total_no_p = total - peach

not_peach = 0
is_peach = 0

for i in range(0, black+1):
    if (i == 0):
        factorial1 = 1
    else:
        factorial1 = reduce(mul, range(black+1-i, black+1))
    # calc n!
    factorial2 = reduce(mul, range(1, total - 3 - i + 1))
    not_peach += factorial1 * red_no_p * (total_no_p - 1 - i) * (total_no_p - 2 - i) * factorial2
    is_peach  += factorial1 * peach  * (total_no_p - i) * (total_no_p - 1 - i) * factorial2

all_conditions = reduce(mul, range(1, total+1))

no_peach = not_peach + is_peach
has_peach = all_conditions - no_peach

print "not_peach      = %d\n" % not_peach
print "is_peach       = %d\n" % is_peach
print "all_conditions = %d\n" % all_conditions
print "no_peach       = %d\n" % no_peach
print "has_peach      = %d\n" % has_peach
