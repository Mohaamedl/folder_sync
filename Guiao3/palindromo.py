from newQueue import Queue


def palindromo(s):
    v = True
    myQ = Queue()
    sSplit = list(filter((' ').__ne__, list(s)))
    print(sSplit)
    
    for e in sSplit:
        myQ.add(e)
    print(myQ)
    for e in sSplit: # para stack considerar ondem inversa ( pois se remove de tras)
        if myQ.first().lower() != e.lower(): 
            v=False
        myQ.remove()
    return v



print(palindromo('somos')) # true
print(palindromo('O galO nada no lago')) # true
print(palindromo('O galO nada hhhohoho lago')) # false