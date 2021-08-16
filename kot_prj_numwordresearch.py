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
    """
    fig, ax = plt.subplots()

    ax.bar(uniq_char, uniq_c_cnt)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)    #  ширина Figure
    fig.set_figheight(6)    #  высота Figure

    plt.show()
    """
    f=open('word_list_i1reg', 'rb')
    word_list=pickle.load(f)
    f.close()
    f=open('word_list_i1obscene', 'rb')
    word_list_obscene=pickle.load(f)
    f.close()
    uniq_word, uniq_w_cnt= np.unique(word_list, return_counts=True)
    uniq_word_obs, uniq_w_cnt_obs= np.unique(word_list_obscene, return_counts=True)
    print(len(uniq_w_cnt))
    print(len(uniq_w_cnt_obs))
    
    f=open('word_dict_obscene.txt', 'r')
    word=f.read()
    word=word.split('\n')
    word_str=''
    for i in word:
        word_str+=i
    word_str=list(word_str)
    word_str_unq, word_cnt_unq=np.unique(word_str, return_counts=True)
    print(word_str_unq, word_cnt_unq)
    
    fig, ax = plt.subplots()

    ax.bar(word_str_unq, word_cnt_unq)

    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)    #  ширина Figure
    fig.set_figheight(6)    #  высота Figure

    plt.show()
    
    #Печать слов различного состава
    '''
    print('Обычный словарь\n-------------------')
    for i in uniq_word:
        if len(i)==5:
            print(i)
    print('\nНеобычный словарь\n-------------------')
    for i in uniq_word_obs:
        if len(i)==5:
            print(i)
    #Распределение слов по количеству букв в них
    '''
    '''
    uniq_w_len=[]
    for i in uniq_word:
        uniq_w_len.append(len(i))
    print(uniq_w_len)
    print(np.unique(uniq_w_len, return_counts=True))
    
    uniq_w_len_obs=[]
    for i in uniq_word_obs:
        uniq_w_len_obs.append(len(i))
    print(uniq_w_len_obs)
    print(np.unique(uniq_w_len_obs, return_counts=True))
    '''
        