import sys

filename = sys.argv[1]
f = open(filename, 'r')

def gc(seq):
  c = 0
  for n in seq:
    if (n is "G" or n is "C"):
      c = c + 1
  return (c / len(seq)) * 100

def parse_fasta(file):
  seq = ''
  sequences = {}
  for line in file:
    if line[0] is '>': 
      seq = line[1:].rstrip()
      sequences[seq] = ''
    else:
      sequences[seq] += line.rstrip()
  return sequences

gcs = {}
sequences = parse_fasta(f)
for s in sequences:
  gcs[s] = gc(sequences[s])


max_gc = max(gcs, key=gcs.get)

print(f'{max_gc}\n{gcs[max_gc]}')
