import sys

filename = sys.argv[1]

S = open(filename, 'r').read()
rna = ''

for n in S:
  c = "U" if n == "T" else n 
  rna += c

print(rna)
# print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')