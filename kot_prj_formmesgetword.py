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
Данный файл предназначен для полученния списка уникальных слов,
используемых мной в переписке. Из списка будут удалены имена. Архив переписок в общем
доступе не доступен не будет.
Будет доступно два списка слов: содержащих обсценную лексику и цензурированный
'''

import os, re
import numpy as np
class calc_word:
    def __init__(self):
        self.word_dict={}
        self.words=[]
    def openfandsearch(self, url):
        
        file=open(url, 'r')
        _str=file.read()
        res=re.findall(r'  <div class="message__header">Вы,(.+)</div>\n  <div>(.+)<div class="kludges"></div></div>', _str)
        if len(res)!=0:
            for i in res:
                #print(i)
                text_f.write(i[1]+'\n')
                self.calc(i[1])
                self.parse(i[1])

    def parse(self, _str):
        _words=_str.split(' ')
        for i in _words:
            i=re.sub(r'[^\w\s]','', i)
            i=i.lower()
            self.words.append(i)
            
        
            
    def calc(self, _str):
        words=_str.split(' ')
        for i in words:
            i=re.sub(r'[^\w\s]','', i)
            i=i.lower()
            if i in self.word_dict:
                self.word_dict[i]=self.word_dict[i]+1
            else:
                self.word_dict[i]=1      
if __name__=='__main__':
#     calc=calc_word()
#     _dir='your_vk_archive_dir'
#     _indir=os.listdir(_dir)
#     s=len(_indir)
#     k=0
#     text_f=open('./mes.txt', 'w')
#     for i in _indir:
#         _ndir=_dir+i
#         try:
#             _file=os.listdir(_ndir)
#         except:
#             pass
#         for f in _file:
#             f_url=_ndir+'/'+f
#             try:
# 
#                 calc.openfandsearch(f_url)
#             except:
#                 pass
#         k=k+1
#         print(k/s*100)
#     text_f.close()
#     calc.words=np.unique(calc.words)
#     #print(calc.words)
#     f=open('word_dict.txt', 'w')
#     for i in calc.words:
#         f.write(i+'\n')
#     f.close()
    f=open('word_dict_obscene.txt', 'r')
    word_dict=f.read()
    f.close()
    word_dict.split('\n')
    word_dict=np.unique(word_dict)
    f=open('word_dict.txt', 'w')
    for i in word_dict:
        f.write(i+'\n')
    f.close()