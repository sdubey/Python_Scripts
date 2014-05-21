import string
import itertools
import sys

def contains_association(association, sentence):
  """This function returns True if and only if the association is
     contained in the sentence. The order of elements in the association is preserved."""
  words = sentence.split(" ")
  try:
    l = [words.index(el) for el in association]
    return sorted(l) == l
  except ValueError:
    return False

def association_count(association, sentences):
  """ This function returns the number of times this association
      has occured in the sentences. The count will preserve the order
      of the words in the association."""
  count = 0
  for sentence in sentences:
    if contains_association(association, sentence):
      count += 1
  return count


def permutations_of_all_associations(associations):
  """Returns all permutations across all associations"""
  l = []
  for association in associations:
    l += list(itertools.permutations(association))
  return l


def remove_punctuation(s):
  exclude = set(string.punctuation)
  return ''.join(ch for ch in s if ch not in exclude)


def main():
  # read the input file for sentences
  # may need some pre-processing of the sentences here
  # read another input file for associations
  if len(sys.argv) is not 4:
    print 'incorrect arguments\nneed: step_one_output.txt step_four_output.txt step_5_output_directory (/Users/sonaldubey/csc898/mini_project/output/step_4)'
    sys.exit(2)
  else:
    data_file  = open(sys.argv[1],'r')
    word_association_file = open(sys.argv[2], 'r')
    output_data_directory = sys.argv[3]

  associations = []
  for line in word_association_file:
    association = eval(line.rstrip())
    associations.append(association)
    
  #print associations  

  sentences = []
  for line in data_file:
    # remove newline char and convert to lower
    raw_sentence = line.rstrip().lower()

    # remove punctutation from raw_sentence
    sentence = remove_punctuation(raw_sentence)

    sentences.append(sentence)

  all_associations = permutations_of_all_associations(associations)

  f = open(output_data_directory+"/step_five_output.txt", "w")
  for association in all_associations:
    count = association_count(association, sentences)
    # write the association and the count to the file.
    f.write(str(association) + " " + str(count) + "\n")
  f.close()

main()
