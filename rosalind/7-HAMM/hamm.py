import sys

filename = sys.argv[1]
f = open(filename, 'r')

s = f.readline()
t = f.readline()

c = 0 

for i in range(0, len(s) - 1):
  if s[i] != t[i]:
    c += 1

print(c) 