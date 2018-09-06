import sys

def fizzerbuzzer(howLong):
  answer = []
  for x in range(1, howLong):
    if x % 15 == 0:
      answer.append("FizzBuzz")
    elif x % 3 == 0:
      answer.append("Fizz")
    elif x % 5 == 0:
      answer.append("Buzz")
    else:
      answer.append(str(x))
  return ' '.join(answer)

if __name__ == "__main__":
  print(fizzerbuzzer(int(sys.argv[1])))
