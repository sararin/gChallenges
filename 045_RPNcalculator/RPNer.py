from operator import add, mul, sub, truediv

def tokenize(expr):
  expr = expr.split(' ')
  return [ x for x in expr if x.isdigit() or x in "+-/*pq"]

def parse(tokens):
  return [ int(x) if x.isdigit() else x for x in tokens ]
  
def evaluate(parsed, stack):
  operators = {'+': add, '-':sub, '/': truediv, '*':mul, 'p':print}
  while parsed:
    element = parsed.pop(0)
    if isinstance(element, str):
      if element in "p":
        operators[element](stack[-1])
      elif element in 'q':
        return -1
      else:
        value = operators[element](stack.pop(-2), stack.pop())
        stack.append(value)
    else:
      stack.append(element)
  return stack
      
if __name__ == "__main__":
    stack = []
    while True:
      expression = input(">")
      tokenized = tokenize(expression)
      parsed = parse(tokenized)
      stack = evaluate(parsed, stack)
      if stack == -1:
        break
