import random
import sys

def getSentence(filename):
  with open(filename, "r") as f:
    return f.read()

def genPairs(sentence):
  generatedPairs = {x:[] for x in sentence}
  generatedPairs['.'] = []
  generatedPairs[','] = []
  for key, value in generatedPairs.items():
    for x, y in enumerate(sentence):
      if key in '.,?!':
        pass
      elif key == y:
        if not (x+1) >= len(sentence):
          generatedPairs[key].append(sentence[x+1])
  return generatedPairs
  """
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
  """

def prepareSentence(sentence):
  sym = ".,?!"
  sentence = [ ' '+c+' ' if c in sym else c for c in sentence ]
  sentence = ''.join(sentence)
  return sentence.lower().split()

def generateChain(bigram):
  rand = random.choice(list(bigram.items()))[0]
  words = [rand]
  choices = bigram[rand]
  while choices:
    rand = words[-1]
    choices = bigram[rand]
    if not choices:
      break
    words.append(random.choice(choices))
  return words
  """
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
  """

bigram = genPairs(prepareSentence(getSentence(sys.argv[1])))
for x in range(10):
  print(' '.join(generateChain(bigram)))
