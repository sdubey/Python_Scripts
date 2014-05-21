
#####################################################################
#
# Sonal Dubey - stop words remover from a file
#
# This script will go through the each line from the file
# sentences that contains the stopwords will be modified, all the stop words will be removed
# command line arguments are a txt file with all the lines
# of Absolute file paths the output 
# 
# input: filelist.txt
# output: familysentences.txt
# 
#usage: $python remove-stop-words.py [input] [output] 
######################################################################
import sys
import nltk
import re

def main():
	
	if len(sys.argv) is not 3:
		print 'incorrect arguments\nneed: inputfilelist.txt outputfile.txt'
		sys.exit(2)
	else:
		inputfile = open(sys.argv[1],'r')
		outfile = open(sys.argv[2], 'w')

	from nltk.corpus import stopwords
	stop = stopwords.words('english')

	for line in inputfile.readlines():
	
		#We only want to work with lowercase for the comparisons
		line = line.lower() 

		#remove punctuation and split into seperate words
		words = re.findall(r'\w+', line,flags = re.UNICODE | re.LOCALE) 

		var = ' '.join([word.lower() for word in words if (word.lower() not in stop)])
		outfile.write(var + '\n')

	inputfile.close()
	outfile.close()	


if __name__ == "__main__":
  main()

