from fast import FASTAReader


g = FASTAReader("FASTA.txt")

for i in g:
    print(i)

