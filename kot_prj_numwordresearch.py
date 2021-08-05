'''
Created on 5 авг. 2021 г.

@author: Smirnov Alexey
Laboratory Assistant
EC GAZ Group "LIPGART"
Bauman Moscow State Technical University
tg: @lelikbezbolika
private e-mail: aasmr@ya.ru
work e-mail: smirnov@bmstu.ru

Разрешается свободное использование с ссылкой на источник
'''

'''
Данный файл предназначен для изучения полученных букв и слов"
'''
import pickle
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    f=open('char_list', 'rb')
    char_list=pickle.load(f)
    f.close()
    uniq_char, uniq_c_cnt= np.unique(char_list, return_counts=True)
    uniq_char=[chr(i) for i in uniq_char]
    fig, ax = plt.subplots()

    ax.bar(uniq_char, uniq_c_cnt)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)    #  ширина Figure
    fig.set_figheight(6)    #  высота Figure

    plt.show()
    
    f=open('word_list_i1reg', 'rb')
    word_list=pickle.load(f)
    f.close()
    f=open('char_list', 'rb')
    char_list=pickle.load(f)
    f.close()
    uniq_word, uniq_w_cnt= np.unique(word_list, return_counts=True)
    print(len(uniq_w_cnt))
    uniq_w_len=[]
    for i in uniq_word:
        uniq_w_len.append(len(i))
    print(uniq_w_len)
    print(np.unique(uniq_w_len, return_counts=True))
        