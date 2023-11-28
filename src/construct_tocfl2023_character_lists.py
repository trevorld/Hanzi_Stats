# coding: utf-8
# TOCFL-2023-words.csv is the words from the Chinese Eight Thousand Vocabulary List
# at https://tocfl.edu.tw/index.php/exam/download
# with a computer-friendly copy forked from PSeitz/tocfl at
# https://github.com/sneaky-foxes/tocfl

import csv
from itertools import chain

class TOCFL():
    """Code to turn TOCFL word list into TOCFL character list"""
    def __init__(self):
        self.sets = [set(), set(), set(), set(), set(), set(), set()]
        self.read_in_characters()
        self.clean_sets()

    def print_sets(self):
        for ii in range(7):
            cset = sorted(list(self.sets[ii]))
            if ii < 2:
                print('TOCFL (2023) Novice ' + str(ii + 1) + ': ' + ''.join(cset))
            else:
                print('TOCFL (2023) ' + str(ii - 1) + ': '+ ''.join(cset))

    def clean_sets(self):
        self.clean_non_hanzi()

        # remove already seen hanzi from upper levels
        for ii in range(7):
            for jj in range(7):
                if ii < jj:
                    self.sets[jj].difference_update(self.sets[ii])

    def level_to_int(self, string):
        """Convert the level into an indexable integer"""
        string = string.rstrip()
        if string == 'TOCFL Novice 1':
            return 0
        elif string == 'TOCFL Novice 2':
            return 1
        elif string == 'TOCFL 1':
            return 2
        elif string == 'TOCFL 2':
            return 3
        elif string == 'TOCFL 3' :
            return 4
        elif string == 'TOCFL 4':
            return 5
        elif string == 'TOCFL 5':
            return 6
        else:
            raise Exception('Should not reach here, string = ' + string)

    def read_in_characters(self):

        f_words = csv.DictReader(open('data/TOCFL-2023-words.csv'))

        for row in f_words:
            word = row['word']
            level = row['tag']
            level = self.level_to_int(level)
            for char in word:
                self.sets[level].add(char)

    def clean_non_hanzi(self):
        """Clean out pronunciation clarification"""
        tones = ["ˉ", "ˊ", "ˇ", "ˋ", "˙"]
        zhuyin = ["ㄇ", "ㄋ", "ㄎ", "ㄑ", "ㄕ", "ㄘ", "ㄨ", "ㄜ", "ㄠ", "ㄤ", "ㄆ", "ㄊ", "ㄍ", "ㄐ", "ㄔ", "ㄗ", "ㄧ",
                "ㄛ", "ㄟ", "ㄣ", "ㄈ", "ㄌ", "ㄏ", "ㄒ", "ㄖ", "ㄙ", "ㄩ", "ㄝ", "ㄡ", "ㄥ", "ㄅ", "ㄉ", "ㄓ", "ㄚ",
                "ㄞ", "ㄢ", "ㄦ"] # Carefully copied from keyboard references to avoid twinned hanzi
        punc = ["/", "(", ")", " ", "（", "）"]
        other = [""] # I have no idea what this is!

        for set_ in self.sets:
            for char in chain(tones, zhuyin, punc, other):
                if char in set_:
                    set_.remove(char)

if __name__ == "__main__":
    tocfl = TOCFL()
    tocfl.print_sets()
