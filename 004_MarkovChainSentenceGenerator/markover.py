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

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise ValueError("not enough values")
  bigram = genPairs(prepareSentence(getSentence(sys.argv[1])))
  for x in range(int(sys.argv[2])):
    print(' '.join(generateChain(bigram)))
