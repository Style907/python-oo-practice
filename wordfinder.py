"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, input):
        self.input = input
        self.file = open(input)
        self.readfile()

    def readfile(self):
        count = 0
        
        for line in self.file:
            count +=1
        self.file.close()

        print(f"{count} words read")

    def random(self):
        
        print(random.choice(open(self.input).read().split()))


class SpecialWordFinder(WordFinder):
    

    def parse(self, file):
       

        return [w.strip() for w in file
                if w.strip() and not w.startswith("#")]

        
