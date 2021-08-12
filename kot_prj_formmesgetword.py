'''
Created on 5 Р°РІРі. 2021 Рі.

@author: Smirnov Alexey
Laboratory Assistant
EC GAZ Group "LIPGART"
Bauman Moscow State Technical University
tg: @lelikbezbolika
private e-mail: aasmr@ya.ru
work e-mail: smirnov@bmstu.ru

Р Р°Р·СЂРµС€Р°РµС‚СЃСЏ СЃРІРѕР±РѕРґРЅРѕРµ РёСЃРїРѕР»СЊР·РѕРІР°РЅРёРµ СЃ СЃСЃС‹Р»РєРѕР№ РЅР° РёСЃС‚РѕС‡РЅРёРє
'''

'''
Р”Р°РЅРЅС‹Р№ С„Р°Р№Р» РїСЂРµРґРЅР°Р·РЅР°С‡РµРЅ РґР»СЏ РїРѕР»СѓС‡РµРЅРЅРёСЏ СЃРїРёСЃРєР° СѓРЅРёРєР°Р»СЊРЅС‹С… СЃР»РѕРІ,
РёСЃРїРѕР»СЊР·СѓРµРјС‹С… РјРЅРѕР№ РІ РїРµСЂРµРїРёСЃРєРµ. Р�Р· СЃРїРёСЃРєР° Р±СѓРґСѓС‚ СѓРґР°Р»РµРЅС‹ РёРјРµРЅР°. РђСЂС…РёРІ РїРµСЂРµРїРёСЃРѕРє РІ РѕР±С‰РµРј
РґРѕСЃС‚СѓРїРµ РЅРµ РґРѕСЃС‚СѓРїРµРЅ РЅРµ Р±СѓРґРµС‚.
Р‘СѓРґРµС‚ РґРѕСЃС‚СѓРїРЅРѕ РґРІР° СЃРїРёСЃРєР° СЃР»РѕРІ: СЃРѕРґРµСЂР¶Р°С‰РёС… РѕР±СЃС†РµРЅРЅСѓСЋ Р»РµРєСЃРёРєСѓ Рё С†РµРЅР·СѓСЂРёСЂРѕРІР°РЅРЅС‹Р№
'''

import os, re
import numpy as np
import enchant

class calc_word:
    def __init__(self):
        self.word_dict={}
        self.words=[]
    def openfandsearch(self, url):
        
        file=open(url, 'r')
        _str=file.read()
        res=re.findall(r'  <div class="message__header">Р’С‹,(.+)</div>\n  <div>(.+)<div class="kludges"></div></div>', _str)
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
#     f=open('word_dict.txt', 'r')
#     word_dict=f.read()
#     f.close()
#     word_dict=word_dict.split('\n')
#     word_dict=np.unique(word_dict)
#     f=open('word_dict.txt', 'w')
#     for i in word_dict:
#         f.write(i+'\n')
#     f.close()
    f=open('word_dict.txt', 'r')
    word_dict=f.read()
    f.close()
    word_dict=word_dict.split('\n')
    dict=enchant.Dict("ru_RU")
    try:
        f=open('word_dict_new.txt', 'r')
        word_dict_new=f.read()
        f.close()
        word_dict_new=word_dict_new.split('\n')
    except:
        word_dict_new=[]
    for i in word_dict:
        if word_dict.index(i)<30004:
            continue
        if dict.check(i)==False:
            print(i+'\n')
            print(word_dict.index(i), word_dict.index(i)/len(word_dict)*100)
            res=input()
            if res=='x':
                print(word_dict.index(i))
                break
            elif res=='re':
                print(word_dict.index(i))
                continue
            elif res=='':
                print(word_dict.index(i))
                word_dict_new.append(i)
            else:
                print(word_dict.index(i))
                i=res
                i=i.split(' ')
                word_dict_new=word_dict_new+i
        else:
            word_dict_new.append(i)
            
    f=open('word_dict_new.txt', 'w')
    for i in word_dict_new:
        f.write(i+'\n')
    f.close()
                
    
    
    
    