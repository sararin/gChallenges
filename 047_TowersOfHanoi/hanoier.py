def hanoiSolve(n, A, B, C):
  if n > 0:
    hanoiSolve(n-1, A, C, B)
    C.insert(0, A.pop(0))
    hanoiSolve(n-1, B, A, C)
  return (A, B, C)

A = [1,2,3,4,5,6,7,8]
B = []
C = []
print(A, B, C) #starting positions
print(hanoiSolve(len(A), A, B, C)) #finishing positions
