import enchant
import urllib.request as reqq
import pickle

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
Данный файл предназначен для полученния букв и поиска слов"
'''

dict=enchant.Dict("ru_RU")

def req(num, min, max):
    #делаем гет-запрос
    res=reqq.urlopen('https://www.random.org/integers/?num='+str(num)+'&min='+str(min)+'&max='+str(max)+'&col=1&base=10&format=plain&rnd=new')
    #дешефруем и создаем список
    res_seq=res.read().decode('utf-8').split('\n')
    #переводим из str в int
    res_seq=[int(i) for i in res_seq[:-1]]
    return res_seq

def find_word(char_list):
    cursor=0
    word_list=[]
    flag=0
    while cursor!=len(char_list):
        i=1
        word=''.join(char_list[cursor:cursor+i])
        while len(word)<=15:
            if len(word)<i:
                break
            if dict.check(word):
                #word_list.append(word)
                flag=1
                #break
            else:
                #flag=0
                if flag==1:
                    flag=0
                    word_list.append(word[:-1])
                    break
            i+=1                    
            word=''.join(char_list[cursor:cursor+i])
        print(cursor)
        if flag==0:
            cursor+=1
        else:
            #cursor=cursor+i
            cursor+=1
    return word_list

#char_list=req(10000, 97, 122)#в ASCII 97 - a, 122 - z
#char_list=req(2000, 1072, 1103)#в ASCII 1072 - а, 1103 - я
#f=open('char_list', 'wb')
#pickle.dump(char_list, f)
f=open('char_list', 'rb')
big_list=pickle.load(f)
f.close()
char_list=[]
for i in big_list:
    char_list+=i
char_list=[chr(i) for i in char_list]
w_ls=find_word(char_list)
f=open('word_list_i1reg', 'wb')
pickle.dump(w_ls, f)
f.close()
#print(w_ls)
#print(len(w_ls))