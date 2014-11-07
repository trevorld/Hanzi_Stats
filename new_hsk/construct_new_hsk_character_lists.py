# coding: utf-8
# HSK-2012-words.txt is the export of first sheet from
# http://files.hskhsk.com/lists/HSK-2012.xls 
# which is supposed to be a copy of the official word lists

class HSK():
    """Code to turn HSK word list into HSK character list"""
    def __init__(self):
        self.sets = [set(), set(), set(), set(), set(), set()]
        self.read_in_characters()
        self.clean_sets()

    def print_sets(self):
        for ii in range(6):
            cset = sorted(list(self.sets[ii]))
            print('New HSK Level ' + str(ii + 1) + ': ' + ''.join(cset))

    def clean_sets(self):
        for set_ in self.sets:
            if '…' in set_:
                set_.remove('…')
        for ii in range(6):
            for jj in range(6):
                if ii < jj:
                    self.sets[jj].difference_update(self.sets[ii])

    def level_to_int(self, string):
        """string - something like '六级）'"""
        string = string.rstrip()
        if string == '一级）':
            return 0
        elif string == '二级）':
            return 1
        elif string == '三级）':
            return 2
        elif string == '四级）':
            return 3
        elif string == '五级）' :
            return 4
        elif string == '六级）':
            return 5
        else:
            raise Exception('Should not reach here.')

    def read_in_characters(self):

        f_words = open('HSK-2012-words.txt')

        for line in f_words:
            word_note_level = line.split('（')
            if len(word_note_level) == 2:
                word, level = word_note_level
            else:
                word, note, level = word_note_level
            level = self.level_to_int(level)
            for char in word:
                self.sets[level].add(char)

if __name__ == "__main__":
    hsk = HSK()
    hsk.print_sets()

