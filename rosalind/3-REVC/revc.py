import sys

filename = sys.argv[1]
S = open(filename, 'r').read()

def revc(seq):
  comps = { "A": "T", "G": "C", "C": "G", "T": "A"}
  c = ""
  for n in seq:
    c = comps[n] + c
  return c

print(revc(S))