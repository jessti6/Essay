import string

entire_line = []
name = []
answer_key = []
student_line = []

word_list = ["is","an","a","the", "on", "and", "to", "of", "also","thereby"]

def parse_key():
    f = open('/Users/Tingting/PycharmProjects/EssayAssessment/data/key.txt', 'r')
    data = f.readlines()

    for line in data:
        if line.endswith('\n'):
            entire_line.append(line)
            words = line.split('\t')
            name.append(words[0])
            answer_key.append(words[1:5])

def parse_student():
    f = open('/Users/Tingting/PycharmProjects/EssayAssessment/data/insulin.txt','r')
    data = f.readlines()

    for line in data:
        if line.endswith('\n'):
            answer = line.split('\t')
            student_line.append(answer[1])


def clear():
    global answer_key
    for whole_line in answer_key:
        for line in whole_line:
            word = line.split()
            resultword = [w for w in word if w.lower() not in word_list ]
            resultword = ' '.join(resultword)

            table = str.maketrans(dict.fromkeys(string.punctuation))
            new_line = resultword.translate(table)
            # word2 = new_line.split()

            # for line2 in word2:
            #     resultword = [w for w in line2 if w.lower() not in word_list]
            #     resultword = ''.join(resultword)

            print(new_line)















