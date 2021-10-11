

#baglac = input("Lütfen İfadeyi Giriniz: ")




#hesplanmısbaglac = baglac.replace("V","or").replace("∧","and").replace("1" , "true").replace("0","false")


#sonuc = bool(hesplanmısbaglac)


#print(hesplanmısbaglac)
def ise(onerme1,onerme2):
    
    if onerme1>onerme2:
        return False
        
    else:
        return True


def yada(onerme1,onerme2):
    if onerme1 == onerme2:
        return False
    else:
        return True

def avea(onerme1,onerme2):
    if onerme1 == onerme2:
        return True
    else:
        return False
       
       


        
    
 
howmany = 0
true = 0
false = 0
trueorfalse=(1,0)

print("Olası Sonuçlar Şunlardır: ")
for p in trueorfalse:
    for q in trueorfalse:
        for r in trueorfalse:

           res = avea((yada((ise(((p or q) and (p or r)),avea(q,r))),yada(p,(ise(r,p))))),ise(yada(p,q),ise(q,r))) 
           
           equals = []
           howmany +=1
           print(f"p:{p} q:{q} r:{r} iken cevap {res}'tir")


        

           if res == 1:
             true +=1
           elif res ==0:
               false+=1

truepercentage = f"{true}/{howmany}"
falsepercentage = f"{false}/{howmany}"


print(f"Bu Önermenin Doğru Olma Olasılığı:{truepercentage} Yanlış Olma olasılığı:{falsepercentage}'dır.")
           