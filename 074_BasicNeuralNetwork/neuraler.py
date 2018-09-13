import random 
from functools import reduce

class Neuron:
  def __init__(self, value, weight, connTo=None):
    self.value = value
    self.connTo = connTo
    self.weight = weight

  def giveValue(self):
    return self.value * self.weight

def addAll(argv):
  temp = []
  for x in argv:
    temp.append(x.giveValue())
  return reduce(lambda x,y: x+y, temp)
  
def uniform(x):
  return x

if __name__ == "__main__":
  inputs = [ Neuron(1, random.uniform(0, 1)), Neuron(1, random.uniform(0, 1)) ]
  hidden = [ Neuron(1, random.uniform(0, 1)), Neuron(1, random.uniform(0, 1)), Neuron(1, random.uniform(0, 1)) ]
  output = [ Neuron(1, 1) ]
  for x in hidden:
    x.value = uniform(addAll(inputs))
  for x in output:
    x.value = uniform(addAll(hidden))
  print(output[0].value)
