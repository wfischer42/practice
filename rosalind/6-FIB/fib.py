import sys

filename = sys.argv[1]
f = open(filename)

S = list(map(int, f.read().split()))
F = (1, 1)

for i in range(2, S[0]):
  Fn = S[1] * F[0] + F[1]
  F = (F[1], Fn)

print(Fn)