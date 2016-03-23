#!/usr/bin/env python

# This file takes a processed text file, with two columns (tab separated).
# First is number of words
# second is the company name
# I stores running count in a dictionary whose keys are the number of words.
# Result is a dictionary with total number of entries per word count.
#
# This script also creates a bar chart so we can eyeball the distribution

import matplotlib.pyplot as plt

fileobj = open('data/counts')

count_dictionary = {}

for idx in range(25):
    count_dictionary[idx] = 0


for line in fileobj:
    cnt_str = line.split('\t')[0]
    count_dictionary[int(cnt_str)] += 1

x = []
y = []
print "#Words\tFrequency"
for key, val in count_dictionary.iteritems():
    print "{0}:\t{1}".format(key, val)
    x.append(key)
    y.append(val)

plt.bar(x,y)
plt.show()




