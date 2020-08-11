import sys

filename = sys.argv[1]
f = open(filename, 'r')

s = f.readline()
t = f.readline()
pos = []
for n in range(0, len(s)):
  if s[n:(n+len(t)) ]== t:
    pos.append(n+1)

print(*pos)