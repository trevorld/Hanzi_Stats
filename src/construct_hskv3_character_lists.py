# coding: utf-8
# HSK-2012-words.txt is the export of first sheet from
# http://files.hskhsk.com/lists/HSK-2012.xls
# which is supposed to be a copy of the official word lists

import csv

class HSK():
    """Code to turn HSK word list into HSK character list"""
    def __init__(self):
        self.sets = [set(), set(), set(), set(), set(), set(), set()]
        self.read_in_characters()
        self.clean_sets()

    def print_sets(self):
        for ii in range(7):
            cset = sorted(list(self.sets[ii]))
            if ii < 6:
                print('HSK (2021) Band ' + str(ii + 1) + ': ' + ''.join(cset))
            else:
                print('HSK (2021) Bands 7-9: ' + ''.join(cset))

    def clean_sets(self):
        for set_ in self.sets:
            if '…' in set_:
                set_.remove('…')
        for ii in range(7):
            for jj in range(7):
                if ii < jj:
                    self.sets[jj].difference_update(self.sets[ii])

    def level_to_int(self, string):
        """string - something like '六级）'"""
        string = string.rstrip()
        if string == 'HSK1':
            return 0
        elif string == 'HSK2':
            return 1
        elif string == 'HSK3':
            return 2
        elif string == 'HSK4':
            return 3
        elif string == 'HSK5' :
            return 4
        elif string == 'HSK6':
            return 5
        elif string == 'HSK7*':
            return 6
        elif string == 'HSK8*':
            return 6
        elif string == 'HSK9*':
            return 6
        else:
            raise Exception('Should not reach here, string = ' + string)

    def read_in_characters(self):

        f_words = csv.DictReader(open('data/HSK-2021-words.csv'))

        for row in f_words:
            word = row['word']
            level = row['tag']
            level = self.level_to_int(level)
            for char in word:
                self.sets[level].add(char)

if __name__ == "__main__":
    hsk = HSK()
    hsk.print_sets()
