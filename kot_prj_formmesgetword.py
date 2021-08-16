'''
Created on 5 Р°РІРі. 2021 Рі.

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
доступе доступен не будет.
Будет доступно два списка слов: содержащих обсценную лексику и цензурированный
'''

import os, re
import numpy as np
import enchant
###
#ПОИСК И ПОДСЧЕТ СЛОВ в СООБЩЕНИЯХ ВК
###
class calc_word:
    def __init__(self):
        self.word_dict={}
        self.words=[]
        self.text_f=''
    def openfandsearch(self, url):
        #Поиск сообщений
        file=open(url, 'r')
        _str=file.read()
        res=re.findall(r'  <div class="message__header">Р’С‹,(.+)</div>\n  <div>(.+)<div class="kludges"></div></div>', _str)
        if len(res)!=0:
            for i in res:
                #print(i)
                self.text_f.write(i[1]+'\n')
                self.calc(i[1])
                self.parse(i[1])
    #Разбиение сообщений на слова
    def parse(self, _str):
        _words=_str.split(' ')
        for i in _words:
            i=re.sub(r'[^\w\s]','', i)
            i=i.lower()
            self.words.append(i)
    #Подсчет уникальных слов без NumPy        
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
    #Выделение из нового словаря уникальных слов
    f=open('word_dict_new.txt', 'r')
    word_dict_new=f.read()
    f.close()
    word_dict_new=word_dict_new.split('\n')
    word_dict=np.unique(word_dict_new)
    f=open('word_dict_obscene.txt', 'w')
    for i in word_dict:
        f.write(i+'\n')
    f.close()
###
#Выделение сообщений из всех диалогов"        
#     calc=calc_word()
#     _dir='your_vk_archive_dir'
#     _indir=os.listdir(_dir)
#     s=len(_indir)
#     k=0
#     calc.text_f=open('./mes.txt', 'w')
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
###

###
#Запись уникальных слов в файл
#     f=open('word_dict.txt', 'w')
#     for i in calc.words:
#         f.write(i+'\n')
#     f.close()
###

###
#Для исправления опечаток
#     f=open('word_dict.txt', 'r')
#     word_dict=f.read()
#     f.close()
#     word_dict=word_dict.split('\n')
#     dict=enchant.Dict("ru_RU")
#     try:
#         f=open('word_dict_new.txt', 'r')
#         word_dict_new=f.read()
#         f.close()
#         word_dict_new=word_dict_new.split('\n')
#     except:
#         word_dict_new=[]
#     for i in word_dict:
#         if word_dict.index(i)<48859:
#             continue
#         if dict.check(i)==False:
#             print(i+'\n')
#             print(word_dict.index(i), word_dict.index(i)/len(word_dict)*100)
#             res=input()
#             if res=='x':
#                 print(word_dict.index(i))
#                 break
#             elif res=='re':
#                 print(word_dict.index(i))
#                 continue
#             elif res=='':
#                 print(word_dict.index(i))
#                 word_dict_new.append(i)
#             else:
#                 print(word_dict.index(i))
#                 i=res
#                 i=i.split(' ')
#                 word_dict_new=word_dict_new+i
#         else:
#             word_dict_new.append(i)
#             
#     f=open('word_dict_new.txt', 'w')
#     for i in word_dict_new:
#         f.write(i+'\n')
#     f.close()
###                
    
    
    
    