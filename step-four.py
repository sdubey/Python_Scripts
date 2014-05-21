import string
import sys

def span(association, sentence):
  """
  This function calculates the association of a word
  in a sentence.
  Inputs: an association and a sentence.
  Output: -1 if the association is not contained in the word, else the length
  of the minimum contiguous sub-sentence that has all the words of the association.
  """

  words = sentence.rstrip().split()

  begin_index = len(words)-1
  end_index = 0

  for el in association:
    try:
      idx = words.index(el)
      if idx < begin_index:
        begin_index = idx
      if idx > end_index:
        end_index = idx
    except ValueError:
      return -1

  return end_index - begin_index + 1

def percentage_of_a_span(association, sentences, k):
  """This function returns the percentage of sentences for an association,
     that have span > k"""

  l = []
  for sentence in sentences:
    s = span(association, sentence)
    if s != -1:
      l.append(s)


  num = 0.0
  for el in l:
    if el>k:
      num += 1

  den = len(l)

  return num/den * 100.0


def filter_associations(associations, sentences, k, min_pct):
  l = []
  for association in associations:
    p = percentage_of_a_span(association, sentences, k)
    if p <= min_pct:
      l.append(association)
  return l

def remove_punctuation(s):
  exclude = set(string.punctuation)
  return ''.join(ch for ch in s if ch not in exclude)



def main():
  # read the input file for sentences
  # may need some pre-processing of the sentences here

  # read another input file for associations

  if len(sys.argv) is not 4:
    print 'incorrect arguments\nneed: step_one_output.txt step_three_output.txt step 4 output directory (/Users/sonaldubey/csc898/mini_project/output/step_4)'
    sys.exit(2)
  else:
    data_file  = open(sys.argv[1],'r')
    word_association_file = open(sys.argv[2], 'r')
    output_data_directory = sys.argv[3]

  associations = []
  for line in word_association_file.readlines():
    association = line.rstrip().split(" ")[0].split(",")
    associations.append(association)

  sentences = []
  for line in data_file.readlines():
    
    # remove newline char and convert to lower
    raw_sentence = line.rstrip().lower()

    # remove punctutation from raw_sentence
    sentence = remove_punctuation(raw_sentence)
    
    sentences.append(sentence)

  print "computing answer for k = 3..."
  answer1 = filter_associations(associations, sentences, 3, 60.0)
  print "computing answer for k = 5..."
  answer2 = filter_associations(associations, sentences, 5, 60.0)
  print "computing answer for k = 10..."
  answer3 = filter_associations(associations, sentences, 10, 60.0)


  # answer to part 1

  f = open(output_data_directory+"/step_four_output_k3.txt", "w")
  for association in answer1:
    f.write(str(association) + "\n")
  f.close()

  # answer to part 2
  f = open(output_data_directory+"/step_four_output_k5.txt", "w")
  for association in answer2:
    f.write(str(association) + "\n")
  f.close()

  f = open(output_data_directory+"/step_four_output_k10.txt", "w")
  # answer to part 3
  for association in answer3:
    f.write(str(association) + "\n")
  f.close()

main()
