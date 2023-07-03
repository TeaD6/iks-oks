#!/bin/python3

print("Ovo je nasa verzija XO igrice")

def rowData(table,row):
    return table[row]

def colData(table,col):
    return [r[col] for r in table]

def dijagonala(t,a):
    return t[0][0]==t[1][1]==t[2][2]==a or t[2][0]==t[1][1]==t[0][2]==a

tabela=[[1,2,3],    [4,5,6],    [7,8,9]]

for r in tabela:print(r)
odigrano=[]
kraj=0
for a in ["X","O","X","O","X","O","X","O","X"]:

    while True:
        pozicija=int(input(f"Enter {a}'s Move: "))
        if pozicija not in odigrano:
            odigrano.append(pozicija)
            break
    red=(pozicija-1)//3
    kolona=(pozicija-1)%3
    tabela [red] [kolona] = a
    
    for r in tabela:print(r)
    
    for e in [0,1,2]:
        if colData(tabela,e)[0]==colData(tabela,e)[1]==colData(tabela,e)[2]==a or \
            rowData(tabela,e)[0]==rowData(tabela,e)[1]==rowData(tabela,e)[2]==a or \
            dijagonala(tabela,a):
            print(f"{a} je pobedio")
            kraj=1
            break
    if kraj==1: break
        
    