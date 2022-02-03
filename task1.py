# У учетом того, что нельзя использовать библиотеку Numpy

def multiplicate(A):
  if len(A) == 0:
    return 'Ошибка: массив нулевой длины!'
  B = []
  for i in range(len(A)):
    mul = 1
    for j in range(len(A)):
      if j !=i:
        mul *= int(A[j])
    B.append(mul)
  return B

A = [1, 2, 3, 4]
print(A)
print(multiplicate(A))