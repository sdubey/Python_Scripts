#####################################################################
#
# This script will go through a list of files and extract all 
# sentences that contain a family member. 
# command line arguments are a txt file with a list
# of Absolute file paths the output is a text file containing all of
# the sentences that include family member
#
# use this grep command to find all files that contian family members and outputs them to ffiles.txt
# egrep -i -w -l -f fnames ~/Documents/csc898/dataset/dataA/* > ffiles.txt
# where fnames is a file that only contains the line:
# (mother|brother|grandfather|sister|grandmother|father|mom|dad|son|daughter|uncle|aunt|niece|nephew|cousin)('s|s)*
#  ! @ # $ % ^ & * ( ) _ +  // remember the position of the metachars
# input: filelist.txt
# output: familysentences.txt
# 
#usage: $python sentence-splitter.py [input] [output] 
######################################################################

import sys
import re
import nltk
import os

def main():

  if len(sys.argv) is not 3:
    print 'incorrect arguments\nneed: inputfilelist.txt outputfile.txt'
    sys.exit(2)
  else:
    filenames = sys.argv[1]
    outfilename = sys.argv[2]

  from os.path import basename 

  #load all filenames
  files =[]
  for filename in open(filenames, 'r'): files.append(filename.strip())

  #initialize arrays 
  familysentences =[]

  #initialize sentence detector
  sentdetector = nltk.data.load('tokenizers/punkt/english.pickle')

  #initialize regerular expression pattern for family members
  familynames = re.compile(r'\b(mother|brother|grandfather|sister|grandmother|father|mom|dad|son|daughter|uncle|aunt|niece|nephew|cousin)(\'s|s)*\b', re.I)

  counter = 0
  #search through all files
  for file in files:

    if counter % 40 == 0:  print '.',
    counter = counter + 1
    text = open(file, 'r').read()

    #split into sentences
    sentences = sentdetector.tokenize(text.strip(), realign_boundaries=True)

    sentences 

    #if sentence contains a family member, save it. Make sure sentence is only one line
    #prepend with filename
    for sent in sentences:
      if familynames.search(sent) is not None:  familysentences.append(sent.replace('\n','').lower())

  #write output to file
  outfile = open(outfilename, 'w')
  for sent in familysentences:
    #print sent
    outfile.write(sent + '\n')

  outfile.close()  

if __name__ == "__main__":
  main()

