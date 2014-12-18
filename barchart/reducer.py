#!/usr/bin/python
import sys
from itertools import groupby
from operator import itemgetter

def read_mapper_output(file):
	for line in file:
		yield line.rstrip().split()

def main(argv):
	data = read_mapper_output(sys.stdin)

	for current_word, group in groupby(data, itemgetter(0)):
		try:
			counting_list = [int(count) for current_word, count in group]
			sumcount = sum(counting_list)
			totalcount = len(counting_list)
			print "%s%s%f" % (current_word, '\t', sumcount/float(totalcount))
		except ValueError:
			# count was not a number, so silently discard this item
			pass

if __name__ == "__main__":
	  main(sys.argv)
