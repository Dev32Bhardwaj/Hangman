# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:56:49 2020
#Total Line count 212
@author: Dev Bhardwaj
"""

import mysql.connector as sql
import functions,os
from random import randrange
from datetime import date,datetime
mycon=sql.connect(user='root',passwd='root',database='school')
cursor=mycon.cursor()
if mycon.is_connected()==True:
    print('Hello Player',end='\n')
print('Welcome to Hangman')
name=input('kindly enter your name ')
name=name.upper()
print()
st="select name,score,date,time from project where name='%s'" %name
cursor.execute(st)
data=cursor.fetchall()
count=cursor.rowcount
curdate=datetime.now()
if count>0:
    for i in data:
        score=i[1]
        ldate=str(i[2])
        ltime=str(i[3])
        ld=ldate.split('-')+ltime.split(':')
        ldatetime=datetime(int(ld[0]),int(ld[1]),int(ld[2]),int(ld[3]),int(ld[4]),int(ld[5]))
        print(name,'your previous score was',score)
        print('you last visited us on',ldate,ltime,'the time gap=',str(curdate-ldatetime),'\n')
else:
    score=ldate=ltime=0
    print('YOU ARE VISITNG FOR THE 1ST TIME')
    print()
print('INSTRUCTIONS: ')
print(' 1.You will have to guess the word asked ')
print(' 2.You will have only 5 lives ')
print(' 3.For every incorect guess you move a step towards the hanging and lose 1 point ')
print(' 4.For every correct answer you get 1 point ')
print(' 5.See if you can avert the \"Hanging\" ')
print('\"BEST OF LUCK\"')
print('*Kindly Enter only in SMALL LETTERS*')
scorelist=[]
ch='yes'
time=[]
file1=open('wordlist.txt')
M=file1.readlines()
wordlist=[]
for n in M:
    n=n.strip('\n')
    ln=n.split(':')
    if ln[0]==name:
        ln[1]=ln[1][1:len(ln[1])-1]
        ln[1]=ln[1].split(',')
        for i in ln[1]:
            i=i[1:len(i)-1]
            wordlist+=[i]
        break
    else:
        wordlist=[]
file1.close()
while ch!='no':
    t=int(input('kindly enter the number of letters you want in the word to guess '))
    print()    
    file=open('words_alpha.txt')
    s=' '
    l=[]
    like=[]
    newwordlist=[]
    while s:
        s=file.readline()
        s=s.strip('\n')
        if len(s)==t:
            l.append(s)
            like.append(s)
    for i in l:
        if i in wordlist:
            l.remove(i)
    if len(l)==0:
        l=like
    index=randrange(len(l))
    word=l[index]
    newwordlist.append(word)
    print('so let us begin')
    vowels=['a','e','i','o','u']
    lw=[]
    nscore=0
    itsw=[]
    for k in word:
        if k in vowels:
            print(k,end=' ')
        else:
            print('_',end=' ')
            lw.append(k)
    print()
    nscore=functions.guess(word,lw)
    print('score=',nscore)
    scorelist.append(nscore)
    time.append(str(datetime.now()-curdate))
    curdate=datetime.now()
    ch=input('do you want to replay the game ')
    wordlist+=newwordlist
    file.close()
print('scorelist=',scorelist)
print('timelist=',time)
if len(scorelist)>1:
    functions.plot(scorelist,time)
if len(scorelist)>1:
    num=int(input('which score do you want to continue with '))-1
    finalscore=scorelist[num]
else:
    finalscore=scorelist[0]
score+=finalscore
print('the net score=',score)
pdate=str(date.today())
tym=datetime.now()
ptime=str(tym.time())
if count==0:
    functions.insert(name,score,pdate,ptime)
    print('your data has been added to our database')
    file1=open("wordlist.txt","a")
    string=name+":"+str(wordlist)+"\n"
    file1.write(string)
    file1.close()
else:
    st2="update project set score={},date='{}',time='{}' where name='{}'".format(score,pdate,ptime,name)
    cursor.execute(st2)
    mycon.commit()
    print('your data has been updated')
    file1=open("wordlist.txt")
    t_rec=open("temp.txt","w+")
    km=file1.readlines()
    for s in km:
        s=s.strip('\n')
        g=s.split(":")
        if g[0]==name:
            string=name+":"+str(wordlist)+"\n"
            t_rec.write(string)
        else:
            t_rec.write(s+'\n')
    t_rec.seek(0)
    file1.close()   
    t_rec.close()
    os.remove("wordlist.txt")
    os.rename("temp.txt","wordlist.txt")
functions.select(name)
change=input('incase of any change type yes ')
while change=='yes':
    feild=input('where do you want a change ')
    newdata=input('what change do you want ')
    if feild=='score':
        newdata=int(newdata)
        st4="update project set score={} where name='{}'".format(newdata,name)
        score=newdata
        cursor.execute(st4)
        mycon.commit()
    elif feild=='name':
        st4="update project set name='{}' where name='{}'".format(newdata,name)
        cursor.execute(st4)
        mycon.commit()
        file1=open("wordlist.txt")
        t_rec=open("temp.txt","w+")
        km=file1.readlines()
        for s in km:
            s=s.strip('\n')
            g=s.split(":")
            if g[0]==name:
                string=newdata+":"+str(wordlist)+"\n"
                t_rec.write(string)
            else:
                t_rec.write(s+'\n')
        t_rec.seek(0)
        file1.close()   
        t_rec.close()
        os.remove("wordlist.txt")
        os.rename("temp.txt","wordlist.txt")
        name=str(newdata).upper
    elif feild=='date':
        st4="update project set date='{}' where name='{}'".format(newdata,name)
        date=newdata
        cursor.execute(st4)
        mycon.commit()
    elif feild=='time':
        st4="update project set time='{}' where name='{}'".format(newdata,name)
        time=newdata
        cursor.execute(st4)
        mycon.commit()
    else:
        print('wrong feild/data entry')
    print('your data has been updated')
    functions.select(name)
    change=input('do you want anymore changes..?? ')
mycon.close()
print('THANK YOU FOR USING OUR PROGRAM')
print('Hope you enjoyed it')
print('See you soon',name)
print('Have a nice day')


