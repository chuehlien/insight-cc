# program that calculates the total number of times each word has been tweeted.


import sys

tweets_fileloc = 0

class uniqueWordDict(object):
	def __init__(self):
		self.dict = {}
		self.output_path = sys.stdout
	def update(self, string):
		'''
			input string, output none
			triggered by processTweets funcion
			splits strings into words and add counts of word to entries in the unique word dictionary object
		'''
		for word in string.split():
			if word not in self.dict:
				self.dict[word] = 1
			else:
				self.dict[word] += 1
	def output(self):
		'''
			input none, output none
			triggered by processTweets function
			sorts dictionary and output unique words and their counts to output file
		'''
		with sys.stdout as f:
			dlist = self.dict.keys()
			dlist.sort()
			for word in dlist:
				f.write('{0:22} {1:8d}\n'.format(word, self.dict[word]))
	def processTweets(self, tweets_fileloc):
		'''
			input starting location in tweet file, output new location in tweet file
			triggered in python file
			reads each line from input text file and trigger update and output functions to process each line
		'''
		with sys.stdin as f:
			f.seek(tweets_fileloc)
			for line in f:
				self.update(line)
			self.output()
			return f.tell()

myWordDict = uniqueWordDict()
tweets_fileloc = myWordDict.processTweets(tweets_fileloc)
