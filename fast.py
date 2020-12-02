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

def FASTAReader(file):
 data = []
 hlavicka = []
 sekvence = []

 with open(file, 'r') as f:
        data = f.readlines()

 iter_NextLine = NextLine(data)
 bool = False
 for line in iter_NextLine:
        for char in line:
             if char == '>':
                 hlavicka.append(line)
                 bool = False
                 break
             else:
                 bool = True
        if bool == True:
             sekvence.append(line)
 return hlavicka,sekvence










