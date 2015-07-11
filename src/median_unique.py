# program that calculates the median number of unique words per tweet

import numpy as np
import sys

tweets_fileloc = 0

class uniqueCounts(object):
	def __init__(self):
	#initialize data structure for keeping track of frequencies of number of unique words in tweet
		self.freq = np.zeros((70,), dtype=np.int) # [0 for x in range(1,71)] # 70 spaces possible
		self.size = 0
		self.output_path = sys.stdout
	def countUnique(self, string):
		'''
			input string, output number of unique words
			triggered by processTweets funcion
			splits strings into words, keep track of unique words, and output number of unique words
		'''
		temp = []
		for word in string.split():
			if word not in temp:
				temp.append(word)
		return len(temp)
	def updateMedian(self, newcount):
		'''
			input integer (new count), output median
			triggered by output funcion
			adds new count to object and keep track of number of counts in object. calculates median with minimal sorting
		'''
		self.size += 1
		self.freq[newcount-1] += 1
		if (self.size > 1):
			mid = float(self.size) / 2
			leftsum = np.sum(self.freq[ :self.marker])
			if leftsum < mid:
				self.marker = self.getNextCount()
				return self.marker
			elif leftsum == mid: #even
				return float((self.marker + self.getNextCount())) / 2
			elif leftsum > mid:
				leftleftsum = leftsum - self.freq[self.marker-1]
				if leftleftsum < mid:
					return self.marker
				elif leftleftsum == mid: # even
					self.marker = self.getPrevCount()
					return float((self.marker + self.getNextCount())) / 2
				elif leftleftsum > mid:
					self.marker = self.getPrevCount()
					return self.marker
		else:
			self.marker = newcount
			return self.marker
	def getNextCount(self):
		'''
			input none, output next count present in object
			triggered by updateMedian funcion
			move down in array until reaching the next count stored
		'''
		x = self.marker
		x += 1
		while self.freq[x-1]==0:
			x += 1
		return x
	def getPrevCount(self):
		'''
			input none, output previous count present in object
			triggered by updateMedian funcion
			move up in array until reaching the previous count stored
		'''
		x = self.marker
		x -= 1
		while self.freq[x-1]==0:
			x -= 1
		return x
	def output(self, f, newcount):
		'''
			input file object, new count, output none
			triggered by processTweets funcion
			gets new median from updateMedian function and write result to file
		'''	
		f.write('%s\n' % self.updateMedian(newcount))
	def processTweets(self, tweets_fileloc):
		'''
			input starting location in tweet file, output new location in tweet file
			triggered in python file
			reads each line from input text file and trigger countUnique and output functions to process each line.
		'''
		with sys.stdin as f:
			f.seek(tweets_fileloc)
			with sys.stdout as foo:
				for line in f:
					self.output(foo, self.countUnique(line))
			return f.tell()


myCountFreq = uniqueCounts()
tweets_fileloc = myCountFreq.processTweets(tweets_fileloc)

