# t' = t**2 + 1
coeffs = [0, 1]
def diff(coeffs):
  next_level=[]
  for i in range(len(coeffs)+1):
    next_level.append(0)
  for i in range(len(coeffs)):
    if coeffs[i] == 0:
      continue
    else:
      if i==0:
        next_level[i] = 0
      else:
        next_level[i-1] += i * coeffs[i]
        next_level[i+1] += i * coeffs[i]
  return next_level

def zero(n, coeffs):
  for i in range(int(n)):
    coeffs = diff(coeffs)[:]
  return coeffs[0]

for i in range(int(input())):
  print(zero(i, coeffs))
