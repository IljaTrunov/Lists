#nimed=["Anton", "Arturik"]
#for i in range (3):
    #nimi=input("sisesta nimi: ")
    #nimed.append(nimi)#добавление списка
#print(nimed)
#nimed.sort(reverse=True)#разворачивает список и сортирует его
#print(nimed)
#nimed.insert(1,input("sisesta veel nimi: "))
#print(nimed)
#nimed.remove("Anton")
#print(nimed)
#nimed.pop(2)
#print(nimed)
#print(len(nimed))
#nimed.count(nimed[0])
#1
#Maakonnad=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
    #try:
        #index=int(input())
        #if 10000<=index<=99999:
            #break
    #except ValueError:
       # print("Vale indeks!")
#index_1=index//10000
#print(Maakonnad[index_1-1])
#if index_1<=3:
    #print("Lähme kodus")
#else:
    #print("Kanna maski, kurad")
#2
#from random import *
#list=[]
#N=randint(2,20)
#for i in range(N):
	#list.append(randint(-50,50))
#print(list)
#while 1:
    #try:
        #k=int(input("Mis positsioonist alustada vahestust"))
        #if k<=N//2:
            #break
    #except ValueError:
            #print("Arv peab olema väiksem kui", N//2)
#k-=1
#for i in range(k,-1,-1):
    #print(list[i],end="<=>")
    #print(list[N-i-1])
    #a=list.pop(i)
    #list.insert(N-i-1-1,a)
    #a=list.pop(N-i-1)
    #list.insert(i,a)
#print(list)
#3
#max=-50
#for element in list:
    #if element>max: max=element
#new_max=max/N #len(list)
#list.index(max)
#ind=list.insert()
#list.remove(max)
#list.insert(ind,new_max)
#print(list)
#4
number=[]
for element in number:
    number.append(abs(element))
print(number.sort())
print(number.sort(reverse=True))
#5
s1=['крот', 'белка', 'выхухоль']
s2=['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
s3=['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
ss=[s1,s2,s3]
N=0
while N<3:
	print(ss[N])
	pikkem=0
	sN_=[]
	for s in ss[N]:
		pikkus=len(s)
		if pikkus>pikkem:pikkem=pikkus	
	for s in ss[N]:
		sN_.append(s.ljust(pikkem,"_"))
	print(sN_)
	N+=1



