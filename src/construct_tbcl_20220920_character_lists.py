# coding: utf-8
# TBCL-20220920-characters.csv is an extraction of
# TBCL-20220920-characters-scrape.html which is a curl of
# https://coct.naer.edu.tw/standsys/querychar.php?q=&num=4000&page=1&deng_ji=all
# with a computer-friendly copy at
# https://github.com/sneaky-foxes/tbcl

from itertools import chain
import csv

class TBCL():
    """Code to turn TBCL scrape into TBCL character list"""
    def __init__(self):
        self.sets = [set(), set(), set(), set(), set(), set(), set()]
        self.read_in_characters()
        self.clean_sets()

    def print_sets(self):
        for ii in range(7):
            cset = sorted(list(self.sets[ii]))
            print('TBCL (20220920) ' + str(ii + 1) + ': ' + ''.join(cset))

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
        if string == '第1級':
            return 0
        elif string == '第1*級':
            return 0
        elif string == '第2級':
            return 1
        elif string == '第2*級':
            return 1
        elif string == '第3級':
            return 2
        elif string == '第3*級':
            return 2
        elif string == '第4級':
            return 3
        elif string == '第4*級':
            return 3
        elif string == '第5級' :
            return 4
        elif string == '第6級':
            return 5
        elif string == '第7級':
            return 6
        else:
            raise Exception('Should not reach here, string = ' + string)

    def read_in_characters(self):

        with open('data/TBCL-20220920-characters.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                word = row["漢字"]
                level = self.level_to_int(row["級別"])
                for char in word:
                    self.sets[level].add(char)

    def clean_non_hanzi(self):
        """Clean out pronunciation clarification"""
        tones = ["ˉ", "ˊ", "ˇ", "ˋ", "˙"]
        zhuyin = ["ㄇ", "ㄋ", "ㄎ", "ㄑ", "ㄕ", "ㄘ", "ㄨ", "ㄜ", "ㄠ", "ㄤ", "ㄆ", "ㄊ", "ㄍ", "ㄐ", "ㄔ", "ㄗ", "ㄧ",
                "ㄛ", "ㄟ", "ㄣ", "ㄈ", "ㄌ", "ㄏ", "ㄒ", "ㄖ", "ㄙ", "ㄩ", "ㄝ", "ㄡ", "ㄥ", "ㄅ", "ㄉ", "ㄓ", "ㄚ",
                "ㄞ", "ㄢ", "ㄦ"] # Carefully copied from keyboard references to avoid twinned hanzi
        punc = ["/", "(", ")", " ", "（", "）", "／"]
        other = [""] # I have no idea what this is!

        for set_ in self.sets:
            for char in chain(tones, zhuyin, punc, other):
                if char in set_:
                    set_.remove(char)

if __name__ == "__main__":
    tbcl = TBCL()
    tbcl.print_sets()
