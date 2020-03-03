import os
import string
import collections
from nltk.tokenize import word_tokenize


entire_line = []
name = []
answer_key = []
student_line = []
lines = []
d = collections.defaultdict(list)
resultword = ''
part1 = []
part2 = []
part3 = []
part4 = []
result = []


word_list = ["is","an","a","the", "in", "on", "and", "are", "to", "of", "also","thereby", "for", "as", "which"]


def files():
    key_file = open('/Users/Tingting/PycharmProjects/Essay/EssayAssessment/data/Insulin Key', 'r')
    student_file = open('/Users/Tingting/PycharmProjects/Essay/EssayAssessment/data/insulin.txt','r')

    with open('outfile.txt', 'w') as output:
        output.write('')

    parse_key(key_file)
    parse_student(student_file)
    compare()
    # parse_key_four_part(key_file)
    # student_id()
    # compare_four_part()

def main_comparison(key_string, input_string):

    words = set(key_string)
    with open('outfile.txt', 'a') as output:
        for word in words:
            output.write(
                '{} appears {} times in key file  and {} times in student file.\n'.format(word, key_string.count(word),
                                                                                          input_string.count(word)))
    output.close()



def parse_key(file1):
    global resultword
    data = file1.readlines()

    for line in data:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        new_line = line.translate(table) # clear all punctuation
        new_line = new_line.replace('\t',' ')
        words = new_line.replace('\n','')
        lines.append(words)

        for whole_line in lines:
            word = whole_line.split()
            resultword = [w for w in word if w.lower() not in word_list ]
            resultword = ' '.join(resultword)
        resultword = resultword.split(' ',1)[1]
    # compare()
    # return resultword

def parse_key_four_part(file1):
    global resultword
    data = file1.readlines()

    for line in data:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        new_line = line.translate(table) # clear all punctuation
        lines.append(new_line)

        for whole_line in lines:
            word = whole_line.split('\t')
            for word1 in word:
                word = word1.split()
                # for word2 in word:
                resultword = [w for w in word if w.lower() not in word_list ]
                # resultword = ' '.join(resultword)
                result.append(resultword)

    part1.append(result[1])
    part2.append(result[2])
    part3.append(result[3])
    part4.append(result[4])
    student_id()
    return

        # resultword = resultword.split(' ',1)[1]
    # return resultword



def parse_student(file2):
    data = file2.readlines()
    for line in data:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        new_line = line.translate(table) #clear all punctuation
        word = new_line.split()
        resultword = [w for w in word if w.lower() not in word_list] # clear some words not need
        resultword = ' '.join(resultword)
        studentID = resultword.split(' ',1)[0]
        student_answer = resultword.split(' ',1)[1]
        d[studentID].append(student_answer) # using dict method(key:value) studentID is the key, the student answer is value.

    return

#compare word by word
#compare with one line
def compare():
    global resultword
    word1 = resultword.split()
    # for word2 in d.values():
    #     for word3 in word2:
    #         word4 = word3.split()
    #         with open('outfile.txt', 'w') as output:
    #             output.write('\n')
    #         main_comparison(word1, word4)
    for key, value in d.items():
        for word3 in value:
            word4 = word3.split()
            with open('outfile.txt', 'a') as output:
                output.write('\nstudent id: {}\n'.format(key))
                output.write('combine key_string in one line:\n')
            main_comparison(word1, word4)


def student_id():
    for key, value in d.items():
        with open('outfile.txt', 'a') as output:
            output.write('\nstudent id: {}\n'.format(key))
        compare_four_part()


def compare_four_part():
    global part1,part2,part3,part4

    for value in d.values():
        for word in value:
            word4 = word.split()
    for word_i in part1:
        with open('outfile.txt', 'a') as output:
            output.write('part 1: \n')
        main_comparison(word_i,word4)
    for word_i in part2:
        with open('outfile.txt', 'a') as output:
            output.write('part 2: \n')
        main_comparison(word_i, word4)
    for word_i in part3:
        with open('outfile.txt', 'a') as output:
            output.write('part 3: \n')
        main_comparison(word_i, word4)
    for word_i in part4:
        with open('outfile.txt', 'a') as output:
            output.write('part 4: \n')
        main_comparison(word_i, word4)

    # return student_id()


if __name__ == '__main__':
    files()




