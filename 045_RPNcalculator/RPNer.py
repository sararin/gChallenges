from operator import add, mul, sub, truediv

def tokenize(expr):
  expr = expr.split(' ')
  return [ x for x in expr if x.isdigit() or x in "+-/*qp"]

def parse(tokens):
  return [ int(x) if x.isdigit() else x for x in tokens ]

def evaluate(parsed, stack):
  operators = {'+': add, '-':sub, '/': truediv, '*':mul}
  while parsed:
    element = parsed.pop(0)
    if isinstance(element, str):
      value = operators[element](stack[-2], stack[-1])
      stack.pop()
      stack.pop()
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
