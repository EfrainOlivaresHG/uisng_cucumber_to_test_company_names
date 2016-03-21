#!/usr/bin/env python
# Read in data file and mark all entries by how many words.
# The initial filter is very simple, just use a regex and remove all non-alpha chars
# Then split on space, and count the items in resulting list
import re

def words_in_string(a_str):
    wordList = re.sub("[^\w]", " ", a_str).split()
    return len(wordList)

source =  open("data/UnnormalizedCompanies.tsv")
counted = open("data/counts", 'w')
for line in source:
    company_str = line.split('\t')[0]
    count = words_in_string(company_str)
    counted.write("{0}\t{1}\n".format(str(count), company_str))


source.close()
counted.close()
