#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

my_list = {}

for line in sys.stdin:
    line = line.strip()
    word, value = line.split('\t')

    if word in my_list:
        my_list[word].append(float(value))
    else:
        my_list[word] = []
        my_list[word].append(float(value))

for word in my_list.keys():
    sum_word = sum(my_list[word])
    aver_word = sum(my_list[word])/ len(my_list[word])
    print ('%s\t%s\t%s'% (word, sum_word, aver_word))