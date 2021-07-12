# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:39:37 2020
#Total Line count 212
@author: Dev Bhardwaj
"""

import matplotlib.pyplot as plt
import mysql.connector as sql
mycon=sql.connect(user='root',passwd='root',database='school')
cursor=mycon.cursor()
def guess(word,lw):
    wrong=correct=nscore=0
    itsw=[]
    nrwl=[]
    for k in lw:
        if k not in nrwl:
            nrwl.append(k)
    vowels=['a','e','i','o','u']
    diagram=(" __________\n |        \n |        \n |         \n |        \n |        ")
    diagramfinal=(" __________\n |        |\n |        O\n |       /|\ \n |        |\n |       / \ ")
    i=1
    while diagram!=diagramfinal:
        print('Attempt',i)
        g=input('enter your guess ')
        if g in lw:
            if g not in itsw:
                itsw.append(g)
                print('CONGRATULATIONS, you guessed it right \n now the new word is ',end="")
                for k in word:
                    if k in itsw or k in vowels:
                        print(k,end=' ')
                    else:
                        print('_ ',end='')
                for m in nrwl:
                    c=word.count(g)
                correct+=c
                nscore+=c
                print()
            else:
                print('sorry you have already given us this word and you lost 1 chance')
        else:
            print('sorry wrong guess\n you loose 1 pt')
            nscore+=-1
            wrong+=1
        diagram=(" __________\n |        \n |        \n |         \n |        \n |        ")
        if wrong==1:
            diagram=(" __________\n |        |\n |        \n |         \n |        \n |        ")
        elif wrong==2:
            diagram=(" __________\n |        |\n |        O\n |         \n |        \n |        ")
        elif wrong==3:
            diagram=(" __________\n |        |\n |        O\n |       /|\ \n |        \n |        ")
        elif wrong==4:
            diagram=(" __________\n |        |\n |        O\n |       /|\ \n |        |\n |         ")
        elif wrong==5:
            diagram=(" __________\n |        |\n |        O\n |       /|\ \n |        |\n |       / \ ")
        print(diagram)
        if correct==len(lw) and correct!=0:
            print('you got the word')
            break
        i+=1
    print('the actual word is',word)
    for k in itsw:
        if k not in nrwl:
            i.remove(k)
    nrwl.sort() , itsw.sort()
    if nrwl==itsw:
        print('yeppie you won')
    else:
        print('sorry better luck next time',len(nrwl)-len(itsw),'letters left')
    return nscore

def plot(scorelist,timelist):
    plt.plot(timelist,scorelist) 
    plt.xlabel('Time') 
    plt.ylabel('Score')
    plt.title('Score V/S Time Graph') 
    plt.show() 

def insert(name,score,pdate,ptime):
        st1=("insert into project(name,score,date,time) values('{}',{},'{}','{}')").format(name,score,pdate,ptime)
        cursor.execute(st1)
        mycon.commit()
        
def select(name):
    st="select name,score,date,time from project where name='%s'" %name
    cursor.execute(st)
    data=cursor.fetchall()
    feild=['name','score','date','time']
    for i in data:
        for j in range(0,4):
            print(feild[j],'=',i[j])
        
