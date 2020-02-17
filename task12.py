str_ = input("Write a sentence: ")
first = str_.index('f')
str_back = str_[::-1]
last = str_back.index('f')
print('Index of first F:{}'.format(first))
print('Index of last F:{}'.format(last))
