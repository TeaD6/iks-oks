#!/bin/python3

print("Ovo je nasa verzija XO igrice")

tabela=[[1,2,3],    [4,5,6],    [7,8,9]]

for r in tabela:print(r)
for a in ["X","O","X","O","X","O","X","O","X"]:
    pozicija=int(input(f"Enter {a}'s Move: "))
    print(f"Uneta Pozicija je {pozicija} red je {(pozicija-1)//3} kolona {(pozicija-1)%3}")
    tabela [(pozicija-1)//3] [(pozicija-1)%3] = a   
    for r in tabela:print(r)
    
    