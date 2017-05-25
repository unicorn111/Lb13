from arraystack import *


class Palindrome:
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = []
        self.palindromes = []

    def read(self):
        if self.file_name == 'words.txt':
            file = open(self.file_name, 'r')
            words1 = file.readlines()
            for i in words1:
                i = i.strip()
                self.words.append(i)
            file.close()
        else:
            file = open(self.file_name, 'r')
            words1 = file.readlines()
            for i in words1:
                i = i.strip()
                i = i.split()
                print(i[0])
                self.words.append(i[0])
            file.close()
        return self.words

    def is_palindrome(self):
        for s in self.words:
            if len(s) % 2 == 0:
                a = int(len(s) / 2)
                s1 = s[:a]
                s2 = s[a:]
                st1 = ArrayStack()
                ct = len(s2)
                for i in s2:
                    st1.push(i)
                n_s2 = ''
                while ct != 0:
                    n_s2 += st1.peek()
                    st1.pop()
                    ct -= 1
                if s1 == n_s2:
                    self.palindromes.append(s)
                else:
                    continue
            else:
                a = int(len(s) // 2)
                s1 = s[:a]
                s2 = s[a + 1:]
                st1 = ArrayStack()
                ct = len(s2)
                for i in s2:
                    st1.push(i)
                n_s2 = ''
                while ct != 0:
                    n_s2 += st1.peek()
                    st1.pop()
                    ct -= 1
                if s1 == n_s2:
                    self.palindromes.append(s)
                else:
                    continue
        return self.palindromes

    def write(self):
        if self.file_name == 'words.txt':
            with open('palindrome_en.txt', 'w') as output_file:
                for i in self.palindromes:
                    output_file.write(i + '\n')
        else:
            with open('palindrome_uk.txt', 'w') as output_file:
                for i in self.palindromes:
                    output_file.write(i + '\n')


def check():
    a = Palindrome('base.lst')
    a.read()
    a.is_palindrome()
    a.write()
check()
