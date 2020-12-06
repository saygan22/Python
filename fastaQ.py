class NextLine:

    def __init__(self, objekt):
        self.objekt = objekt
        self.indexline = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.indexline += 1
        if self.indexline == len(self.objekt):
            raise StopIteration
        return self.objekt[self.indexline]

def FASTAQReader(file):

 hlavicka = []
 sekvence = []
 komentar = []
 kvalita_cteni = []

 with open(file, 'r') as f:
        data = []
        data = f.readlines()

 iter_NextLine = NextLine(data)
 count_line = 1
 for line in iter_NextLine:

    while count_line <= 4:

       if count_line == 1:
           hlavicka.append(line.rstrip())
           count_line = count_line + 1
           break
       elif count_line == 2:
           sekvence.append(line.rstrip())
           count_line = count_line + 1
           break
       elif count_line == 3:
           komentar.append(line.rstrip())
           count_line = count_line + 1
           break
       elif count_line == 4:
           kvalita_cteni.append(line.rstrip())
           count_line = count_line + 1
           break
    if count_line == 5:
        count_line = count_line - 4
 return hlavicka,sekvence,komentar,kvalita_cteni
