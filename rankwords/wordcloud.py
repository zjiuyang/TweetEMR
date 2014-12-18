#!/usr/bin/python
import heapq
import sys

def load_stop_words():
	ifile = open('stopwords.txt', 'r')
	stopwords = set()
	for line in ifile:
		stopwords.add(line.rstrip())
	return stopwords

def main():
	stopwords = load_stop_words();
	count = 0
	happy_queue = []
	sad_queue = []

	for line in sys.stdin:
        	tokens = line[:-1].split()
		if tokens[0] not in stopwords:
			if count < 10:
				heapq.heappush(happy_queue, (int(tokens[1]), tokens[0]))
				heapq.heappush(sad_queue, (int(tokens[2]), tokens[0]))
			else:
				heapq.heappushpop(happy_queue, (int(tokens[1]), tokens[0]))
				heapq.heappushpop(sad_queue, (int(tokens[2]), tokens[0]))
			count+=1
		

	print "=======happy words======="
	for item in happy_queue:
 		print('%s - %s' % item)
	print "=======sad words======="
	for item in sad_queue:
 		print('%s - %s' % item)

if __name__ == "__main__":
	main()
