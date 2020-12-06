from fastaQ import FASTAQReader


g = FASTAQReader("data.fq")

for i in g:
    print(i)

