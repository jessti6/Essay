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

word_list = ["is","an","a","the", "in", "on", "and", "are", "to", "of", "also","thereby", "for", "as"]


def files():
    key_file = open('/Users/Tingting/PycharmProjects/Essay/EssayAssessment/data/Insulin Key', 'r')
    student_file = open('/Users/Tingting/PycharmProjects/Essay/EssayAssessment/data/insulin.txt','r')

    parse_key(key_file)
    parse_student(student_file)
    compare()

def parse_key(file1):
    # count = 0
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
    return resultword

        # print(resultword)
    # return


def parse_student(file2):
    data = file2.readlines()
    for line in data:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        new_line = line.translate(table) #remove all punctuation
        word = new_line.split()
        resultword = [w for w in word if w.lower() not in word_list] # clear some words
        resultword = ' '.join(resultword)
        # print(resultword)
        # for line in resultword:
        studentID = resultword.split(' ',1)[0]
        student_answer = resultword.split(' ',1)[1]
        d[studentID].append(student_answer) # using dict method(key:value) studentID is the key, the answer is value.

    # print(d)
    return

#compare word by word
#or find the similarity of two documents
def compare():
    global resultword
    word1 = resultword.split()
    for word2 in d.values():
        for word3 in word2:
            word4 = word3.split()

    # dictionary = gensim.corpora.Dictionary(gen_docs)
            words = set(word1) & set(word4)
            with open('outfile.txt', 'w') as output:
                for word in words:
                    output.write(
                        '{} appears {} times in key file  and {} times in student file.\n'.format(word, word1.count(word), word4.count(word)))
    # avg_sims = []
    # for line in d.values():
    #     query_doc = [w.lower() for w in word_tokenize(line)]
        # query_doc_bow = dictionary.doc2bow(query_doc)





# def clear():
#     global answer_key
#     for whole_line in answer_key:
#         for line in whole_line:
#             word = line.split()
#             resultword = [w for w in word if w.lower() not in word_list ]
#             resultword = ' '.join(resultword)
#
            # word2 = new_line.split()

            # for line2 in word2:
            #     resultword = [w for w in line2 if w.lower() not in word_list]
            #     resultword = ''.join(resultword)

            # print(new_line)




if __name__ == '__main__':
    files()




