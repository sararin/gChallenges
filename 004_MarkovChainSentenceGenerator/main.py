import random
import sys

def getSentence(filename):
  with open(filename, "r") as f:
    return f.read()

def genPairs(sentence):
    generatedPairs = []
    generatedPairs.append((sentence.pop(-2),sentence.pop()))
    while sentence:
      x = sentence.pop()
      if '.' in x:
        generatedPairs.append((x[:-1], '.'))
      else:
        generatedPairs.append((x, generatedPairs[-1][0]))
    generatedPairs.reverse()
    return generatedPairs

def prepareSentence(sentence):
  return sentence.lower().split()

def generateChain(bigram):
  rand = random.choice(bigram)[0] 
  words = [rand]
  choices = [ x for x in bigram if x[0] == rand ]
  words.append( random.choice(choices)[1] )
  while choices:
    rand = words[-1]
    choices = [ x for x in bigram if x[0] == rand ]
    if not choices:
      break
    words.append( random.choice(choices)[1] )
  return words


for x in range(15):
  bigram = genPairs(prepareSentence(getSentence(sys.argv[1])))
  print(' '.join(generateChain(bigram)))
