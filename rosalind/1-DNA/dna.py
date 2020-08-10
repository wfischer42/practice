import sys

filename = sys.argv[1]

S = open(filename, 'r').read()

counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
for n in S:
  counts[n] += 1

print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}')