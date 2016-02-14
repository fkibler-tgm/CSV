__author__ = 'Florian Kibler'

import csv, codecs

class Converter():
    def __init__(self, filename):
        self.inhalt=None
        f = open(filename, 'r')
        self.reader = csv.reader(f, dialect=csv.excel)

    def opencsv(self):
        self.inhalt = ''
        for row in self.reader:
            self.inhalt+=row

    def recognize(self):
        sn = csv.Sniffer()
        s = sn.sniff(self.opencsv())
        return s.delimiter



c = Converter('csv.txt')
c.opencsv()
print(c.inhalt)
